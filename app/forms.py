from django import forms

from .models import \
    PartnerSet, \
    TransactionSet, \
    ProductSet, \
    ProductItem


class NewClientForm(forms.ModelForm):

    class Meta:
        model = PartnerSet
        fields = ('name', 'code')


class NewTransactionForm(forms.ModelForm):

    class Meta:
        model = ProductItem
        # items = ProductItem.objects.all()


        fields = ('code', 'name')
        # fields = ('m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10',
        #           'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9', 'w10')
        # widgets = {
        #     'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        # }


class NewStorageForm(forms.ModelForm):
    name = forms.CharField(initial='Storage name')
    _fields = [name]
    items = ProductItem.objects.all()
    for item in items:
        item_field = forms.CharField(max_length=6, name=item.code, label=item.code)
        _fields.append(item_field)

    fields = tuple(_fields)

