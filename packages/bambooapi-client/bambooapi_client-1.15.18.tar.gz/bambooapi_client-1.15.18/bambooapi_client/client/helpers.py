# noqa: D100
import pandas as pd


def convert_time_index_to_utc(df: pd.DataFrame) -> None:
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
    >>> df = pd.DataFrame(
    ...     [[25.0]],
    ...     columns=['power'],
    ...     index=pd.DatetimeIndex(
    ...         ['1992-05-01T00:00:00+01:00'],
    ...         name='time',
    ...     ),
    ... )
    >>> convert_time_index_to_utc(df)
    >>> df.index
    DatetimeIndex(['1992-04-30 23:00:00+00:00'], dtype='datetime64[ns, UTC]', name='time', freq=None)
    """  # noqa: E501
    df.index = df.index.tz_convert('UTC')
