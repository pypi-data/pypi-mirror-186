# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WebvizSettings(Component):
    """A WebvizSettings component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- visible (boolean; required)

- width (number; required)"""
    @_explicitize_args
    def __init__(self, children=None, visible=Component.REQUIRED, width=Component.REQUIRED, **kwargs):
        self._prop_names = ['children', 'visible', 'width']
        self._type = 'WebvizSettings'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'visible', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['visible', 'width']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WebvizSettings, self).__init__(children=children, **args)
