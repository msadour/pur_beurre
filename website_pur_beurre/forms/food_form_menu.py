from django import forms


class FoodForm(forms.Form):
    food = forms.CharField(label='',
                           max_length=100,
                           required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Search',
                                                         'style': 'width:50%;line-height: 2em;border-radius: 5px',
                                                         'class': 'input_form_search_food',
                                                         })
                           )