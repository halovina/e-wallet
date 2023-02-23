from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

class CreateUpdate(models.Model):
    created_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.now()

        self.update_date = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
        
        
def is_administrator(function):
    def wrapper(request, *args, **kwargs):
        chekUser = User.objects.get(id=request.user.id)
        if chekUser.is_staff == False:
            return HttpResponseRedirect('/home/dashboard')
        return function(request, *args, **kwargs)
    return wrapper
