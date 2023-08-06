import pandas as pd

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index


def add_prices(hourly: pd.DataFrame, prices: pd.DataFrame) -> pd.DataFrame:
    """
    This function adds price data
    """
    set_measurement_time_as_dataframe_index(hourly)

    result = hourly.merge(prices,
                          left_index=True,
                          right_index=True,
                          how='left')
    result.index.name = 'measurementTime'

    return result
