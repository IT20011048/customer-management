from typing import SupportsRound
from django.forms.utils import ErrorDict
from django.shortcuts import render
from .forms import CustomerRegistration
from .models import cus

# Create your views here.

#this function will add new customers
def add_show(request):
 if request.method == 'POST' :
  fm = CustomerRegistration(request.POST) 
  if  fm.is_valid() :
   nm = fm.cleaned_data['name']
   ad = fm.cleaned_data['address']
   pn = fm.cleaned_data['phone_number']
   em = fm.cleaned_data['email_address']
   reg = cus(name=nm,address=ad,phone_number=pn,email_address=em)
   reg.save()  
   fm = CustomerRegistration()     
 else:
  fm = CustomerRegistration()  
 stud = cus.objects.all()
 return render( request, 'customer/create.html',{'form': fm,'stu':stud})
    
#this function will delete new customers