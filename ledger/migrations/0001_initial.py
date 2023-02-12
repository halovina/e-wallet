# Generated by Django 4.1.5 on 2023-02-12 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('balance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralLedger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debit', models.FloatField(default=0.0)),
                ('creadit', models.FloatField(default=0.0)),
                ('reference_id', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('updated_date', models.DateTimeField(blank=True, null=True)),
                ('account_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_type_ledger', to='account.accounttype')),
                ('balance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance_ledger', to='balance.mainbalance')),
            ],
            options={
                'db_table': 'ledger',
            },
        ),
    ]
