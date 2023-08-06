# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ViewVisibilityContainer(Component):
    """A ViewVisibilityContainer component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional)

- notShowInViews (list of strings; optional)

- showInViews (list of strings; optional)"""
    @_explicitize_args
    def __init__(self, children=None, showInViews=Component.UNDEFINED, notShowInViews=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'notShowInViews', 'showInViews']
        self._type = 'ViewVisibilityContainer'
        self._namespace = 'webviz_core_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'notShowInViews', 'showInViews']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ViewVisibilityContainer, self).__init__(children=children, **args)
