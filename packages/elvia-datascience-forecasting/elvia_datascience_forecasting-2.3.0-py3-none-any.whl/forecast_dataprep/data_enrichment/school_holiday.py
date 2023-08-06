import pandas as pd
from datetime import datetime

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index


def _process_school_holiday_data(school_holidays: pd.DataFrame,
                                 metadata: pd.DataFrame,
                                 timespan_start: datetime,
                                 timespan_end: datetime) -> pd.DataFrame:
    """
    Prepares the school holiday information for a given time range of interest.
    The result can later be used to enrich the hourly data by merging on time.

    :param pd.DataFrame school_holidays: Dataframe containing local school holiday information.
    :param pd.DataFrame metadata: Dataframe containing metadata for the desired model targets.
    :param datetime timespan_start: Start of the time period of interest.
    :param datetime timespan_end: End of the time period of interest.
    :returns: Dataframe containing modelTargetId, timestamps and a boolean column schoolHoliday
    :raises KeyError: If school_holidays doesn't contain columns: fromTime, toTime , region; Or if metadata doesn't contain columns: modelTargetId, fylke
    """

    date_range: pd.DatetimeIndex = pd.date_range(start=timespan_start,
                                                 end=timespan_end,
                                                 freq='H',
                                                 tz='UTC')
    dft = pd.DataFrame(data=date_range, columns=['time'])

    # Cartesian product between these 2 gives us all possible combinations
    df = dft.merge(school_holidays, how='cross')

    # We keep only those entries that fall between the from- and to- dates
    df['schoolHoliday'] = (df['fromTime'] < df['time']) & (df['time'] <=
                                                           df['toTime'])

    # We drop what we don't need
    df.drop(columns=['fromTime', 'toTime', 'holiday'], inplace=True)
    df.drop_duplicates(inplace=True)

    # We now do the cartesian product with the metadata dataframe, in order to link holiday
    # and region to the modelTargetIds
    df = df.merge(metadata.loc[:, ['modelTargetId', 'fylke']], how='cross')

    # This time we filter out the nonsense by requiring a match on the fylke and region columns
    df.drop(df[df.fylke != df.region].index, inplace=True)
    df.drop(columns=['region', 'fylke'], inplace=True)

    df.rename(columns={'time': 'measurementTime'}, inplace=True)
    df.set_index('measurementTime', inplace=True)

    df['schoolHoliday'] = df['schoolHoliday'].astype(float)

    return df


def add_school_holidays(hourly: pd.DataFrame, school_holidays: pd.DataFrame,
                        metadata: pd.DataFrame, timespan_start: datetime,
                        timespan_end: datetime) -> pd.DataFrame:
    """
    Add the school holiday feature to the input dataframe.    

    :param pd.DataFrame hourly: Dataframe containing hourly consumption data
    :param pd.DataFrame school_holidays: Dataframe containing local school holiday information.
    :param pd.DataFrame metadata: Dataframe containing metadata for the desired model targets.
    :param datetime timespan_start: Start of the time period of interest.
    :param datetime timespan_end: End of the time period of interest.
    :returns: Hourly dataframe with the school holidays feature
    :raises KeyError: If school_holidays doesn't contain columns: fromTime, toTime , region; Or if metadata doesn't contain columns: modelTargetId, fylke; Or if df doesn't contain columns: modelTargetId, index (as or column) measurementTime
    """
    # We reset the indices because we will be doing a multicolumn merge at the end
    if isinstance(hourly.index, pd.DatetimeIndex):
        hourly.reset_index(inplace=True)

    sh = _process_school_holiday_data(school_holidays, metadata,
                                      timespan_start, timespan_end)

    if isinstance(sh.index, pd.DatetimeIndex):
        sh.reset_index(inplace=True)

    hourly = hourly.merge(sh,
                          on=['measurementTime', 'modelTargetId'],
                          how='left')

    # There may be NaNs if the school holiday dataframe is empty
    hourly['schoolHoliday'].fillna(0, inplace=True)

    set_measurement_time_as_dataframe_index(hourly)

    return hourly
