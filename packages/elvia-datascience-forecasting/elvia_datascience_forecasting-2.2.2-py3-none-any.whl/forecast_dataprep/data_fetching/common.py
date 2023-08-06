"""
This module contains functions with queries against Edna BQ
"""
from datetime import datetime, timedelta
from typing import Optional, Tuple

from google.cloud import bigquery
from google.cloud.bigquery.job import QueryJob
import pandas as pd

from forecast_dataprep.data_fetching.data_models import BigQueryBundle
from forecast_dataprep.data_models import ModelTargetLevel, ModelTargetList
from forecast_dataprep.data_fetching.meteringpoints import get_meteringpoint_hourly_data, get_meteringpoint_weekly_data
from forecast_dataprep.data_fetching.substations import get_substation_hourly_data, get_substation_weekly_data


def get_hourly_data(
    bq: BigQueryBundle,
    targets: ModelTargetList,
    timespan: Optional[Tuple[datetime, datetime]] = None
) -> Optional[pd.DataFrame]:

    if targets.level == ModelTargetLevel.METERING_POINT:
        return get_meteringpoint_hourly_data(bq, targets.identifiers, timespan)
    elif targets.level == ModelTargetLevel.SUBSTATION:
        return get_substation_hourly_data(bq, targets.identifiers, timespan)
    return None


def get_weekly_data(bq: BigQueryBundle,
                    targets: ModelTargetList) -> pd.DataFrame:

    if targets.level == ModelTargetLevel.METERING_POINT:
        return get_meteringpoint_weekly_data(bq, targets.identifiers)
    elif targets.level == ModelTargetLevel.SUBSTATION:
        return get_substation_weekly_data(bq, targets.identifiers)
    return None


def get_national_holidays(bq: BigQueryBundle, from_time: datetime,
                          to_time: datetime):
    query = (
        "SELECT fromTime, toTime, holiday "
        f"FROM `{bq.project.name}.{bq.project.dataset}.{bq.project.national_holiday}` "
        "WHERE fromTime < @to_time "
        "AND toTime > @from_time ")

    job_config = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter("from_time", "TIMESTAMP", from_time),
        bigquery.ScalarQueryParameter("to_time", "TIMESTAMP", to_time)
    ])
    query_job: QueryJob = bq.client.query(query, job_config=job_config)

    result = query_job.result().to_dataframe(create_bqstorage_client=False)
    return result


def get_school_holidays(bq: BigQueryBundle, from_time: datetime,
                        to_time: datetime):
    query = (
        "SELECT fromTime, toTime, holiday, region "
        f"FROM `{bq.project.name}.{bq.project.dataset}.{bq.project.school_holiday}` "
        "WHERE fromTime < @to_time "
        "AND toTime > @from_time ")

    job_config = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter("from_time", "TIMESTAMP", from_time),
        bigquery.ScalarQueryParameter("to_time", "TIMESTAMP", to_time)
    ])
    query_job: QueryJob = bq.client.query(query, job_config=job_config)

    result = query_job.result().to_dataframe(create_bqstorage_client=False)
    return result


def get_prices(bq: BigQueryBundle,
               from_time: datetime,
               to_time: datetime,
               extrapolate: bool = True):
    """
    Fetch prices.

    :param bool extrapolate: If true, fill out future prices with the prices from the last known day
    """
    query = (
        "SELECT EndTime AS t, Value AS price "
        f"FROM `{bq.project.name}.{bq.project.prices_dataset}.{bq.project.prices_table}` "
        "WHERE EndTime < @to_time AND EndTime > @from_time ")

    job_config = bigquery.QueryJobConfig(query_parameters=[
        bigquery.ScalarQueryParameter("from_time", "TIMESTAMP", from_time),
        bigquery.ScalarQueryParameter("to_time", "TIMESTAMP", to_time)
    ])
    query_job: QueryJob = bq.client.query(query, job_config=job_config)

    prices: pd.DataFrame = query_job.result().to_dataframe(
        create_bqstorage_client=False)

    prices.set_index('t', inplace=True)
    prices.sort_index(inplace=True)

    result: pd.DataFrame = _add_empty_rows_for_datapoints_in_the_future(
        prices, from_time, to_time)

    if extrapolate:
        return _extrapolate_missing_future_prices(result)
    return result


def _add_empty_rows_for_datapoints_in_the_future(prices: pd.DataFrame,
                                                 from_time: datetime,
                                                 to_time: datetime):
    required_times = pd.DataFrame(
        pd.date_range(from_time, to_time, freq='1H', tz='utc')).set_index(0)
    required_times.index.name = 't'
    required_times.sort_index(inplace=True)
    result = prices.merge(required_times,
                          left_index=True,
                          right_index=True,
                          how='outer')
    result.index.name = 'measurementTime'
    return result


def _extrapolate_missing_future_prices(prices: pd.DataFrame):
    """
    NaNs will remain if there is data for corresponding previous points in time
    """
    prices.sort_index(inplace=True)
    for _ in prices[prices['price'].isna() == True].index:
        if _ - timedelta(days=1) in prices.index:
            prices.loc[_] = prices.loc[_ - timedelta(days=1)]

    return prices
