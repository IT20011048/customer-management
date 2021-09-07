from django import forms
from django.db.models import fields
from .models import cus
from django.core import validators

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = cus
        fields = ('name', 'address', 'phone_number', 'email_address')

        widgets = {

             'name' : forms.TextInput(attrs={'class': 'form-control'}),
             'address' : forms.TextInput(attrs={'class': 'form-control'}),
             'phone_number' : forms.NumberInput(attrs={'class': 'form-control'}),
             'email_address' : forms.EmailInput(attrs={'class': 'form-control'}),          

        }

class Customersearch(forms.ModelForm):

    class Meta:
        model = cus
        fields = ['phone_number']