# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DraggablePanel(Component):
    """A DraggablePanel component.


Keyword arguments:

- children (list of a list of or a singular dash component, string or numbers | a list of or a singular dash component, string or number; optional)

- id (string; required)

- height (string; default '100px')

- left (string; default '50px')

- top (string; default '50px')

- width (string; default '100px')"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'bubble_train'
    _type = 'DraggablePanel'
    @_explicitize_args
    def __init__(self, children=None, id=Component.REQUIRED, width=Component.UNDEFINED, height=Component.UNDEFINED, left=Component.UNDEFINED, top=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'height', 'left', 'top', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'height', 'left', 'top', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DraggablePanel, self).__init__(children=children, **args)
