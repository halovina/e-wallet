from django.db import models
from balance.models import MainBalance
from account.models import AccountType
from internal.utils import CreateUpdate

# Create your models here.
class GeneralLedger(CreateUpdate):
    balance = models.ForeignKey(MainBalance, related_name='balance_ledger', on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, related_name='account_type_ledger', on_delete=models.CASCADE)
    debit = models.FloatField(default=0.0)
    creadit =models.FloatField(default=0.0)
    reference_id = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'ledger'