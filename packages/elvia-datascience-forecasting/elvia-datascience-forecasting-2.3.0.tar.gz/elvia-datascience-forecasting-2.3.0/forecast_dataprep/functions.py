from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Tuple, Optional

import pandas as pd

from forecast_dataprep.data_enrichment.cyclical_features import add_cyclical_features
from forecast_dataprep.data_enrichment.delayed_features import add_delayed_consumption_feature
from forecast_dataprep.data_enrichment.national_holiday import add_national_holiday
from forecast_dataprep.data_enrichment.prices import add_prices
from forecast_dataprep.data_enrichment.school_holiday import add_school_holidays
from forecast_dataprep.data_enrichment.temperature import get_temperature_forecasts_from_metadata
from forecast_dataprep.data_enrichment.weekly_average import add_hour_of_the_week_average
from forecast_dataprep.data_fetching import get_dataframes, get_metadata
from forecast_dataprep.data_fetching.data_models import BigQueryBundle
from forecast_dataprep.data_ingestion.prediction import there_is_enough_historical_data
from forecast_dataprep.data_ingestion.shared import ingest_metadata_dataframe
from forecast_dataprep.data_ingestion.training import ingest_hourly_consumption_data
from forecast_dataprep.data_models import IngestmentOutput, ModelTargetList
from forecast_dataprep.data_enrichment.time_constants import TimeConstants
from forecast_dataprep.weather_api.data_models import WeatherApiBundle


def fetch_ingest_and_enrich(
        bq: BigQueryBundle,
        targets: ModelTargetList,
        timespan: Tuple[datetime, datetime],
        weather_api: WeatherApiBundle,
        training: bool = False,
        use_prices: bool = True,
        prediction_start: Optional[datetime] = None) -> pd.DataFrame:
    """
    Get data from BQ, then ingest and enrich it, so it can be used for training or prediction

    :param BigQueryBundle bq: Object with the BigQuery client and project details
    :param ModelTargetList targets: Object containing either meteringpoint or substation identifiers
    :param tuple timespan: datetime tuple with the start and end of the time period of interest
    :param WeatherApiBundle weather_api: Object with Weather API info and credentials
    :param bool training: True if training constraints should be applied on the data. False implies prediction.
    :param bool use_prices: If true, add the price information as an additional feature
    :param datetime prediction_start: Used only if not training. Adjusts the prediction horizon.
    """
    # Step 0: Check input types
    if not isinstance(targets, ModelTargetList):
        raise TypeError

    # Step 1: Get metadata
    dfm = get_metadata(bq, targets)

    # Step 2: Branching. Separate route that run simultaneously to minimise run time
    with ThreadPoolExecutor() as executor:
        path_1_task = executor.submit(main_ingestion_route, dfm, targets, bq,
                                      timespan, training, use_prices,
                                      prediction_start)
        path_2_task = executor.submit(get_temperature_forecasts_from_metadata,
                                      dfm, timespan, weather_api)
    df_ingestion: IngestmentOutput = path_1_task.result()
    df_temperature: pd.DataFrame = path_2_task.result()

    # Step 3: Merge route
    merged_hourly: pd.DataFrame = merge_routes(
        df_ingestion.ingested_hourly_data, df_temperature)

    # Step 4: Enrich
    return enrich_hourly_data(ingestment_output=IngestmentOutput(
        merged_hourly, df_ingestion.ingested_metadata,
        df_ingestion.enrichment_features),
                              timespan=timespan,
                              use_prices=use_prices,
                              prediction=not training)


def enrich_hourly_data(ingestment_output: IngestmentOutput,
                       timespan: Tuple[datetime, datetime], use_prices: bool,
                       prediction: bool) -> pd.DataFrame:
    """
    Adds features (cyclical, holidays, hour-of-the-week average consumption, shifted consumption, 
    price) to the ingested hourly data. The metadata dataframe needs to be enriched with fylke, 
    as this is needed to add the school holidays.

    :param bool use_prices: If true, add the price information as an additional feature
    :param bool prediction: If both use_prices and prediction are true, prices will be interpolated/extrapolated
    """

    ingested_hourly_data = add_cyclical_features(
        ingestment_output.ingested_hourly_data)

    ingested_hourly_data = add_national_holiday(
        ingested_hourly_data,
        ingestment_output.enrichment_features.national_holidays, timespan[0],
        timespan[1])

    ingested_hourly_data = add_hour_of_the_week_average(
        ingested_hourly_data,
        ingestment_output.enrichment_features.weekly_average)

    if use_prices:
        ingested_hourly_data = add_prices(
            ingested_hourly_data, ingestment_output.enrichment_features.prices,
            prediction)

    for delay in TimeConstants.DELAYED_FEATURES:
        ingested_hourly_data = add_delayed_consumption_feature(
            ingested_hourly_data, delay)

    ingested_hourly_data = add_school_holidays(
        ingested_hourly_data,
        ingestment_output.enrichment_features.school_holidays,
        ingestment_output.ingested_metadata, timespan[0], timespan[1])

    return ingested_hourly_data.sort_index()


def main_ingestion_route(
        raw_metadata: pd.DataFrame,
        model_targets: ModelTargetList,
        bq: BigQueryBundle,
        timespan: Tuple[datetime, datetime],
        training: bool,
        use_prices: bool,
        prediction_start: Optional[datetime] = None) -> IngestmentOutput:
    """
    This enrichment route is meant to run in parallel with :py:func:`~forecast_dataprep.data_enrichment.temperature.get_temperature_forecasts_from_metadata`

    :param pd.DataFrame raw_metadata: Result from :py:func:`~forecast_dataprep.data_fetching.__init__.get_metadata` 
    :param ModelTargetList model_targets: Object representing desired substations or meteringpoints
    :param BigQueryBundle bq: Object containing the BQ client and the BQ project name
    :param tuple timespan: datetime tuple with the start and end of the time period of interest
    :param bool training: If true, the hourly consumption data will be filtered using certain conditions
    :param bool use_prices: If true, add the price information as an additional feature
    :param datetime prediction_start: Point in time when one wants the prediction to start. Ignored if training
    :returns: EnrichmentInput 
    """
    dfm_ingested = ingest_metadata_dataframe(raw_metadata)

    dfs = get_dataframes(bq, model_targets, timespan, use_prices)

    if dfs.hourly_consumption is None or dfs.hourly_consumption.empty:
        raise ValueError('No hourly consumption data')

    if training:
        dfs.hourly_consumption = ingest_hourly_consumption_data(
            timespan, dfs.hourly_consumption)
        if dfs.hourly_consumption is None or dfs.hourly_consumption.empty:
            raise ValueError('No hourly consumption data')
    elif not there_is_enough_historical_data(
            dfs.hourly_consumption, TimeConstants.DELAYED_FEATURES,
            TimeConstants.FORECAST_HORIZON, prediction_start):
        raise ValueError('Not enough hourly consumption data')

    return IngestmentOutput(dfs.hourly_consumption, dfm_ingested, dfs.ingested)


def merge_routes(ingested_hourly_data: Optional[pd.DataFrame],
                 temperature_data: pd.DataFrame) -> Optional[pd.DataFrame]:
    """
    Intermediate stage following data ingestion. 
    
    :param pd.DataFrame ingested_hourly_data: Result from :py:func:`~forecast_dataprep.methods.main_ingestion_route` 
    :param pd.DataFrame temperature_data: Result from :py:func:`~forecast_dataprep.data_enrichment.temperature.get_temperature_forecasts_from_metadata` 
    :returns: pd.DataFrame or None if any of the input dataframes is either empty or None
    """
    if ingested_hourly_data is not None \
        and not ingested_hourly_data.empty and not temperature_data.empty:
        return ingested_hourly_data.reset_index().merge(
            temperature_data.rename(columns={'time': 'measurementTime'}),
            on=['measurementTime', 'modelTargetId'],
            how='outer').set_index('measurementTime')
    return None
