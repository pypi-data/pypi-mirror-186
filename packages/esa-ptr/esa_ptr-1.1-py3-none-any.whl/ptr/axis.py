"""PTR axis module."""

from .element import Element


AXIS = {
    'X': [1, 0, 0],
    'Y': [0, 1, 0],
    'Z': [0, 0, 1],
}


def invert(vec):
    """Invert vector values."""
    return [-1 * v for v in vec]


def parse_vector(*axis):
    """Parse axis vector.

    Parameters
    ----------
    *axis: tuple or str
        Axis vector tuple or name (eg. ``(1, 0, 0)`` or '-Y').

    Returns
    -------
    list
        X, Y, Z vector components.

    """
    if len(axis) == 1 and isinstance(axis[0], str):
        name = axis[0]
        vec = name.upper()[-1]

        if vec not in ['X', 'Y', 'Z']:
            raise ValueError('Only (+/-) X, Y, Z are considered as valid.')

        vec = AXIS[vec]

        if name.startswith('-'):
            vec = invert(vec)

    elif len(axis) == 3:
        vec = list(axis)

    else:
        raise ValueError('This axis vector must have 3 components (x, y, z).')

    return vec


class ElementAxis(Element):
    """PTR axis element.

    Parameters
    ----------
    frame: str
        Element reference frame.
    *axis: tuple or str
        Axis vector tuple or axis name (eg. '-Y').
    description: str or list, optional
        Axis description, put as a xml-comment on top of the element.

    """

    def __init__(self, frame, *axis, description=None):
        self.vec = parse_vector(*axis)

        super().__init__(
            f'{frame}Axis',
            {'x': self.x, 'y': self.y, 'z': self.z},
            frame=frame,
            description=description,
        )

    @property
    def frame(self):
        """Axis frame attribute."""
        return self.attrs['frame']

    def __neg__(self):
        return ElementAxis(self.frame, *invert(self.vec))

    def __pos__(self):
        return ElementAxis(self.frame, *self.vec)

    @property
    def x(self):
        """X-axis value."""
        return self.vec[0]

    @property
    def y(self):
        """Y-axis value."""
        return self.vec[1]

    @property
    def z(self):
        """Z-axis value."""
        return self.vec[2]


class ScAxis(ElementAxis):
    """PTR spacecraft axis element.

    Parameters
    ----------
    *xyz: tuple or str
        Spacecraft vector tuple or axis name (eg. ``(1, 0, 0)`` or '-Y').
    description: str or list, optional
        Axis description, put as a xml-comment on top of the element.

    """

    def __init__(self, *axis, description=None):
        super().__init__('SC', *axis, description=description)


# Spacecraft axis shortcuts
xScAxis = ScAxis('X')
yScAxis = ScAxis('Y')
zScAxis = ScAxis('Z')
