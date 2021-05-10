from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
	name=models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.name



 
class Complain(models.Model):
	name=models.CharField(max_length=100,blank=True)
	department=models.CharField(max_length=100,blank=True)
	complain=models.TextField(blank=True)

	add_time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.department





class Suggestion(models.Model):
	name = models.CharField(max_length=100)
	department=models.CharField(max_length=100)
	suggestion=models.TextField()
	add_time=models.DateTimeField(auto_now=True)










class Vendor(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name=models.CharField(max_length=200,null=True,blank=True)
	phone=models.CharField(max_length=200,null=True,blank=True)
	email=models.EmailField(max_length=200,null=True,blank=True)
	date_created=models.DateTimeField(auto_now_add=True,null=True)
	price=models.TextField(null=True,blank=True)
	address=models.TextField(null=True,blank=True)
	insta=models.CharField(max_length=2048,null=True,blank=True)
	twitter=models.CharField(max_length=2048,null=True,blank=True)
	fb=models.CharField(max_length=2048,null=True,blank=True)
	
	TimesBooked=models.IntegerField(null=True,blank=True)
	bio=models.TextField(null=True,blank=True)
	Options=(('Electricity','Electricity'),
				('HouseKeeping','HouseKeeping'),
				('PestControl','PestControl'),
				('Carpenter','Carpenter'),
				('Milk','Milk'),
				('Civil','Civil'),
				('Newspaper','Newspaper'),
				('Plumber','Plumber'),)
	
	image=models.ImageField(default="no-profile-pic-icon-27.jpg",null=True,blank=True)
	Authenticated=models.BooleanField(default=False,null=True,blank=True)
	type=models.CharField(max_length=200,null=True,choices=Options)
	def __str__(self):
		return self.name


class Customer(models.Model):
	user = models.OneToOneField(User, null=True,  on_delete=models.CASCADE,blank=True)
	name=models.CharField(max_length=200,null=True,blank=True)
	phone=models.CharField(max_length=200,null=True,blank=True)
	email=models.EmailField(max_length=200,null=True,blank=True)
	date_created=models.DateTimeField(auto_now_add=True,null=True,blank=True)
	address=models.CharField(max_length=200,null=True,blank=True)
	maintencefees=models.FloatField(null=True,blank=True)
	liked=models.ManyToManyField(Vendor)
	
	def __str__(self):
		return self.name

	




class Order(models.Model):
	STATUS=(
		('Pending','Pending'),
		('Completed','Completed'),
	)
	
	customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)

	vendor=models.ForeignKey(Vendor,null=True,on_delete=models.SET_NULL)

	date_created=models.DateTimeField(auto_now_add=True,null=False)
	status=models.CharField(max_length=200,null=True,choices=STATUS)
	

class Booking(models.Model):
	Options=(('Club House','Club House'),
		('Guest House','Guest House'),
		('Function Hall','Function Hall'))
	STATUS=(('Approved','Approved'),
		('Pending','Pending'),
		('Denied','Denied'))
	customer=models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
	date_created=models.DateTimeField(auto_now_add=True,null=False,blank=True)

	Type=models.CharField(max_length=200,null=True,blank=True,choices=Options)
	status=models.CharField(max_length=200,null=True,blank=True,choices=STATUS)
	
	startdate=models.DateField(null=True,blank=True)
	reason=models.TextField(null=True,blank=True)
	
	


