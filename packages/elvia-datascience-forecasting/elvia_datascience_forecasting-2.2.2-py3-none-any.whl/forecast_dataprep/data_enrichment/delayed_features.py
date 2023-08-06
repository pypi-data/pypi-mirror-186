import pandas as pd


def add_delayed_consumption_feature(
        hourly: pd.DataFrame,
        delay_hours: int,
        feature_name_prefix: str = 'energyWh_') -> pd.DataFrame:
    """
    This function repeats the hourly consumption column, but the values are shifted forwards in 
    time by a certain amount of hours. This tells the model what the consumption was earlier that
    week, which happens to be a good predictor for future consumption.

    :param pd.DataFrame hourly: Dataframe with a DatetimeIndex index
    :param int delay_hours: The time shift of the column that will be added, in hours
    :param str feature_name_prefix: Prefix to be added at the start of the feature name
    :returns: Dataframe with a DatetimeIndex index
    """
    feature_name = feature_name_prefix + str(delay_hours)
    hourly[feature_name] = hourly.groupby('modelTargetId')['energyWh'].shift(
        periods=delay_hours)

    return hourly
