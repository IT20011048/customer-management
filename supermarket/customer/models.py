from enum import unique
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.core.validators import RegexValidator,MinLengthValidator


class cus(models.Model):
   
   #name validation
  alphabetic = RegexValidator(r'^[a-zA-Z .]*$', 'Only letters, spaces and dots are allowed.')
  name_separaterS = RegexValidator (r'^[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+?.?[a-zA-Z]+$','only one space or dot allowed to separate names')
  
  #address validation
  address_regex = RegexValidator (r'^[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?,?.?[a-zA-Z0-9/"]+?(,?)(.?)[a-zA-Z0-9/"]+$','some special characters are not allowed')

  #phone number validator
  phonenum_regex = RegexValidator(r'^[0-9]{1,12}$')

  #email validator
  EMAIL_REGEX = RegexValidator( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-z]{2,8}?\.?([a-z]{2,8})?$)")


  name = models.TextField(validators = [MinLengthValidator(4),alphabetic,name_separaterS,],max_length=100, blank=False, null=False)
  address = models.CharField(validators = [MinLengthValidator(5),address_regex],max_length=150,blank=False, null=False)
  phone_number = models.CharField(validators = [MinLengthValidator(10),phonenum_regex],max_length=12, blank=False, null=False, unique=True)
  email_address = models.CharField(validators=[EMAIL_REGEX],max_length=70,unique=True)
  