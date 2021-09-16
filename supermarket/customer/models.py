from enum import unique
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.core.validators import RegexValidator,MinLengthValidator



class cus(models.Model):

  alphabetic = RegexValidator(r'^[a-zA-Z .]*$', 'Only letters are allowed.')
  EMAIL_REGEX = RegexValidator( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[com|lk]+$)")


  name = models.TextField(validators = [MinLengthValidator(4),alphabetic],max_length=80, blank=False, null=False)
  address = models.CharField(validators = [MinLengthValidator(5)],max_length=150,blank=False, null=False)
  phone_number = models.CharField(validators = [MinLengthValidator(10)],max_length=10, blank=False, null=False, unique=True,)
  email_address = models.CharField(validators=[EMAIL_REGEX],max_length=70,unique=True)
  