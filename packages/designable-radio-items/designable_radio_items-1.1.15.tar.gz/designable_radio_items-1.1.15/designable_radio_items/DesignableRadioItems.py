# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DesignableRadioItems(Component):
    """A DesignableRadioItems component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional)

- className (string; optional)

- n_clicks (number; default 0)

- name (string; optional)

- options (list; required)

- readonly (boolean; default False)

- value (string | number; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'designable_radio_items'
    _type = 'DesignableRadioItems'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, options=Component.REQUIRED, value=Component.UNDEFINED, name=Component.UNDEFINED, className=Component.UNDEFINED, readonly=Component.UNDEFINED, n_clicks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'n_clicks', 'name', 'options', 'readonly', 'value']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'n_clicks', 'name', 'options', 'readonly', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['options']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DesignableRadioItems, self).__init__(**args)
