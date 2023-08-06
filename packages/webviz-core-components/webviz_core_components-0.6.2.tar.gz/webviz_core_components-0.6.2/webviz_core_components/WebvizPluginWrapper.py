# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class WebvizPluginWrapper(Component):
    """A WebvizPluginWrapper component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- id (string; required)

- contactPerson (optional)

- deprecationWarnings (list; optional)

- feedbackUrl (string; optional)

- initiallyActiveViewId (string; required)

- name (string; required)

- persisted_props (list of a value equal to: "children"s; optional):
    Properties whose user interactions will persist after refreshing
    the component or the page.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when the component - or the page - is refreshed. If `persisted` is
    truthy and hasn't changed from its previous value, a `value` that
    the user has changed while using the app will keep that change, as
    long as the new `value` also matches what was given originally.
    Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: "local", "session", "memory"; optional):
    Where persisted user changes will be stored: memory: only kept in
    memory, reset on page refresh. local: window.localStorage, data is
    kept after the browser quit. session: window.sessionStorage, data
    is cleared once the browser quit.

- screenshotFilename (string; optional)

- stretch (boolean; optional)

- tourSteps (list; optional)

- views (list; required)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, name=Component.REQUIRED, views=Component.REQUIRED, initiallyActiveViewId=Component.REQUIRED, screenshotFilename=Component.UNDEFINED, contactPerson=Component.UNDEFINED, deprecationWarnings=Component.UNDEFINED, stretch=Component.UNDEFINED, feedbackUrl=Component.UNDEFINED, tourSteps=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'contactPerson', 'deprecationWarnings', 'feedbackUrl', 'initiallyActiveViewId', 'name', 'persisted_props', 'persistence', 'persistence_type', 'screenshotFilename', 'stretch', 'tourSteps', 'views']
        self._type = 'WebvizPluginWrapper'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'contactPerson', 'deprecationWarnings', 'feedbackUrl', 'initiallyActiveViewId', 'name', 'persisted_props', 'persistence', 'persistence_type', 'screenshotFilename', 'stretch', 'tourSteps', 'views']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['id', 'initiallyActiveViewId', 'name', 'views']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(WebvizPluginWrapper, self).__init__(children=children, **args)
