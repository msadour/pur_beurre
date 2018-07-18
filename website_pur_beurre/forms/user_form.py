from django import forms
from django.utils.safestring import mark_safe


class UserForm(forms.Form):
    user_name = forms.CharField(label=mark_safe('Nom d\'utilisateur '), max_length=100, required=False)
    mail = forms.CharField(label=mark_safe('Adresse mail '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('Mot de passe '), max_length=100, required=False, widget=forms.PasswordInput)
    password_again = forms.CharField(label=mark_safe('Confirmez votre mot de passe '), max_length=100, required=False,
                               widget=forms.PasswordInput)