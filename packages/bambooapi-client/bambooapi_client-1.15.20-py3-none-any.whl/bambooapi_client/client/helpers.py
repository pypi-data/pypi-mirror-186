# noqa: D100
from typing import Any, Dict, List

from pandas import DataFrame, DatetimeIndex


def convert_time_index_to_utc(df: DataFrame) -> None:
    """Convert dataframe time index timezone to UTC.

    Note
    ----
    Pandas uses python-dateutil to parse datetimes. Even if the timestamp
    timezone is clearly UTC, dateutils may assign either tzlocal() or
    tzutc(). The way it is assigned is not consistent, and may depend on the
    machine running this code.
    https://github.com/dateutil/dateutil/issues/349
    https://github.com/dateutil/dateutil/issues/842

    Examples
    --------
    >>> df = DataFrame(
    ...     [[25.0]],
    ...     columns=['power'],
    ...     index=DatetimeIndex(
    ...         ['1992-05-01T00:00:00+01:00'],
    ...         name='time',
    ...     ),
    ... )
    >>> convert_time_index_to_utc(df)
    >>> df.index
    DatetimeIndex(['1992-04-30 23:00:00+00:00'], dtype='datetime64[ns, UTC]', name='time', freq=None)
    """  # noqa: E501
    df.index = df.index.tz_convert('UTC')


def to_datapoints(df: DataFrame) -> List[Dict[str, Any]]:
    """Transform dataframe to list of records, removing NaN values."""
    return [v.dropna().to_dict() for k, v in df.reset_index().iterrows()]
