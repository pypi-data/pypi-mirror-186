from numpy import sin, cos, pi
import pandas as pd

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index


def _add_trigonometric_transformations(
        df: pd.DataFrame, feature_name: str,
        feature_max_value: float) -> pd.DataFrame:
    """
    This function adds trigonometric transformations of a cyclical feature.
    We assume this will make the cyclical nature of these features more obvious to the model.
    The dataframe index does not play a role.

    :param pd.DataFrame df: Dataframe containing feature_name among its columns
    :param str feature_name: Name of the column that will be transformed
    :param float feature_max_value: Maximum value feature_name can take. Used to normalise.
    :returns: The dataframe with the transformed cyclical features
    """
    df[feature_name + '_sin'] = sin(2 * pi * df[feature_name] /
                                    feature_max_value)
    df[feature_name + '_cos'] = cos(2 * pi * df[feature_name] /
                                    feature_max_value)

    return df


def add_cyclical_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function adds the cyclical features, i.e. day of the week, month of the year etc.    

    :param pd.DataFrame df: Dataframe with index of type DatetimeIndex or with a datetime column named measurementTime
    :returns: The dataframe, with the cyclical features added to it.
    :raises KeyError: If the index isn't set and measurementTime isn't among the columns
    """
    set_measurement_time_as_dataframe_index(df)

    df['hourOfDay'] = df.index.hour
    df['dayOfWeek'] = df.index.day_of_week
    df['monthOfYear'] = df.index.month

    df = _add_trigonometric_transformations(df, 'hourOfDay', 24)
    df = _add_trigonometric_transformations(df, 'dayOfWeek', 7)
    df = _add_trigonometric_transformations(df, 'monthOfYear', 12)

    df.drop(columns=['hourOfDay', 'dayOfWeek', 'monthOfYear'], inplace=True)

    return df
