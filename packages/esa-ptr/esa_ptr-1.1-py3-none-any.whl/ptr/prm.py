"""Pointing Request Message module."""

from .agm import AGMResults, agm_simulation
from .element import XML, Element
from .metadata import Comment, ElementMetadata
from .timeline import Timeline


class PointingRequestMessage(Timeline):
    """Pointing Request Message element.

    Parameters
    ----------
    *blocks: ObsBlock, optional
        Block element(s).
    header: str, ptr.Element or list, optional
        Header comments.
    description: str or list, optional
        Message top comment description.
    seg_name: str, optional
        Segment name attribute.
    seg_metadata: str or list, optional
        Segment metadata comments.
    frame: str, optional
        Timeline reference frame (default: 'SC').
    **attrs:
        Timeline attributes keywords.

    Warning
    -------
    Only 1 segment is accepted for PTR.
    Support for PTS is out of scope for now.

    """

    def __init__(self, *blocks, header=None, description=None,
                 seg_name=None, seg_metadata=None, frame='SC', **attrs):
        super().__init__(*blocks, frame=frame, description=description, **attrs)

        self.header = Element('header')
        self.add_header(header)

        self.seg_name = seg_name
        self.seg_metadata = seg_metadata

    def add_header(self, element):
        """Append elements to the header."""
        if isinstance(element, (Element, dict)):
            self.header.append(element)

        elif isinstance(element, (list, tuple)):
            for el in element:
                self.add_header(el)

        elif element:
            # Add single value into a Comment element
            self.header.append(Comment(element))

    @property
    def xml(self):
        """PRM XML representation."""
        prm = XML.createElement('prm')

        # Add header only if present
        if self.header:
            prm.appendChild(self.header.xml)

        # Wrap prm > body > segment > data > timeline
        body = Element('body').xml
        seg = ElementMetadata('segment',
                              name=self.seg_name, metadata=self.seg_metadata).xml
        data = Element('data').xml
        timeline = super().xml

        data.appendChild(timeline)
        seg.appendChild(data)
        body.appendChild(seg)
        prm.appendChild(body)

        return prm

    def simulate(self, metakernel, agm_endpoint, cache=True) -> AGMResults:
        """Simulate Pointing Request with the Attitude Generator Module.

        Parameters
        ----------
        metakernel: str
            Baseline metakernel for AGM input
        agm_endpoint: str
            AGM endpoint.
        cache: bool, optional
            Use cache the response if present locally.

        Returns
        -------
        AGMResults
            AGM simulation results. If the simulation succeeded, the resulting CK
            can be loading into spiceypy.

        """
        return agm_simulation(metakernel, str(self), agm_endpoint, cache=cache)
