"""
This module has the highest level functions for fetching data from Edna BQ
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Optional, Tuple

import pandas as pd

from forecast_dataprep.data_fetching.data_models import BigQueryBundle
from forecast_dataprep.data_models import Dataframes, EnrichmentFeaturesBundle, ModelTargetList, ModelTargetLevel
from forecast_dataprep.data_fetching.common import get_hourly_data, get_national_holidays, get_prices, get_school_holidays, get_weekly_data
from forecast_dataprep.data_fetching.meteringpoints import get_meteringpoint_metadata
from forecast_dataprep.data_fetching.substations import get_substation_metadata


def get_dataframes(bq: BigQueryBundle, targets: ModelTargetList,
                   timespan: Tuple[datetime,
                                   datetime], use_prices: bool) -> Dataframes:
    """
    Query Edna tables and fetch data, returned as dataframes.
    The substation/meteringpoint metadata is not part of this group of queries, in order to 
    optimise the overall execution order.

    :param bool use_prices: Price data will be included if true
    """
    with ThreadPoolExecutor() as executor:
        dfh = executor.submit(get_hourly_data, bq, targets, timespan)
        dfw = executor.submit(get_weekly_data, bq, targets)
        dfnh = executor.submit(get_national_holidays, bq, timespan[0],
                               timespan[1])
        dfsh = executor.submit(get_school_holidays, bq, timespan[0],
                               timespan[1])
        if use_prices:
            dfp = executor.submit(get_prices, bq, timespan[0], timespan[1])
            dfp = dfp.result()
        else:
            dfp = pd.DataFrame(columns=['price', 'measurementTime']).set_index(
                'measurementTime')

    dfh = dfh.result()
    dfw = dfw.result()
    dfnh = dfnh.result()
    dfsh = dfsh.result()

    return Dataframes(dfh, EnrichmentFeaturesBundle(dfw, dfsh, dfnh, dfp))


def get_metadata(bq: BigQueryBundle,
                 targets: ModelTargetList) -> Optional[pd.DataFrame]:
    """
    Get meteringpoint/substation metadata. 
    The result contains columns latitude and longitude that are needed to get the right forecast
    data from Weather API. It also contains column postalCode, which is needed to enrich with the
    location-dependant school holidays feature.
    """
    if targets.level == ModelTargetLevel.METERING_POINT:
        return get_meteringpoint_metadata(bq, targets.identifiers)
    elif targets.level == ModelTargetLevel.SUBSTATION:
        return get_substation_metadata(bq, targets.identifiers)
    return None
