from django.contrib import admin
from .models import cus
# Register your models here.

@admin.register(cus)
class useradmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone_number','email_address')