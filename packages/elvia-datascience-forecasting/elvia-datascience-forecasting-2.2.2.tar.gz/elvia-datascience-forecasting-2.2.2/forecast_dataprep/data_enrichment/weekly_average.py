import pandas as pd

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index


def add_hour_of_the_week_average(hourly: pd.DataFrame,
                                 weekly: pd.DataFrame) -> pd.DataFrame:
    """
    Add the weekly average consumption feature to the hourly dataframe

    :param pd.DataFrame hourly: Hourly consumption dataframe
    :param pd.DataFrame weekly: Weekly averaged consumption dataframe    
    :returns: The hourly dataframe with the weekly feature added to it
    """

    # We must ensure the index is set before we access its datetime properties
    set_measurement_time_as_dataframe_index(hourly)
    hourly['hourOfWeek'] = 24 * hourly.index.day_of_week + hourly.index.hour

    if isinstance(weekly.index, pd.DatetimeIndex):
        weekly.reset_index(inplace=True)
    weekly.rename(columns={'energyWh': 'hourOfWeekAverage'}, inplace=True)

    # We need to temporarily unset the index in order to do a multi-column merge
    hourly.reset_index(inplace=True)
    hourly = hourly.merge(weekly, on=['modelTargetId', 'hourOfWeek'])

    hourly.drop(columns=['hourOfWeek'], inplace=True)

    # Set the index again
    hourly.set_index('measurementTime', inplace=True)

    return hourly
