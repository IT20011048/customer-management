from django import forms
from django.db.models import fields
from .models import cus
from django.core.validators import RegexValidator,MinLengthValidator


class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = cus
        fields = ('name', 'address', 'phone_number', 'email_address')

        widgets = {

             'name' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter customer name'}),
             'address' : forms.TextInput(attrs={'class': 'form-control','placeholder': 'enter customer address'}),
             'phone_number' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'enter customer phone number'}),
             'email_address' : forms.EmailInput(attrs={'class': 'form-control','placeholder': 'enter customer email address'}),          

        }

class Customersearch(forms.ModelForm):

    class Meta:
        model = cus
        fields = ['phone_number']

        