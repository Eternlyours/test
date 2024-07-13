from django.db import models

from accounts.service import create_transaction, delete_transaction
from .utils import get_format_date


class Accounts(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    name = models.CharField(verbose_name='Название счёта', max_length=50)
    balance = models.DecimalField(
        verbose_name='Баланс', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Счёт'

    def __str__(self):
        return str(self.id)

    def json(self):
        return {
            'id': str(self.id),
            'name': str(self.name),
            'balance': str(self.balance)
        }


class Transactions(models.Model):
    id = models.AutoField(verbose_name='Идентификатор', primary_key=True)
    account_id = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, verbose_name='Счёт')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    amount = models.DecimalField(
        verbose_name='Cумма', max_digits=10, decimal_places=2)
    account_balance = models.DecimalField(
        verbose_name='Баланс на момент поступления', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Операция'

    def save(self, *args, **kwargs):
        create_transaction(self)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        delete_transaction(self)
        return super().delete(*args, **kwargs)

    def json(self):
        return {
            'id': str(self.id),
            'account_id': str(self.account_id),
            'account_balance': str(self.account_balance),
            'date': get_format_date(self.date),
            'amount': str(self.amount)
        }
