# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WebvizDialog(Component):
    """A WebvizDialog component.


Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; required)

- actions (list of strings; optional)

- disableDraggable (boolean; default False)

- disableEscapeKeyDown (boolean; default False)

- height (number | string; default undefined)

- heightOwner (a value equal to: "dialog", "content"; default undefined)

- maxWidth (number | string; default undefined)

- minWidth (number; default 200)

- modal (boolean; default False)

- open (boolean; default False)

- title (string; required)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, open=Component.UNDEFINED, modal=Component.UNDEFINED, title=Component.REQUIRED, heightOwner=Component.UNDEFINED, height=Component.UNDEFINED, minWidth=Component.UNDEFINED, maxWidth=Component.UNDEFINED, disableDraggable=Component.UNDEFINED, disableEscapeKeyDown=Component.UNDEFINED, actions=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'actions', 'disableDraggable', 'disableEscapeKeyDown', 'height', 'heightOwner', 'maxWidth', 'minWidth', 'modal', 'open', 'title']
        self._type = 'WebvizDialog'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'actions', 'disableDraggable', 'disableEscapeKeyDown', 'height', 'heightOwner', 'maxWidth', 'minWidth', 'modal', 'open', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id', 'title']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WebvizDialog, self).__init__(children=children, **args)
