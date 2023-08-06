"""PTR time module."""

import re
from datetime import date, datetime, timedelta


def dt(time) -> datetime:
    """Datetime parser."""
    if isinstance(time, datetime):
        return time

    if isinstance(time, date):
        return datetime(time.year, time.month, time.day)

    if hasattr(time, 'item'):
        return time.item()  # numpy.datetime64

    t = str(time)

    if t.endswith('.'):
        t = t[:-1]  # Remove the dot if present at the end

    return datetime.fromisoformat(t)


STD_DURATION = re.compile(
    r'^'
    r'(?:(?P<day>-?\d+) (days?,? )?)?'
    r'((?:(?P<hr>-?\d+):)(?=\d+:\d+))?'
    r'(?:(?P<min>-?\d+):)?'
    r'(?P<sec>-?\d+(?:\.\d+)?)'
    r'$'
)
UNITS_DURATION = re.compile(
    r'^'
    r'(?:(?P<day>[+-]?\d+(?:\.\d+)?)\s*(?:d|D|days?))?\s*'
    r'(?:(?P<hr>[+-]?\d+(?:\.\d+)?)\s*(?:h|hrs?|hours?))?\s*'
    r'(?:(?P<min>[+-]?\d+(?:\.\d+)?)\s*(?:m|mins?|minutes?))?\s*'
    r'(?:(?P<sec>[+-]?\d+(?:\.\d+)?)\s*(?:s|secs?|seconds?))?\s*'
    r'(?:(?P<ms>[+-]?\d+(?:\.\d+)?)\s*(?:ms|msecs?|milliseconds?))?'
    r'$'
)
MICRO_SEC = {
    'ms': 1e-3, 'sec': 1, 'min': 60, 'hr': 3_600, 'day': 86_400,
}


def td(delta) -> timedelta:
    """Time delta parser.

    Example: ``7 day, 12:34:56.789`` for
    7 days, 12 hours, 34 minutes, 56 secondes and 789 milliseconds.

    We recommend to use this formatting but you can provide
    explicit units following the rules below:

    Valid units:

    - ``ms``, ``msec``, ``millisecond``
    - ``s``, ``sec``, ``second``
    - ``m``, ``min``, ``minute``
    - ``h``, ``hr``, ``hour``
    - ``d``, ``D``, ``day``

    Plural units are also valid.

    Space between the value and the units is accepted.

    Month(s) and year(s) are not accepted.

    If a ``int`` or a ``float`` is provide, it is assume
    that the value is express in secondes.

    Raises
    ------
    ValueError
        If the provided value format is invalid.

    """
    if isinstance(delta, timedelta):
        return delta

    s = str(delta)

    match = STD_DURATION.match(s) or UNITS_DURATION.match(s)

    if not match:
        raise ValueError(f'Invalid format: `{delta}`')

    us = 1e6 * sum(
        float(value) * MICRO_SEC[unit]
        for unit, value in match.groupdict(default=0).items()
    )

    return timedelta(microseconds=us)
