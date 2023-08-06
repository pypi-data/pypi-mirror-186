"""PTR datetime window module."""

from functools import wraps

from .parser import dt
from .time import EndTime, StartTime
from ..element import Element


def is_window(func):
    """Check if the other is derived from a datetime window."""
    @wraps(func)
    def wrap(self, other):
        """Wrapped function."""
        if not isinstance(other, WithDatetimeWindow):
            raise TypeError(f'{self.__class__.__name__} can not be compared to '
                            f'{other.__class__.__name__}.')
        return func(self, other)
    return wrap


class WithDatetimeWindow:
    """Add Time window properties to Element objects."""
    def __init__(self):
        self._start, self._end = None, None  # pragma: no cover

    @is_window
    def __and__(self, other) -> bool:
        """Check intersection with an other datetime window.

        ----------|◁◁◁ self  ▷▷▷|----------
        ----░░░---|--- other ---|---░░░----
        -------░░░|-------------|░░░-------
        -------███|███-------███|███-------
        ----------|███-------███|----------
        ----------|█████████████|███-------
        -------███|█████████████|----------
        ----------|---███████---|----------
        ----------|█████████████|----------
        -------███|█████████████|███-------

        self & other == True: █ / False: ░

        """
        return self.start < other.end and self.end > other.start

    @is_window
    def __lt__(self, other) -> bool:
        """Exclusive lower datetime window comparison.

        Self starts before and is shorter than other:

        ----------|◁◁◁ self  ▷▷▷|----------
        ----░░░---|--- other ---|---███----
        -------░░░|-------------|███-------
        -------░░░|░░░-------███|███-------
        ----------|░░░-------███|----------
        ----------|█████████████|███-------
        -------░░░|░░░░░░░░░░░░░|----------
        ----------|---███████---|----------
        ----------|░░░░░░░░░░░░░|----------
        -------░░░|░░░░░░░░░░░░░|░░░-------

        self < other == True: █ / False: ░

        """
        return self.start < other.start or \
            (self.start == other.start and self.end < other.end)

    @property
    def start(self) -> StartTime:
        """Time window start time value."""
        return self._start

    @property
    def end(self) -> EndTime:
        """Time window end time value."""
        return self._end

    @property
    def window(self):
        """Time window start and end time values."""
        return self.start, self.end

    def set_window(self, start, end):
        """Set time window boundaries."""
        if hasattr(self, '_start') or hasattr(self, '_end'):
            raise AttributeError('Use `.edit()` method instead.')

        start_time = StartTime(start)
        end_time = EndTime(end)

        if start_time >= end_time:
            raise ValueError('Start time shall be before end time.')

        self._start, self._end = start_time, end_time

        self.append(self._start)
        self.append(self._end)

    @property
    def duration(self):
        """Block duration."""
        return self.end - self.start

    def append(self, element):
        """Append a new element or text/numeric value."""
        raise NotImplementedError

    def edit(self, *, start=None, end=None):
        """Edit temporal window boundaries.

        Parameters
        ----------
        start: str, datetime.datetime or datetime.timedelta
            Start time absolute or relative offset.

        end: str, datetime.datetime or datetime.timedelta
            End time absolute or relative offset.

        Raises
        ------
        ValueError
            If the new start time is after the end time.
        ValueError
            If the new end time is before the start time.

        Warning
        -------
        This operation change the duration of the temporal window.

        """
        if start is None:
            start_dt = self.start.datetime
        else:
            try:
                start_dt = self.start + start  # Relative offset (timedelta)
            except ValueError:
                start_dt = dt(start)           # Absolute offset (datetime)

        if end is None:
            end_dt = self.end.datetime
        else:
            try:
                end_dt = self.end + end  # Relative offset (timedelta)
            except ValueError:
                end_dt = dt(end)         # Absolute offset (datetime)

        # Check that the new window boundaries are still valid
        if end_dt <= start_dt:
            raise ValueError(
                f'Start time `{start_dt.isoformat()}` must be before '
                f'end time: `{end_dt.isoformat()}`.')

        # Edit window only if required
        if start:
            self.start.edit(start_dt)

        if end:
            self.end.edit(end_dt)

        return self

    def offset(self, offset, *, ref='start'):
        """Offset the temporal window globally.

        Parameters
        ----------
        offset: str datetime.timedelta or datetime.datetime
            Global or relative offset.

        ref: str, optional
            Boundary reference for relative offset.
            Only ``start|end|center`` are accepted

        Raise
        -----
        KeyError
            If the reference keyword is invalid.

        Note
        ----
        This operation does not change the duration of the window.

        """
        try:
            # Global offset (with timedelta)
            self.start.offset(offset)
            self.end.offset(offset)

        except ValueError:
            # Relative offset (with datetime)
            t, d = dt(offset), self.duration

            if ref == 'start':
                self.start.edit(t)
                self.end.edit(t + d)

            elif ref == 'end':
                self.start.edit(t - d)
                self.end.edit(t)

            elif ref == 'center':
                self.start.edit(t - d / 2)
                self.end.edit(t + d / 2)

            else:
                raise KeyError('For relative offset, the ref keyword must be '
                               'in `start|end|center`.') from None
        return self


class ElementWindow(Element, WithDatetimeWindow):
    """Element with datetime window properties."""

    def __init__(self, tag, start, end, *elements, **attrs):
        super().__init__(tag, **attrs)
        self.set_window(start, end)

        for element in elements:
            self.append(element)
