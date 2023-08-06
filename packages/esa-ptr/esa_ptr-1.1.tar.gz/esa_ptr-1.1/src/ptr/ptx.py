"""Planning timeline parser."""

from html.parser import HTMLParser
from pathlib import Path

from .block import ElementBlock, ObsBlock
from .datetime import EndTime, StartTime
from .element import Element
from .metadata import Comment, File, Metadata
from .prm import PointingRequestMessage
from .timeline import Timeline


ELEMENTS = {
    'startTime': StartTime,
    'endTime': EndTime,
    'comment': Comment,
    'metadata': Metadata,
    'timeline': Timeline,
}


def el_parser(element):
    """Read element and convert it if necessary.

    Warning
    -------
    Only the top level element is parsed, not its children.

    """
    if isinstance(element, Element):
        if element.tag in ELEMENTS:
            return ELEMENTS[element.tag](
                *element,
                description=element.description,
                **element.attrs,
            )

        if element.tag == 'include':
            return File(element.attrs['href'], description=element.description)

        if element.tag == 'block':
            return block_parser(element)

        if element.tag == 'prm':
            return prm_parser(element)

    return element


def _extract(element, key):
    """Extract a key from a element if when is not present."""
    try:
        return list(element.pop(key))
    except KeyError:
        return None


def block_parser(element):
    """Parse block element.

    Parameters
    ----------
    element: ptr.Element
        PTR block element.

    Returns
    -------
    ElementBlock, ObsBlock or None
        Parsed block element.

    Raises
    ------
    AttributeError
        If the block does not have a defined `href` attribute.

    Note
    ----
    SLEW blocks are discarded (appended automatically in Timeline).

    """
    ref = element.attrs.get('ref', '').upper()

    if not ref:
        raise AttributeError(f'Block without `ref` attribute:\n{element}')

    # Remove `ref` from element attributes
    del element.attrs['ref']

    # Skip slew block
    if ref == 'SLEW':
        return None

    # Check start time
    if 'startTime' not in element:
        raise KeyError(f'Block without `startTime` element:\n{element}')

    # Remove only the 1st direct child
    start = element.pop(element.index('startTime'))

    # Check end time
    if 'endTime' not in element:
        raise KeyError(f'Block without `endTime` element:\n{element}')

    # Remove only the 1st direct child
    end = element.pop(element.index('endTime'))

    # Extract if metadata if present
    metadata = _extract(element, 'metadata')

    if ref == 'OBS':
        return ObsBlock(
            start, end, *element,
            metadata=metadata,
            description=element.description,
            **element.attrs,
        )

    return ElementBlock(
        ref, start, end, *element,
        metadata=metadata,
        description=element.description,
        **element.attrs,
    )


def prm_parser(element):
    """Parse pointing request message element.

    Parameters
    ----------
    element: ptr.Element
        PTR pointing request message element.

    Returns
    -------
    PointingRequestMessage
        Parsed pointing request message element.

    """
    header = _extract(element, 'header')

    # Check is the segment is present
    if 'segment' not in element:
        raise KeyError(f'Pointing request message without `segment` element:\n{element}')

    segment = element.pop('segment')

    # Check is the timeline is present
    if 'timeline' not in segment:
        raise KeyError(f'Pointing request message without `timeline` segment:\n{segment}')

    timeline = segment.pop('timeline')

    seg_name = segment.attrs.get('name')
    seg_metadata = _extract(segment, 'metadata')

    return PointingRequestMessage(
        *timeline,
        header=header,
        description=element.description,
        seg_name=seg_name,
        seg_metadata=seg_metadata,
        **element.attrs,
    )


class PtxParser(HTMLParser):
    """PTX content parser."""

    def __init__(self):
        super().__init__()

        self.data = None
        self.elements = []
        self.desc = []

    @property
    def tag(self):
        """Get case-sensitive tag name."""
        tag = self.get_starttag_text()

        for c in '</>':
            tag = tag.replace(c, '')

        return tag.split()[0]

    def handle_starttag(self, _, attrs):
        """Handle tag opening."""
        el = Element(self.tag, **dict(attrs))

        if self.desc:
            el.description = self.desc
            self.desc = []

        self.elements.append(el)

    def handle_endtag(self, tag):
        """Handle tag closure."""
        last_tag = self.elements[-1].tag.lower()

        if tag != last_tag:
            raise KeyError(f'Closing </{tag}> tag before </{last_tag}>.')

        # Get the last element of the list and convert it if necessary
        el = el_parser(self.elements.pop())

        if el is not None:
            if self.elements:
                self.elements[-1].append(el)
            else:
                self.data = el

    def handle_startendtag(self, tag, attrs):
        """Handle empty tag."""
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data):
        """Handle data in tags."""
        if value := data.strip():
            self.elements[-1].append(value)

    def handle_comment(self, data):
        """Handle comment string."""
        if desc := data.strip():
            self.desc.append(desc)

    def error(self, message):
        """Parser error."""
        raise NotImplementedError


def read_ptx(ptx):
    """PTX file reader.

    Parameters
    ----------
    ptx: str or pathlib.Path
        PTX file content text or file name.

    Returns
    -------
    PointingRequestMessage
        Parsed pointing request content.

    """
    content = str(ptx).strip()

    if not content.startswith('<'):
        content = Path(ptx).read_text(encoding='utf-8').strip()

    parser = PtxParser()
    parser.feed(content)

    return parser.data


# Alias `read_ptx` in `read_ptr`
read_ptr = read_ptx
