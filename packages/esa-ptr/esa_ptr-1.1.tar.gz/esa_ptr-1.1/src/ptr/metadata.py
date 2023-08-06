"""PTR metadata module."""

from pathlib import Path

from .element import Element


class Comment(Element):
    """PTR metadata comment element.

    Parameters
    ----------
    text: str
        Comment message.
    description: str or list, optional
        Comment description, put as a xml-comment on top of the element.

    """

    def __init__(self, text, description=None):
        super().__init__('comment', str(text), description=description)


class File(Element):
    """PTR include file comment element.

    Parameters
    ----------
    fname: str
        Filename to include message.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.

    """

    def __init__(self, text, description=None):
        super().__init__('include', href=str(text), description=description)


class Metadata(Element):
    """PTR metadata element.

    Parameters
    ----------
    *comments: str, list, tuple or ptr.Element
        Metadata comments.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.

    Note
    ----
    If the comment provided is a pathlib.Path it
    will be converted as a `File` element.

    If the comment provided is not an `Element` object
    it will be formatted as an `Comment` element.

    """

    def __init__(self, *comments, description=None):
        super().__init__('metadata', *comments, description=description)

    def append(self, element):
        """Append new metadata."""
        if isinstance(element, (list, tuple)):
            for el in element:
                self.append(el)
            return self

        if isinstance(element, Path):
            element = File(element)

        elif element and not isinstance(element, (Element, dict)):
            element = Comment(element)

        return super().append(element)


class WithMetadata:
    """Add Metadata properties to Element objects."""

    def insert(self, index, element):
        """Insert element before a given index."""
        raise NotImplementedError

    def add_metadata(self, *comments):
        """Append comment(s) to the element."""
        try:
            meta = self['metadata']
        except KeyError:
            meta = Metadata()
            self.insert(0, meta)

        meta.append(comments)


class ElementMetadata(Element, WithMetadata):
    """Element with metadata properties."""

    def __init__(self, tag, *elements, metadata=None, description=None, **attrs):
        super().__init__(tag, description=description, **attrs)
        if metadata:
            self.add_metadata(metadata)

        for element in elements:
            self.append(element)
