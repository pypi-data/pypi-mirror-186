# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Backdrop(Component):
    """A Backdrop component.


Keyword arguments:

- opacity (number; required)"""
    @_explicitize_args
    def __init__(self, opacity=Component.REQUIRED, **kwargs):
        self._prop_names = ['opacity']
        self._type = 'Backdrop'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['opacity']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['opacity']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Backdrop, self).__init__(**args)
