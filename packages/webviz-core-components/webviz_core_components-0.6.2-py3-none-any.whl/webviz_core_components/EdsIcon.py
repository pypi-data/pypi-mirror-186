# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class EdsIcon(Component):
    """An EdsIcon component.


Keyword arguments:

- id (string; optional)

- color (string; optional)

- icon (string; required)

- size (a value equal to: 16, 24, 32, 40, 48; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, icon=Component.REQUIRED, size=Component.UNDEFINED, color=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'color', 'icon', 'size']
        self._type = 'EdsIcon'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'color', 'icon', 'size']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['icon']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(EdsIcon, self).__init__(**args)
