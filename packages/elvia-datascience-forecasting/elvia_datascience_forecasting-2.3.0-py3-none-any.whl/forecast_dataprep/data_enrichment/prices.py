import pandas as pd

from forecast_dataprep.data_ingestion.shared import set_measurement_time_as_dataframe_index, interpolate_extrapolate_series


def add_prices(hourly: pd.DataFrame, prices: pd.DataFrame,
               prediction: bool) -> pd.DataFrame:
    """
    This function adds price data.
    If prediction, missing values are interpolated, except for those at the beginning of the series.
    """

    if prediction:
        prices = prices[prices.first_valid_index():]
        prices = interpolate_extrapolate_series(prices['price'])

    set_measurement_time_as_dataframe_index(hourly)

    result = hourly.merge(prices,
                          left_index=True,
                          right_index=True,
                          how='left')
    result.index.name = 'measurementTime'

    return result
