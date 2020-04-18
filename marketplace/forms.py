from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, help_text=None)
    password = forms.CharField(max_length=100, required=True, help_text=None)
    first_name = forms.CharField(max_length=30, required=False, help_text=None)
    last_name = forms.CharField(max_length=30, required=False, help_text=None)
    email = forms.EmailField(max_length=254, help_text=None)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'hori'}),
            'last_name': forms.TextInput(attrs={'class': 'hori'}),
            'username': forms.TextInput(attrs={'class': 'allign'}),
            'password': forms.TextInput(attrs={'class': 'allign'}),
            'email': forms.TextInput(attrs={'class': 'allign'}),
        }



