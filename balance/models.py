from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MainBalance(models.Model):
    user = models.ForeignKey(User, related_name='balance_user', on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'main_ballance'
    