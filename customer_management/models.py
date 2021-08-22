from enum import unique
from django.db import models
from django.db.models.base import Model


class User(models.Model):
  name = models.CharField(max_length=80, null=False,blank=False)
  address = models.CharField(max_length=150, null=False,blank=False)
  phone = models.PhoneNumberField(null=False, blank=False, unique=True)
  email = models.CharField(max_length=70,null=False,blank=False)
