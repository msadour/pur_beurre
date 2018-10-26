from django import forms
from django.utils.safestring import mark_safe


class UserForm(forms.Form):
    user_name = forms.CharField(label=mark_safe('Username '), max_length=100, required=False)
    mail = forms.CharField(label=mark_safe('Email '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('Password '), max_length=100, required=False, widget=forms.PasswordInput)
    password_again = forms.CharField(label=mark_safe('Retyping your password '), max_length=100, required=False,
                               widget=forms.PasswordInput)


class UserUpdateForm(forms.Form):
    user_name = forms.CharField(label=mark_safe('New username '), max_length=100, required=False)
    mail = forms.CharField(label=mark_safe('New email '), max_length=100, required=False)
    password = forms.CharField(label=mark_safe('New password '), max_length=100, required=False, widget=forms.PasswordInput)
    password_again = forms.CharField(label=mark_safe('Retyping your new password '), max_length=100, required=False,
                               widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['placeholder'] = user.username
        self.fields['mail'].widget.attrs['placeholder'] = user.email