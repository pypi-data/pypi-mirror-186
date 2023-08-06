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
