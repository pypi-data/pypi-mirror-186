# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WebvizSettingsGroup(Component):
    """A WebvizSettingsGroup component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; required)

- alwaysOpen (boolean; optional)

- notVisibleInViews (list of strings; optional)

- open (boolean; optional)

- pluginId (string; required)

- title (string; required)

- viewId (string; required)

- visibleInViews (list of strings; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, title=Component.REQUIRED, open=Component.UNDEFINED, viewId=Component.REQUIRED, pluginId=Component.REQUIRED, visibleInViews=Component.UNDEFINED, notVisibleInViews=Component.UNDEFINED, alwaysOpen=Component.UNDEFINED, onToggle=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'alwaysOpen', 'notVisibleInViews', 'open', 'pluginId', 'title', 'viewId', 'visibleInViews']
        self._type = 'WebvizSettingsGroup'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'alwaysOpen', 'notVisibleInViews', 'open', 'pluginId', 'title', 'viewId', 'visibleInViews']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id', 'pluginId', 'title', 'viewId']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WebvizSettingsGroup, self).__init__(children=children, **args)
