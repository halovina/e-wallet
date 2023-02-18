from django.db import models
from django.contrib.auth.models import User
from internal.utils import CreateUpdate

# Create your models here.
class MainBalance(CreateUpdate):
    user = models.ForeignKey(User, related_name='balance_user', on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    
    class Meta:
        db_table = 'main_ballance'
    