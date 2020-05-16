from django import forms
from crispy_forms.helper import FormHelper


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BookingForm(forms.Form):
    helper = FormHelper()
    helper.form_show_errors = True
    book_date = forms.DateField(widget=DateInput)
    book_time = forms.TimeField(widget=TimeInput)

    fields = [
        book_date, book_time,
    ]