from enum import unique
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

class cus(models.Model):
  name = models.CharField(max_length=80, blank=False, null=False)
  address = models.CharField(max_length=150,blank=False, null=False)
  phone_number = models.CharField(max_length=15, blank=False, null=False, unique=True,)
  email_address = models.CharField(max_length=70,unique=True)
