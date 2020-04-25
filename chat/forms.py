from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class JoinChatRoom(forms.Form):
    username = forms.CharField(
        error_messages={'required': 'Please specify who you wish to chat with'}
    )
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()



