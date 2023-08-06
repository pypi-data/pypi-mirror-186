# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Overlay(Component):
    """An Overlay component.
An overlay that can be used to remove focus from the background and set focus on a certain component
(e.g. dialog, notification).

Keyword arguments:

- visible (boolean; required):
    Set if the overlay shall be shown or not.

- zIndex (number; optional):
    Optionally defined a preferred z-index for the overlay."""
    @_explicitize_args
    def __init__(self, visible=Component.REQUIRED, zIndex=Component.UNDEFINED, onClick=Component.REQUIRED, **kwargs):
        self._prop_names = ['visible', 'zIndex']
        self._type = 'Overlay'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['visible', 'zIndex']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['visible']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Overlay, self).__init__(**args)
