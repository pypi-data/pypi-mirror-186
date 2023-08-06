from datetime import datetime
from typing import Tuple
import pandas as pd

from forecast_dataprep.weather_api.data_models import Location, WeatherApiBundle
from forecast_dataprep.weather_api.wrapper import get_temperature_forecasts


def get_temperature_forecasts_from_metadata(
        raw_metadata: pd.DataFrame, timespan: Tuple[datetime, datetime],
        weather_api: WeatherApiBundle) -> pd.DataFrame:
    """
    From a metadata dataframe containing columns modelTargetId, latitude and longitude,
    generate a dataframe with columns time, modelTargetId, temperature containing past and/or 
    future forecast temperature data from Weather API.
    
    :params pd.DataFrame raw_metadata: metadata dataframe, previous ingestion not necessary
    :param tuple timespan: Start and end of the prediction/training time interval
    :param WeatherApiBundle weather_api: Weather API info and credentials
    :returns: Dataframe with time, temperature and location, if success
    """

    if not isinstance(raw_metadata, pd.DataFrame) or not all(
        [_ in raw_metadata.columns for _ in ['latitude', 'longitude']]):
        raise KeyError('Malformed metadata')

    locations = [
        Location(_[0], _[1]) for _ in raw_metadata[['latitude', 'longitude'
                                                    ]].drop_duplicates().values
    ]

    if not locations:
        raise ValueError('No locations')

    dftemp: pd.DataFrame = get_temperature_forecasts(timespan, locations,
                                                     weather_api)

    return raw_metadata.merge(
        dftemp.reset_index(),
        on=['latitude',
            'longitude']).loc[:, ['modelTargetId', 'temperature', 'time']]
