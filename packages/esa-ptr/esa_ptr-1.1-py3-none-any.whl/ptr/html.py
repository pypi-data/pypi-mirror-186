"""HTML helpers."""

import uuid


COLLAPSIBLE_STYLE = '''
ul.collapsible {
  list-style: none;
  margin: 0;
  padding-left: 0 !important;
}
ul.collapsible li input + label {
  display: inline-block;
  width: 140px;
  color: #777;
  font-weight: 500;
  padding: 4px 0 2px 0;
}
ul.collapsible li input:enabled + label {
  cursor: pointer;
}
ul.collapsible li input[type="checkbox"] {
  display: none;
}
ul.collapsible li input + label:before {
  content: '► ';
  font-size: 11px;
  color: #777;
  width: 20px;
}
ul.collapsible li input:checked + label:before {
  content: '▼ ';
}
ul.collapsible li input ~ div {
  display: none;
}
ul.collapsible li input:checked ~ div {
  display: block;
}
ul.collapsible ul.collapsible {
  list-style: none;
  margin-left: 1em;
}
'''


class HTMLCollapsible:
    """HTML collapsible element.

    Parameters
    ----------
    *elements: tuple
        Elements to put in the collapsible list.
        They must be formatted as:

        ``('header-1', data_1), ('header-2', data_2, 'expand'), …``

        The keyword `'expand'`` is optional, if provided
        the list will be expanded.

    Note
    ----
    If the provided data element has a `_repr_html_()` representation,
    if will be forwarded in the list representation.

    """

    def __init__(self, *elements):
        self.html = f'<style>{COLLAPSIBLE_STYLE}</style>\n'

        self.html += '<ul class="collapsible">\n'
        for header, data, *expand in elements:
            _id = uuid.uuid4()

            if expand and 'expand' in str(expand).lower():
                checked = 'checked'
            else:
                checked = 'unchecked'

            # Get HTML representation
            if hasattr(data, '_repr_html_'):
                content = html(data)

            elif isinstance(data, list):
                content = '<ul>\n<li>'
                content += '</li>\n<li>'.join([f'{d}' for d in data])
                content += '</li>\n</ul>'

            elif isinstance(data, dict):
                content = '<ul>\n<li>'
                content += '</li>\n<li>'.join([
                    f'<b>{key}</b> {value}' for key, value in data.items()
                ])
                content += '</li>\n</ul>'

            else:
                content = f'{data}'

            self.html += (
                '<li>\n'
                f'    <input id="{_id}" type="checkbox" {checked}>\n'
                f'    <label for="{_id}">{header}</label>\n'
                f'    <div>{content}</div>\n'
                '</li>\n'
            )

        self.html += '</ul>'

    def __str__(self):
        return self.html

    def __repr__(self):
        return str(self)

    def _repr_html_(self):
        return str(self)


def html(obj):
    """Return object _repr_html_() representation."""
    if repr_html := getattr(obj, '_repr_html_', False):
        return repr_html()

    raise NotImplementedError(f'`{obj.__class__.__name__}` has no HTML representation.')
