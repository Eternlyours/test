from accounts.utils import filtering, to_json
from .models import Accounts, Transactions
from django.http import JsonResponse
from django.views.generic import View
from .forms import AccountsForm, TransactionsForm
from django.views.generic import View
from django.shortcuts import redirect


class AccountsAPIView(View):
    model = Accounts

    def post(self, request, *args, **kwargs):
        form = AccountsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            Accounts.objects.create(**cleaned_data)
        return redirect('accounts')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().order_by('id')
        resp = JsonResponse(data=to_json(queryset), status=200, safe=False)
        return resp

    def get_queryset(self):
        return self.model.objects.all()


class TransactionAPIView(View):
    model = Transactions

    def post(self, request, *args, **kwargs):
        form = TransactionsForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            account_id = cleaned_data['account_id']
            amount = cleaned_data['amount']
            instance = Accounts.objects.get(pk=account_id)
            Transactions.objects.create(account_id=instance, amount=amount)
        return redirect('transactions')

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().select_related('account_id').order_by('-date')
        queryset = filtering(queryset, request)
        resp = JsonResponse(data=to_json(queryset), status=200, safe=False)
        return resp

    def delete(self, request, *args, **kwargs):
        obj_id = request.GET.get('id', None)
        if obj_id:
            try:
                object = Transactions.objects.get(
                    pk=request.GET.get('id', None))
                object.delete()
            except:
                pass

        return redirect('transactions')

    def get_queryset(self):
        return self.model.objects.all()
