""""""
# Standard library imports

# Third party imports
import ipyvuetify as v

# Local imports

class DataPickerWithDialog(v.Col):
    """
    DataPickerWithDialog(cols="auto", align_self="center")
    """

    def __init__(self, **kwargs):
        """"""
        super().__init__(**kwargs)

        self._date_picker = v.DatePicker(
            type="month",
        )
        self._dialog = v.Dialog(
            v_model=False,
            children=[self._date_picker],
            width="320px",
            transition="dialog-bottom-transition"
        )
        self._text_field = v.TextField(
            value="20110101",
            prepend_icon="mdi-calendar",
            clearable=True,
            outlined=True,
            placeholder="YYYYMMDD",
            label="Start date"
        )
        self._text_field.on_event("click:prepend", self.calendar_button_clicked)
        self._date_picker.on_event("input", self.date_chosen)
        self.children = [self._dialog, self._text_field]

    def calendar_button_clicked(self, *args):
        """"""
        self._dialog.v_model = not self._dialog.v_model

    def date_chosen(self, widget, event, data):
        """"""
        self._dialog.v_model = False
        self._text_field.value = data.replace("-", "") + "01"
