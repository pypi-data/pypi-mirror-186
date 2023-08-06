# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ScrollArea(Component):
    """A ScrollArea component.


Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- height (number | string; optional)

- noScrollbarPadding (boolean; optional)

- width (number | string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, width=Component.UNDEFINED, height=Component.UNDEFINED, noScrollbarPadding=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'height', 'noScrollbarPadding', 'width']
        self._type = 'ScrollArea'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'height', 'noScrollbarPadding', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ScrollArea, self).__init__(children=children, **args)
