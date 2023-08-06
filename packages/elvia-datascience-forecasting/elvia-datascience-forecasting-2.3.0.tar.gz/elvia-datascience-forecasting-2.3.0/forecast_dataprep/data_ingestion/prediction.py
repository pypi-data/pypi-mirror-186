from datetime import datetime, timedelta
from typing import List, Optional

import pandas as pd

from .shared import set_measurement_time_as_dataframe_index


def there_is_enough_historical_data(
        hourly: pd.DataFrame,
        feature_delays: List[int],
        forecast_horizon: int,
        desired_prediction_start: Optional[datetime] = None) -> bool:
    """
    Check whether there is enough historical consumption data in order to construct the "delayed" 
    features. measurementTime is expected as dataframe index.
    
    :param pd.DataFrame hourly: Historical consumption. The index should be of type DateTimeIndex.
    :param list feature_delays: Number of hours that the feature will shift the consumption values
    :param int forecast_horizon: Length of the forecast horizon. Needed to calculate the time ranges.
    :param datetime desired_prediction_start: Optional. Desired point in time when the prediction starts. If None, deduced from the dataframe index.
    
    :rtype: bool
    :returns: True if there's enough data
    """

    if not hourly.size:
        raise ValueError('Empty dataframe')

    set_measurement_time_as_dataframe_index(hourly)

    if desired_prediction_start is None:
        desired_prediction_start = max(pd.to_datetime(
            hourly.index)).to_pydatetime() + timedelta(hours=1)

    for feature_delay in feature_delays:
        # Required hours to create this feature
        hours_required = pd.date_range(
            start=desired_prediction_start - timedelta(hours=feature_delay),
            end=desired_prediction_start - timedelta(hours=feature_delay) +
            timedelta(hours=forecast_horizon),
            freq='H',
            tz='utc')

        # Interesection between required hours and existing hours
        missing_hours = [
            hour_req for hour_req in hours_required
            if hour_req not in hourly.index
        ]
        if missing_hours:
            return False

    return True
