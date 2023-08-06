import pandas as pd
from datetime import datetime

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index

TIME_INDEX_NAME = 'measurementTime'


def _process_national_holiday_data(national_holidays: pd.DataFrame,
                                   timespan_start: datetime,
                                   timespan_end: datetime) -> pd.DataFrame:
    """
    Prepares the national holiday information for a given time range of interest.
    The result can later be used to enrich the hourly matrix by merging against it on time.

    :param pd.DataFrame national_holidays: Dataframe containing national holiday information.
    :param datetime timespan_start: Start of the time period of interest.
    :param datetime timespan_end: End of the time period of interest.
    :returns: Dataframe containing timestamps and a boolean column nationalHoliday
    :raises KeyError: If national_holidays doesn't contain columns: fromTime, toTime 
    """

    date_range: pd.DatetimeIndex = pd.date_range(start=timespan_start,
                                                 end=timespan_end,
                                                 freq='H',
                                                 tz='UTC')
    dft = pd.DataFrame(data=date_range, columns=['time'])
    df = dft.merge(national_holidays, how='cross')
    df['nationalHoliday'] = (df['fromTime'] < df['time']) & (df['time'] <=
                                                             df['toTime'])
    df.drop(columns=['fromTime', 'toTime', 'holiday'], inplace=True)
    df.drop_duplicates(inplace=True)
    df.set_index('time', inplace=True)

    df['nationalHoliday'] = df['nationalHoliday'].astype(float)
    return df


def add_national_holiday(hourly: pd.DataFrame, national_holidays: pd.DataFrame,
                         timespan_start: datetime,
                         timespan_end: datetime) -> pd.DataFrame:
    """
    Enrich by adding a national holiday feature to the hourly consumption data.

    :param pd.DataFrame hourly: Dataframe containing hourly consumption data
    :param pd.DataFrame national_holidays: Dataframe containing national holiday information.
    :param datetime timespan_start: Start of the time period of interest.
    :param datetime timespan_end: End of the time period of interest.
    """

    set_measurement_time_as_dataframe_index(hourly)

    nh: pd.DataFrame = _process_national_holiday_data(national_holidays,
                                                      timespan_start,
                                                      timespan_end)

    result = hourly.merge(nh, left_index=True, right_index=True, how='left')

    # There may be NaNs if the national_holidays dataframe is empty
    result['nationalHoliday'].fillna(0, inplace=True)

    result.index.name = TIME_INDEX_NAME

    return result
