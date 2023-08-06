"""Generic PTR snippets."""

from .element import Element


class Lon(Element):
    """PTR east longitude element.

    Parameters
    ----------
    lon: float
        East longitude value.
    units: str, optional
        Value units (default: 'deg').
    description: str or list, optional
        Longitude description, put as a xml-comment on top of the element.

    """
    def __init__(self, lon_e, units='deg', description=None):
        super().__init__('lon', float(lon_e), units=units, description=description)


class Lat(Element):
    """PTR latitude element.

    Parameters
    ----------
    lon: float
        Latitude value.
    units: str, optional
        Value units (default: 'deg').
    description: str or list, optional
        Latitude description, put as a xml-comment on top of the element.

    """
    def __init__(self, lat, units='deg', description=None):
        super().__init__('lat', float(lat), units=units, description=description)


class Target(Element):
    """PTR target element.

    Parameters
    ----------
    lon_e: float
        Target east longitude coordinate.
    lat: float
        Target latitude coordinate.
    frame: str, optional
        Target reference frame (default 'EME2000').
    units: str, optional
        Value coordinates units (default: 'deg').
    description: str or list, optional
        Target description, put as a xml-comment on top of the element.
    **attrs: optional
        Targets attributes.

    """
    def __init__(self, lon_e, lat, frame='EME2000', units='deg', **attrs):
        super().__init__(
            'target',
            Lon(lon_e, units=units),
            Lat(lat, units=units),
            frame=frame,
            **attrs
        )


class SolarArrays(Element):
    """PTR metadata solar array element.

    Parameters
    ----------
    fixed_rotation_angle: float, optional
        Solar array fixed rotation angle (in degrees).
    description: str or list, optional
        Solar array description, put as a xml-comment on top of the element.

    """

    def __init__(self, fixed_rotation_angle=None, description=None, **attrs):
        super().__init__('solarArrays', description=description, **attrs)

        if fixed_rotation_angle is not None:
            self.append(
                Element('fixedRotationAngle', fixed_rotation_angle, units='deg')
            )
