from typing import SupportsRound
from django.forms.utils import ErrorDict
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.utils import html
from .forms import CustomerRegistration
from .models import cus
from .forms import Customersearch
from .models import *

#navigate to home page
def home(request):
  return render(request,"home.html")

#this function will add new customers
def add(request):
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
 return render( request, 'add.html',{'form': fm,'stu':stud})


#this function will view registered customers
def create(request):
 if request.method == 'POST' :
  fm = CustomerRegistration(request.POST)    
 else:
  fm = CustomerRegistration()  
 stud = cus.objects.all()
 return render( request, 'create.html',{'form': fm,'stu':stud})



 #this function will update/edit registered customers
def update_data(request, id):
 if request.method == 'POST':
  pi = cus.objects.get(pk=id)
  fm = CustomerRegistration(request.POST, instance=pi)
  if fm.is_valid():
   fm.save()  
 else:
    pi = cus.objects.get(pk=id)
 fm = CustomerRegistration(instance=pi)         
 return render(request,'update.html', {'form' :fm } )
     
#this function will delete new customers
def delete_data(request, id):
 if request.method == 'POST':
  pi = cus.objects.get(pk=id)
  pi.delete()        
 return redirect('/create')

#this function will search customers
def search(request):
  fm = Customersearch(request.POST or None)
  stud = cus.objects.all()
  if request.method == 'POST':
   given_name =request.POST['name']
   stud = cus.objects.filter(phone_number=given_name)
  return render(request, 'create.html',{'form': fm,'stu':stud})
  
