from django import forms


class FoodForm(forms.Form):
    food = forms.CharField(label='Votre produit',
                           max_length=100,
                           required=False,
                           widget=forms.TextInput(attrs={'class': 'input-sm form-control'}))