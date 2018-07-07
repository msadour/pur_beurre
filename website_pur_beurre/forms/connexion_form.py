from django import forms


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, required=False)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=False)