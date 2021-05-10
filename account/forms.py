from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import  forms
from.models import Customer,Vendor,Booking


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
         
class VendorForm(ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
		 
class VendorFormImage(ModelForm):
	class Meta:
		model = Vendor
		fields =['image']

class BookingForm(ModelForm):
	class Meta:
		model=Booking
		fields='__all__'
		
