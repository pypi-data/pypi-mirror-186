# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DrawCanvas(Component):
    """A DrawCanvas component.


Keyword arguments:

- refresh (boolean; default False)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'bubble_train'
    _type = 'DrawCanvas'
    @_explicitize_args
    def __init__(self, refresh=Component.UNDEFINED, **kwargs):
        self._prop_names = ['refresh']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['refresh']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DrawCanvas, self).__init__(**args)
