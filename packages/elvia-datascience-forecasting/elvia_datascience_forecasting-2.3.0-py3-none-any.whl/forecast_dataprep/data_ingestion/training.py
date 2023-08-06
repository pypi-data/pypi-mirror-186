from datetime import datetime, timedelta
from typing import Tuple

import numpy as np
import pandas as pd

from .shared import set_measurement_time_as_dataframe_index

SECONDS_HOUR = 60 * 60


def _discard_model_targets_with_too_many_consumption_zeros(
        hourly: pd.DataFrame, threshold: float = 0.1) -> pd.DataFrame:
    """
    Remove from the input dataframe those model targets for which the consumption is
    zero too often. 
    The index is expected to be of type DatetimeIndex and named measurementTime.

    :param pd.DataFrame df: Pandas dataframe with columns modelTargetId, energyWh.
    :param threshold float: Fraction of the energy consumption values that can be zero, above which model targets are discarded. Between 0 and 1.

    :raises: KeyError if expected column titles are missing from dataframe.
    :rtype: pd.DataFrame    
    """
    set_measurement_time_as_dataframe_index(hourly)

    if not all([_ in hourly.columns for _ in ['modelTargetId', 'energyWh']]):
        raise KeyError('Expected columns are missing')

    # Group by modelTargetId and count zeros for each column
    count_zeros = hourly.groupby('modelTargetId').agg(lambda x: x.eq(0).sum())

    # Deduce the number of rows based on the unique timestamps
    len_history = hourly.index.value_counts().count()

    # We need to reset the index for the next step to work
    hourly.reset_index(inplace=True)

    # Apply condition and get the modelTargetId values to be excluded
    # empty_trafo_idx is a CategoricalIndex
    empty_trafo_idx = count_zeros.loc[count_zeros['energyWh'] > len_history *
                                      threshold].index

    if not empty_trafo_idx.empty:
        hourly = hourly.drop(index=hourly.loc[hourly['modelTargetId'].isin(
            empty_trafo_idx)].index)

    return hourly.set_index('measurementTime')


def _discard_model_targets_with_too_few_datapoints(
        hourly: pd.DataFrame,
        span_in_hours: int,
        threshold: float = 0.9) -> pd.DataFrame:
    """
    Remove from the input dataframe those model targets for which the number of historical 
    datapoints is below a given threshold. Assumes that all datapoints in the dataframe lie 
    within the time range of interest

    Requires index of type DateTimeIndex to be set or as a column called measurementTime.

    :param pd.DataFrame hourly: Pandas dataframe with required columns: modelTargetId
    :param int span_in_hours: Total time span with which one wants to train.
    :param threshold float: Fraction of the energy consumption values that can be zero, under which model targets are discarded. Between 0 and 1.
    
    :raises: ValueError if missing columns
    :rtype: pd.DataFrame    
    """

    set_measurement_time_as_dataframe_index(hourly)

    if 'modelTargetId' not in hourly.columns:
        raise ValueError('Expected modelTargetId column is missing')

    # Group by modelTargetId and calculate lengths
    lengths = hourly.groupby('modelTargetId').agg(lambda x: x.notnull().sum())

    # Apply condition and get the modelTargetId values to be excluded
    # empty_trafo_idx is a CategoricalIndex
    bad_idx = lengths.loc[lengths.min(axis=1) < span_in_hours *
                          threshold].index

    if not bad_idx.empty:
        hourly = hourly.drop(
            index=hourly.loc[hourly['modelTargetId'].isin(bad_idx)].index)

    return hourly


def _interpolate_outliers(hourly: pd.DataFrame,
                          window_hours: int = 30 * 24,
                          sigmas_threshold: float = 5):
    """
    Correct consumption outliers that are too many sigmas away from the mean.
    The outliers are replaced with an linear interpolation of values in the vecinity that 
    aren't too far from the mean.

    Values are changed in place. 

    :param pd.DataFrame hourly: Dataframe with mandatory columns targetModelId, energyWh
    :param int window_hours: Time window used in the calculations
    :param float sigmas_threshold: The threshold, measured in standard deviations. The smaller the value, the stricter the criterion.
    :rtype: None
    """
    for index in list(hourly['modelTargetId'].unique()):

        row_selection = hourly['modelTargetId'] == index

        # Calculate a rolling mean
        hourly.loc[row_selection,
                   'mean'] = hourly.loc[row_selection, 'energyWh'].rolling(
                       timedelta(hours=window_hours)).mean().fillna(
                           method='bfill').fillna(method='ffill')

        # Put the sigmas-based indicator in a new column.
        # The std function returns a scalar.
        hourly.loc[row_selection, 'sigmas_off'] = (
            hourly.loc[row_selection, 'mean'] -
            hourly.loc[row_selection, 'energyWh']) / max(
                1, hourly.loc[row_selection, 'energyWh'].std(ddof=0))

        # A new column where we store whether the outlier condition is true
        hourly.loc[row_selection, 'interpolate'] = hourly.loc[
            row_selection, 'sigmas_off'].where(
                (hourly.loc[row_selection, 'sigmas_off'] < sigmas_threshold)
                & (hourly.loc[row_selection,
                              'sigmas_off'] > -sigmas_threshold))

        # Put NaNs where the bad behaved values are
        hourly.loc[(hourly['interpolate'].isna() == True) & (row_selection),
                   'energyWh'] = np.nan

        # Replace the bad values with well-behaved interpolations
        hourly.loc[row_selection,
                   'energyWh'] = hourly.loc[row_selection,
                                            'energyWh'].interpolate(
                                                method='ffill',
                                                inplace=False).astype(float)

        hourly.drop(columns=['mean', 'sigmas_off', 'interpolate'],
                    inplace=True)


def ingest_hourly_consumption_data(timespan: Tuple[datetime, datetime],
                                   hourly: pd.DataFrame,
                                   zeros_threshold: float = 0.25,
                                   datapoints_threshold: float = 0.95,
                                   interpolation_window: timedelta = timedelta(
                                       days=30),
                                   sigmas_away: float = 5) -> pd.DataFrame:
    """
    This function is only meant to be used when building a training set:
    - Remove modelTargets that have too many zeros
    - Remove modelTargets with insufficient datapoints
    - Interpolate consumption outliers
    """

    hourly = _discard_model_targets_with_too_many_consumption_zeros(
        hourly, zeros_threshold)

    span_in_hours = int(
        (timespan[1] - timespan[0]).total_seconds() / SECONDS_HOUR)
    hourly = _discard_model_targets_with_too_few_datapoints(
        hourly, span_in_hours, datapoints_threshold)

    window_hours = int(interpolation_window.total_seconds() / SECONDS_HOUR)
    _interpolate_outliers(hourly,
                          window_hours=window_hours,
                          sigmas_threshold=sigmas_away)

    return hourly
