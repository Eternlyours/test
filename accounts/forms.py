from django import forms


class AccountsForm(forms.Form):
    name = forms.CharField(label='name', max_length=50)


class TransactionsForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    account_id = forms.IntegerField(min_value=1)
