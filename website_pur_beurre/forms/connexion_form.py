from django import forms
from django.utils.safestring import mark_safe


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Username",
                               max_length=30,
                               required=False,
                               )

    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=False)

class UserForm(forms.Form):
	user_name = forms.CharField(label=mark_safe('Username '), max_length=100, required=False)
	first_name = forms.CharField(label=mark_safe('Username '), max_length=100, required=False)
	last_name = forms.CharField(label=mark_safe('Username '), max_length=100, required=False)
	mail = forms.CharField(label=mark_safe('Email '), max_length=100, required=False)
	password = forms.CharField(label=mark_safe('Password '), max_length=100, required=False, widget=forms.PasswordInput)
	password_again = forms.CharField(label=mark_safe('Retyping your password '), max_length=100, required=False,
                               widget=forms.PasswordInput)