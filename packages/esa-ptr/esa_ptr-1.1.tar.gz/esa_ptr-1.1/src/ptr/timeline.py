"""PTR timeline module."""

from warnings import warn

from .block.slew import SLEW_BLOCK
from .block.utils import gap, insort, is_block
from .datetime import dt, td
from .element import XML, Element


class Timeline(Element):
    """Planning Timeline Request element.

    Parameters
    ----------
    *blocks: ObsBlock, optional
        Block element(s) (default: None).
    frame: str, optional
        Timeline reference frame (default: 'SC').
    description: str or list, optional
        Timeline description, put as a xml-comment on top of the element.
    **attrs:
        Timeline attributes keywords.

    Note
    ----
    The blocks are automatically sorted. Overlaps
    is not allowed and will raise a BlockOverlapError.
    Slew blocks are automatically appended to fill
    the gaps between the blocks. They should not be
    included in the blocks input list (it will return
    a TypeError).

    """

    def __init__(self, *blocks, frame='SC', **attrs):
        super().__init__('timeline', frame=frame, **attrs)

        for block in blocks:
            self.append(block)

    @property
    def start(self):
        """Timeline start time."""
        return self[0].start if self else None

    @property
    def end(self):
        """Timeline end time."""
        return self[-1].end if self else None

    @property
    def duration(self):
        """Timeline duration."""
        return self.end - self.start if self else None

    @property
    def xml(self):
        """Element XML object."""
        xml = XML.createElement(self.tag)

        # Add element attributes
        for key, value in self.attrs.items():
            if value is not None:
                xml.setAttribute(key, str(value))

        latest = False
        for block in self:
            # Add a slew between blocks only when required
            if latest and gap(latest, block):
                xml.appendChild(SLEW_BLOCK.xml)

            # Add child description if present
            for desc in block.xml_desc:
                xml.appendChild(desc)

            xml.appendChild(block.xml)
            latest = block

        return xml

    @is_block
    def append(self, element):
        """Append a new block to the timeline.

        Warning
        -------
        The new block will be added chronologically in
        the list of elements. It must fit between the other
        blocks.

        """
        insort(self._els, element)
        element.link_timeline(self)  # Link this timeline to this block element

        return self

    def insert(self, _, element):
        """Disable index insertion."""
        warn('Insertion is always performed chronologically. '
             'You should use `.append()` instead.',
             SyntaxWarning, stacklevel=2)

        return self.append(element)

    def pop(self, key=-1):
        """Remove block from timeline."""
        block = super().pop(key)
        block.unlink_timeline(self)
        return block

    def sort(self):
        """Sort blocks."""
        self._els.sort()

    def offset(self, offset, *, ref='start'):
        """Offset timeline blocks globally.

        Parameters
        ----------
        offset: str datetime.timedelta or datetime.datetime
            Global or relative offset.

        ref: str, optional
            Boundary reference for relative offset (datetime).
            Only ``start|end|center`` are accepted

        Raise
        -----
        KeyError
            If the reference keyword is invalid.

        Note
        ----
        This operation does not change the duration of the timeline.

        """
        try:
            delta = td(offset)
        except ValueError:
            t = dt(offset)
            if ref == 'start':
                delta = t - self.start.datetime
            elif ref == 'end':
                delta = t - self.end.datetime
            elif ref == 'center':
                delta = t - (self.start + self.duration / 2)
            else:
                raise KeyError('For relative offset, the ref keyword must be '
                               'in `start|end|center`.') from None

        # Move the blocks from the end when delta > 0 to avoid collisions
        for block in self if delta.total_seconds() <= 0 else reversed(self):
            block.offset(delta)

        return self
