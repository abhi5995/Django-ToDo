from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1','password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'})
        }
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email'
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Password')