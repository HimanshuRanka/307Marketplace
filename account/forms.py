from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_mcgill_email(value):
    if not value.endswith('mcgill.ca'):
        raise ValidationError(
            'Email not from mcgill domain',
            code = 'not_mcgill'
        )


class RegisterForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'Gotta make a username!'}
    )

    email = forms.EmailField(
        validators=[validate_mcgill_email],
        error_messages={'not_mcgill': 'mcgill members only'})

    password = forms.CharField(max_length=30)
    password_confirm = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        # Validation involving multiple fields
        if 'password' in cleaned_data and 'password_confirm' in cleaned_data and cleaned_data['password'] != \
                cleaned_data['password_confirm']:
            self.add_error('password_confirm', 'Passwords do not match')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()



