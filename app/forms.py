from django import forms

from .models import Client, Transaction, ProductSet


class NewClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('name', 'form')


class NewTransactionForm(forms.ModelForm):

    class Meta:
        model = ProductSet
        fields = ('m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10',
                  'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10')
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }
