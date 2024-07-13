# Generated by Django 5.0.7 on 2024-07-11 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Баланс'),
        ),
    ]