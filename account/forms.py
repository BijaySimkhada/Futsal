from django import forms
from .models import Account, UserInfo, FutsalInfo
from crispy_forms.helper import FormHelper


class LoginForm(forms.Form):
    helper = FormHelper()
    helper.form_show_errors = True
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    fields = [
        email, password
    ]

class RegisterUser(forms.Form):
    helper = FormHelper()
    helper.form_show_errors = True
    username = forms.CharField(max_length=30)
    email = forms.CharField(max_length=30)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    fields = [
        username, email, password, confirm_password
    ]

    def clean(self):
        cleaned_data = super(RegisterUser, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and Confirm password donot match"
            )


class InfoUser(forms.Form):
    helper = FormHelper()
    helper.form_show_errors = True
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)

    fields = ('first_name', 'last_name', 'phone')


class TimeInput(forms.TimeInput):
    input_type = 'time'


class FutsalForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_errors = True
    class Meta:
        model = FutsalInfo
        widgets = {'open_at': TimeInput(), 'close_at': TimeInput()}
        fields = ('futsal_name', 'phone', 'location', 'open_at', 'close_at', 'price', 'img1', 'img2', 'img3', 'img4')