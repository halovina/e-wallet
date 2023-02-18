from django.db import models
from internal.utils import CreateUpdate

# Create your models here.
class AccountType(CreateUpdate):
    type_name = models.CharField(blank=True, null=True, max_length=50)
    slug = models.CharField(blank=True, null=True, max_length=75)
    
    class Meta:
        db_table = 'account_type'