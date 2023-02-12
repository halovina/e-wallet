from django.db import models
from balance.models import MainBalance
from account.models import AccountType

# Create your models here.
class GeneralLedger(models.Model):
    balance = models.ForeignKey(MainBalance, related_name='balance_ledger', on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, related_name='account_type_ledger', on_delete=models.CASCADE)
    debit = models.FloatField(default=0.0)
    creadit =models.FloatField(default=0.0)
    reference_id = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'ledger'