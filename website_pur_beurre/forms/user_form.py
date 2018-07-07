from django import forms
from django.utils.safestring import mark_safe


class UserForm(forms.Form):
    user_name = forms.CharField(label=mark_safe('<br />Nom d\'utilisateur '), max_length=100, required=False)
    mail = forms.CharField(label=mark_safe('<br />Adresse mail '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('<br />Mot de passe '), max_length=100, required=False, widget=forms.PasswordInput)