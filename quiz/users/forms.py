from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email=forms.EmailField(
        max_length=100,
        required = True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )

    usn = forms.IntegerField(
        required=True,
        help_text='Enter usn',
         widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'usn'}),
    )


    password = forms.CharField(
        help_text='Enter Password',
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        )
    class Meta:
        model = get_user_model()
        fields = ('email', 'usn', 'password')