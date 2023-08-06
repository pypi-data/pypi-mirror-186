"""PTR time module."""

from datetime import datetime

from .parser import dt, td
from ..element import XML, Element


class WithTime:
    """Add Time properties to Element objects."""

    def __add__(self, other):
        return self.datetime + td(other)  # -> datetime

    def __sub__(self, other):
        try:
            return self.datetime - dt(other)  # -> timedelta
        except ValueError:
            return self.datetime - td(other)  # -> datetime

    def __gt__(self, other) -> bool:
        return (self - dt(other)).total_seconds() > 0

    def __lt__(self, other) -> bool:
        return (self - dt(other)).total_seconds() < 0

    def __ge__(self, other) -> bool:
        return (self - dt(other)).total_seconds() >= 0

    def __le__(self, other) -> bool:
        return (self - dt(other)).total_seconds() <= 0

    @property
    def datetime(self) -> datetime:
        """Datetime value."""
        raise NotImplementedError

    def edit(self, value):
        """Edit time value."""
        raise NotImplementedError

    @property
    def date(self):
        """Date value."""
        return self.datetime.date()

    @property
    def time(self):
        """Time value."""
        return self.datetime.time()

    @property
    def iso(self):
        """ISO formatted datetime."""
        return self.datetime.isoformat()

    def item(self) -> datetime:
        """Datetime value (numpy-like)."""
        return self.datetime

    def offset(self, offset):
        """Shift time value."""
        self.edit(self.datetime + td(offset))
        return self


class Time(WithTime):
    """Generic Time object."""
    def __init__(self, time):
        self._dt = dt(time)

    def __str__(self):
        return self.iso

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.iso}')"

    def __eq__(self, other) -> bool:
        return self.datetime == dt(other)

    @property
    def datetime(self) -> datetime:
        """Datetime value."""
        return self._dt

    def edit(self, value):
        """Edit time value."""
        self._dt = dt(value)
        return self


class ElementTime(WithTime, Element):
    """Time element.

    Parameters
    ----------
    tag: str
        Element tag name.
    time: str, datetime.datetime or numpy.datetime64
        Element time.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.

    Note
    ----
    The element is parsed as a native datetime.datetime object,
    and display in XML in ISO format: ``YYYY-MM-DDThh:mm:ss``.

    """
    def __init__(self, tag, time, description=None):
        if not description and isinstance(time, ElementTime):
            description = time.description

        super().__init__(tag, dt(time), description=description)

    @property
    def datetime(self) -> datetime:
        """Datetime value."""
        return self[0]

    def edit(self, value):
        """Edit time value."""
        self._els[0] = dt(value)
        return self

    @property
    def xml(self):
        """XML PTR time object."""
        xml = XML.createElement(self.tag)
        xml.appendChild(XML.createTextNode(f' {self.iso} '))
        return xml


class StartTime(ElementTime):
    """PTR start ElementTime element.

    Parameters
    ----------
    time: str, datetime.datetime or numpy.datetime64
        Element start time.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.

    """
    def __init__(self, time, description=None):
        super().__init__('startTime', time, description=description)


class EndTime(ElementTime):
    """PTR end time element.

    Parameters
    ----------
    time: str, datetime.datetime or numpy.datetime64
        Element end time.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.

    """
    def __init__(self, time, description=None):
        super().__init__('endTime', time, description=description)
