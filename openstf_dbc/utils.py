import datetime

import pandas as pd

DEFAULT_FREQ = "15min"
DEFAULT_TZ = datetime.timezone.utc


def genereate_datetime_index(start, end, freq=None):
    # Use timezone info from start if given
    if start.tzinfo:
        tz = start.tzinfo
    # Else use default timezone
    else:
        tz = DEFAULT_TZ

    if not freq:
        freq = DEFAULT_FREQ

    return pd.date_range(
        start=start,
        end=end,
        freq=freq,
        tz=tz,
    )
