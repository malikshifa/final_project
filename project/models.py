from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class shape(models.Model):
    id = models.AutoField(primary_key=True)
    point = models.CharField(max_length=1000)
    shapetype = models.CharField(max_length=100,null=True,blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)

