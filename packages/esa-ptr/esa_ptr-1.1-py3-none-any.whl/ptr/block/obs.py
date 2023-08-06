"""PTR observation blocks module."""

from .block import ElementBlock


class ObsBlock(ElementBlock):
    """PTR observation block.

    Parameters
    ----------
    start: string, datetime.datetime or numpy.datetime64
        Block start time.
    end: string, datetime.datetime or numpy.datetime64
        Block end time.
    *elements:
        Block elements.

    metadata: str, int, float, ptr.Element, tuple or list, optional
        Block metadata comments.
    description: str or list, optional
        Block description, put as a xml-comment on top of the element.
    **attrs:
        Block keywords attributes.

    """

    def __init__(self, start, end, *elements, metadata=None, description=None, **attrs):
        super().__init__(
            'OBS', start, end, *elements,
            metadata=metadata, description=description, **attrs
        )
