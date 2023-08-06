from datetime import timedelta

import numpy as np
import pandas as pd

fylker = pd.DataFrame(data={
    3: 'Oslo',
    11: 'Rogaland',
    15: 'Møre og Romsdal',
    18: 'Nordland',
    30: 'Viken',
    34: 'Innlandet',
    38: 'Vestfold og Telemark',
    42: 'Agder',
    46: 'Vestland',
    50: 'Trøndelag',
    54: 'Troms og Finnmark'
}.items(),
                      columns=['fylkesnummer',
                               'fylke']).astype({'fylke': 'category'})


def add_fylkesnavn(metadata: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a categorical column named fylke.
    
    :raises KeyError: Requires municipalityNo to be present in the input columns.
    """
    metadata['fylkesnummer'] = np.floor(
        (metadata['municipalityNo'].astype(int) / 100)).astype(int)
    metadata = metadata.merge(fylker, on='fylkesnummer')
    return metadata.drop(columns=['fylkesnummer'])


def set_measurement_time_as_dataframe_index(df: pd.DataFrame) -> None:
    """
    Ensure the index is set, else set it from a column with name measurementTime.

    :raises: KeyError if failure
    """

    if not isinstance(df.index, pd.DatetimeIndex):
        if 'measurementTime' not in df.columns:
            raise KeyError('Wrong index')
        df.set_index('measurementTime', inplace=True)


def ingest_metadata_dataframe(metadata: pd.DataFrame) -> pd.DataFrame:
    return add_fylkesnavn(metadata)


def interpolate_extrapolate_series(dfp: pd.Series,
                                   dt_hours: int = 24) -> pd.Series:
    """
    Interpolate and/or extrapolate data. 
    Assumes a complete index with 1 hour intervals.
    
    :param pd.Series dfp: Time series, with Nans in the future or just missing values in the middle
    :param int dt_hours: Period duration, in hours, to use while filling the NaNs
    :return: Time series where the NaNs are replaced with interpolated/extrapolated values
    """

    dfp.sort_index(inplace=True)

    # Is interpolation/extrapolation needed?
    if not dfp.isna().any():
        return dfp

    # We want at least the first dt_hours to not be NaNs
    if dfp.index[:dt_hours].isna().any():
        raise ValueError(
            'Not enough data while attempting to interpolate data')

    ready = False
    while not ready:
        # Get the next NaN and its replacement, e.g. from a reasonably similar point in time in the past
        t_nan = dfp.isna().idxmax(axis=0)
        t_value = t_nan - timedelta(hours=dt_hours)

        if not dfp.index.isin([t_value]).any():
            raise ValueError(
                'Index gaps were found while attempting to interpolate data')

        # Account for possible duplicates
        if isinstance(dfp.at[t_value], pd.Series):
            replacement = dfp.at[t_value].iat[0]
        else:
            replacement = dfp.at[t_value]

        # Forward fill with our estimate
        dfp.at[t_nan] = replacement

        # Are we done?
        ready = not dfp.isna().any()

    return dfp
