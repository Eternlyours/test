from django.contrib import admin
from .models import Accounts, Transactions


class AccountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance', )
    fields = ('id', 'name', 'balance', )
    readonly_fields = ('id', )


class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_id', 'account_balance', 'date', 'amount', )
    fields = ('id', 'account_id', 'account_balance', 'date', 'amount', )
    readonly_fields = ('id', 'date', 'account_balance', )


admin.site.register(Accounts, AccountsAdmin)
admin.site.register(Transactions, TransactionsAdmin)
