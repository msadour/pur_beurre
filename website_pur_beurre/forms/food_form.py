from django import forms


class ProductForm(forms.Form):
    product = forms.CharField(label='Votre produit', max_length=100, required=False)