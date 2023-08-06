import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual, Layout


class Fields(object):
    def text(self, description="", placeholder="", width="50%", disabled=True, value=None):
        return widgets.Text(
            description=description,
            placeholder=placeholder,
            layout=Layout(width=width),
            disabled=disabled,
            value=value
        )

    def textarea(self, description="", placeholder="", width="50%", disabled=True, value=None, *args, **kwargs):
        return widgets.Textarea(
            description=description,
            placeholder=placeholder,
            layout=Layout(width=width),
            disabled=disabled,
            value=value,
            *args,
            **kwargs
        )

    def radio(self, description="", options=[], placeholder="", width="50%", disabled=True, value=None, *args,
              **kwargs):
        return widgets.RadioButtons(
            options=options,
            description=description,
            placeholder=placeholder,
            layout=Layout(width=width),
            disabled=disabled,
            value=value,
            *args,
            **kwargs
        )

    def label(self, label, layout="50%"):
        return widgets.Label(label, layout=Layout(width=layout))

    def datetime(self, description, value, disabled=False):
        return widgets.DatePicker(
            description=description,
            disabled=disabled,
            value=value
        )

    def marks(self, description, value):
        return widgets.Valid(
            value=value,
            description=description,
        )

    def checkbox(self, description, value, disabled=True, indent=False):
        return widgets.Checkbox(
            value=value,
            description=description,
            disabled=disabled,
            indent=indent
        )

    def select_multiple(self, description, options, disabled=True, value=None, rows=10):
        return widgets.SelectMultiple(
            options=options,
            value=value,
            rows=rows,
            description=description,
            disabled=disabled
        )

    def button(self, description, icon):
        return widgets.Button(description=description, icon=icon)
