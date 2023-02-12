from django.db import models

# Create your models here.
class AccountType(models.Model):
    type_name = models.CharField(blank=True, null=True, max_length=50)
    slug = models.CharField(blank=True, null=True, max_length=75)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'account_type'