"""PTR Elements module."""

from functools import wraps
from pathlib import Path
from xml.dom import getDOMImplementation

from .datetime.parser import dt, td


XML = getDOMImplementation().createDocument(None, None, None)


class FrozenElementError(Exception):
    """Frozen element error."""


def frozen_lock(func):
    """Freezing decorator."""
    @wraps(func)
    def wrap(self, *args, **kwargs):
        """Wrapper function."""
        if self.is_frozen():
            raise FrozenElementError(f'<{self.tag}> cannot be changed.')
        return func(self, *args, **kwargs)
    return wrap


class Element:
    """Abstract PTR element object.

    Parameters
    ----------
    tag: str
        Element tag name.
    *elements: any
        Text/numerical values or list of children elements.
    description: str or list, optional
        Element description, put as a xml-comment on top of the element.
    **attrs: str
        Element attributes.

    """
    INDENT = '  '
    LIST_SEP = '  '

    def __init__(self, tag, *elements, description=None, **attrs):
        self.tag = tag
        self.description = description
        self.attrs = attrs

        for element in elements:
            self.append(element)

    def __str__(self):
        s = ''
        for desc in self.xml_desc:
            s += desc.toprettyxml(indent=self.INDENT)

        s += self.xml.toprettyxml(indent=self.INDENT)
        return s.strip()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, other):
        return self.append(other)

    def __len__(self):
        return len(self._els)

    def __iter__(self):
        return iter(self._els)

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._els[key]

        elements = []
        for el in self:
            if isinstance(el, Element):
                if el.tag == key:
                    elements.append(el)
                elif key in el:
                    children = el[key]
                    if isinstance(children, list):
                        elements.extend(children)
                    else:
                        elements.append(children)

        if not elements:
            raise KeyError(key)

        return elements[0] if len(elements) == 1 else elements

    def __setitem__(self, key, value):
        self[key].set_value(value)

    def __contains__(self, key):
        for el in self:
            if isinstance(el, Element) and (el.tag == key or key in el):
                return True
        return False

    def __delitem__(self, key):
        self.pop(key)

    @property
    def tag(self):
        """Element tag name."""
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Element tag name setter."""
        self._tag = tag
        self._els = []
        self._attrs = {}
        self._desc = []

    @property
    def value(self):
        """Element parsed value."""
        if len(self) != 1 or isinstance(self[0], Element):
            raise ValueError('Only single value can be retrieved with `.value`')

        return self._value_parser(self[0])

    def _value_parser(self, value):
        """Value parser."""
        if self.LIST_SEP in str(value):
            return [
                self._value_parser(v.strip())
                for v in str(value).split(self.LIST_SEP)
                if v.strip()
            ]

        if str(value).isdecimal():
            return int(value)

        for func in [float, dt, td]:
            try:
                return func(value)
            except (ValueError, TypeError):
                pass

        return value

    def set_value(self, value):
        """Set element value."""
        if len(self) != 1 or isinstance(self[0], Element):
            raise ValueError('Only single value can be edited.')

        self._els[0] = value

        return self

    def freeze(self, status=True):
        """Freeze the element."""
        setattr(self, 'frozen', status)

    def is_frozen(self):
        """Check if the element is frozen."""
        return getattr(self, 'frozen', False)

    @frozen_lock
    def append(self, element):
        """Append a new element or text/numeric value."""
        if len(self) == 1 and not isinstance(self[0], Element):
            raise ValueError(f'<{self.tag}> already content the value '
                             f'`{self[0]}` impossible to add `{element}`.')

        if isinstance(element, dict):
            for tag, value in element.items():
                self.append(Element(tag, value))
            return self

        if self and not isinstance(element, Element):
            raise ValueError(
                f'<{self.tag}> already content {len(self)} `ptr.Element`, '
                f'impossible to add `{element}`.')

        if element is not None:
            self._els.append(element)

        return self

    @property
    def description(self):
        """Element description."""
        return self._desc

    @description.setter
    def description(self, desc):
        """Element description setter."""
        if not desc:
            self._desc = []
        elif isinstance(desc, (list, tuple)):
            self._desc.extend(d for d in desc)
        else:
            self._desc.append(desc)

    @property
    def xml_desc(self):
        """Element XML formatted description."""
        return (
            XML.createComment(f' {desc.replace("-", "–").strip()} ')
            for desc in self.description
        )

    @property
    def xml(self):
        """Element XML object."""
        xml = XML.createElement(self.tag)

        # Add element attributes
        for key, value in self.attrs.items():
            if value is not None:
                xml.setAttribute(key, str(value))

        for element in self:
            if isinstance(element, Element):
                # Add child description if present
                for desc in element.xml_desc:
                    xml.appendChild(desc)

                child = element.xml
            else:
                child = XML.createTextNode(f' {self._fmt_el(element)} ')

            xml.appendChild(child)

        return xml

    def _fmt_el(self, element) -> str:
        """Format element as XML text string."""
        if not isinstance(element, str) and hasattr(element, '__iter__'):
            return self.LIST_SEP.join([
                self._fmt_el(el)
                for el in element
            ])

        return str(element).strip()

    def index(self, tag) -> int:
        """Locate tag element index in the elements list.

        Parameters
        ----------
        tag: str
            Tag element name to search in the Element.

        Returns
        -------
        int
            Index of the tag element requested.

        Raises
        ------
        ValueError
            If the tag element was not found in the Element.

        Note
        ----
        If multiple tag elements are present only the index
        of the first tag element found is returned.
        Only the top level children are explored.

        """
        for i, el in enumerate(self):
            if el.tag == tag:
                return i

        raise ValueError(f'`{tag}` is not present in {self}')

    @frozen_lock
    def pop(self, key=-1):
        """Pop child element(s) by index or key.

        Parameters
        ----------
        key: int or str
            Element index or Element tag name to remove.
            By default the last element is removed.

        Returns
        -------
        Element or list(Element, ...)
            Popped element(s).

        Raises
        ------
        IndexError
            If the provided index is out of range.
        KeyError
            If not element match the provided key.
        TypeError
            If the key provided is invalid.

        Note
        ----
        When removed by tag name, if multiple child elements match
        the provided key, they will all be removed and returned.

        """
        if isinstance(key, int):
            return self._els.pop(key)

        if isinstance(key, str):
            if key not in self:
                raise KeyError(f'`{key}` is not in `{self.__class__.__name__}`.')

            els, ipop = [], []
            for i, el in enumerate(self._els):
                if isinstance(el, Element):
                    if el.tag == key:
                        els.append(el)  # Store the element to remove
                        ipop.append(i)    # and its index

                    elif key in el:
                        p = el.pop(key)
                        if isinstance(p, list):
                            els.extend(p)
                        else:
                            els.append(p)

            for i in reversed(ipop):
                self._els.pop(i)  # Remove the els elements here

            return els[0] if len(els) == 1 else els

        raise TypeError(
            f'Only `int` and `str` are accepted (`{type(key).__name__}` provided).')

    @frozen_lock
    def insert(self, index, element):
        """Insert element before a given index."""
        self.append(element)         # Check if the element can be append
        el = self.pop()              # Remove the last added element
        self._els.insert(index, el)  # Insert the element at the right position

    def save(self, filename, overwrite=False):
        """Save the element into a file.

        Parameters
        ----------
        filename: str or pathlib.Path
            Output filename.
        overwrite: bool, optional
            Overwrite the file if already exists (default: False).

        Returns
        -------
        pathlib.Path
            Output file location.

        """
        fname = Path(filename)

        if fname.exists() and not overwrite:
            raise FileExistsError(filename)

        fname.write_text(str(self) + '\n', encoding='utf-8')

        return fname
