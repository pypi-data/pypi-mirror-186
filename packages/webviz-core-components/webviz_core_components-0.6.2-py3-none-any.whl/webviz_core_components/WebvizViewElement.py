# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WebvizViewElement(Component):
    """A WebvizViewElement component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; required)

- download (optional)

- flexGrow (number; optional)

- hidden (boolean; optional)

- screenshotFilename (string; optional)

- showDownload (boolean; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, flexGrow=Component.UNDEFINED, hidden=Component.UNDEFINED, showDownload=Component.UNDEFINED, screenshotFilename=Component.UNDEFINED, download=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'download', 'flexGrow', 'hidden', 'screenshotFilename', 'showDownload']
        self._type = 'WebvizViewElement'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'download', 'flexGrow', 'hidden', 'screenshotFilename', 'showDownload']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WebvizViewElement, self).__init__(children=children, **args)
