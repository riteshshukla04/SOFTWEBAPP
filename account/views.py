from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import Group

from .forms import CreateUserForm,CustomerForm,VendorForm,OrderForm,VendorFormImage,BookingForm
from django.contrib import messages
from .models import Complain, Suggestion
from .models import Order,Vendor,Customer
from .models import *
from .decorators import unauthenticated_user,allowed_users,authenticated_user
from django.core.signals import request_finished
from django.dispatch import receiver
from django.contrib.auth import authenticate,login,logout
from .filters import OrderFilter
import os
from .ProblemSolving import Checkfreeslot
from datetime import date,datetime

GuestHouseNumber=1
ClubHouseNumber=1
HallNumber = 2




@csrf_exempt
@unauthenticated_user
def Login(request):
    context={}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
           messages.info(request,"Username or password incorrect")             
     
    return render(request,'login2.html',context)




@csrf_exempt
@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)
            mob=request.POST.get("phone")
            custom=Customer(name=user.username,user=user,email=user.email,phone=mob)
            custom.save()
            messages.success(request,"Account was created")
            return redirect("/login")
    context={'form':form}
    return render(request,'register2.html',context)







def logoutUser(request):
    logout(request)
    return redirect("/")





def userPage(request):
    
    return render(request,"user.html")




def homepage(request):
    total_orders=0
    checkvendor=False
    if request.user.groups.filter(name='vendor').exists():
        total_orders=Order.objects.filter(vendor=Vendor.objects.get(user=request.user)).count()
        checkvendor=True
    if request.user.groups.filter(name='customer').exists():
        total_orders=Order.objects.filter(customer=Customer.objects.get(user=request.user)).count()
        checkvendor=False
    today=date.today()
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    context={"total_orders":total_orders,"today":today,'current_time':current_time,'checkvendor':checkvendor}
    return render(request,'hi.html',context)




@authenticated_user
def feedbackhome(request):
    return render(request, 'feedbackhome.html')



@csrf_exempt
@unauthenticated_user
def VendorRegister(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            global usernameForm
            usernameForm=form.cleaned_data.get('username')
            group=Group.objects.get(name='vendor')
            user.groups.add(group)
            
                       
            vend=Vendor(name=user.username,user=user,email=user.email)
            vend.save()
            messages.success(request,'Account was created')
            
            return redirect('/vendorform/')
    context={'form':form}
    return render(request,'registerVendor1.html',context)



@csrf_exempt
@unauthenticated_user
def VendorForm(request):
    if request.method == 'POST':

        
        phone = request.POST['Phone']
        pic=request.FILES['pic']
        add=request.POST['Address']
        cost=request.POST['cost']
        bio=request.POST['Bio']
        type=request.POST['type']
        insta=request.POST['Instagram']
        fb=request.POST['fb']
        twitter=request.POST['twitter']
        vendors=Vendor.objects.get(name=usernameForm)
        vendors.address=add
        vendors.price=cost

        vendors.bio=bio
        vendors.type=type
        vendors.insta=insta
        vendors.fb=fb
        vendors.twitter=twitter
        vendors.TimesBooked=0
        
        vendors.type=type
        vendors.phone=phone
        
        vendors.image=pic
        vendors.save()
        messages.success(request,"Account was successfully Created")
        return redirect("/")
        
    
    return render(request,'vendorform.html')





	




@authenticated_user
def add_complain(request):
    if request.method == 'POST':
        name = request.user.username
        depart = request.POST['depart']
        complain = request.POST['complain']
        compl = Complain(department=depart, complain=complain, name=name)
        compl.save()
        messages.success(request, 'Complain has been registered.')
    return render(request, 'add-complain.html')






@authenticated_user
def add_suggestion(request):
    if request.method == 'POST':
        name = request.user.username
        depart = request.POST['depart']
        suggestion = request.POST['suggest']
        sugg = Suggestion(department=depart, suggestion=suggestion, name=name)
        sugg.save()
        messages.success(request, 'Thank you for your suggestion.')
    return render(request, 'add-suggestion.html')





@allowed_users(['vendor'])
def vendors(request):
    orders=Order.objects.filter(vendor=Vendor.objects.get(user=request.user)).order_by('-date_created')
    
    total_orders=orders.count()
    delivered=orders.filter(status="Completed").count()
    pending=orders.filter(status="Pending").count()
    context={'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'Vendorsorder.html',context)







@authenticated_user
def myorder(request):

    custom=Customer.objects.get(user=request.user)
    orders=Order.objects.filter(customer=Customer.objects.get(user=request.user)).order_by('-date_created')
    booking=Booking.objects.filter(customer=Customer.objects.get(user=request.user))

    total_orders=orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    delivered=orders.filter(status="Completed").count()
    pending=orders.filter(status="Pending").count()
    x=custom.liked.all()
    
    context={'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending,'custom':custom,'myFilter':myFilter,'x':x,'booking':booking}
    return render(request,'myorders.html',context)





@csrf_exempt
@authenticated_user
def updatecustomer(request,pk):
    custom=Customer.objects.get(user=request.user)
    form=CustomerForm(instance=custom)
    if request.method=='POST':
        form=CustomerForm(request.POST,instance=custom)
        if form.is_valid():
            form.save()
            return redirect("/myorder")
    context={'form':form}
    return render(request,'updateform.html',context)
        


def store(request,pk):
    vendor1=Vendor.objects.filter(type=pk).order_by("-TimesBooked")
    
    

    context={'products': vendor1}
    return render(request,'shoppinggrid.html',context)





def vendorinfo(request,pk):
    vendor1=Vendor.objects.get(name=pk)
    context={'vendors':vendor1}
         
    return render(request,'vendorinfo.html',context)









@authenticated_user
def complete_order(request,pk):
    order=Order.objects.get(id=pk)
    order.status="Completed"
    order.save()
    return redirect("/Vendor")




@authenticated_user
def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    order.delete()
    if request.user.groups.filter(name='vendor').exists():
        
            return redirect("/Vendor")
    return redirect("/myorder")


@authenticated_user
@allowed_users(['customer'])
def add_order(request,pk):
    
    vend=Vendor.objects.get(id=pk)
    vend.TimesBooked+=1
    vend.save()
    custom=Customer.objects.get(user=request.user)
    
    order=Order(customer=custom,vendor=vend,status="Pending")
    order.save()

    messages.warning(request,"Order Successfully Placed")
    return redirect(f"/")    



def contact(request):
    return render(request,'contacts.html')







def search(request):
    query=request.GET['query']
    p1=Vendor.objects.filter(name__contains=query)
    p2=Vendor.objects.filter(type__contains=query)
    products=p1.union(p2)
    context={'products':products}
    return render(request,'search.html',context)


def addlike(request,pk):
    custom=Customer.objects.get(user=request.user)
    vend=Vendor.objects.get(id=pk)
    custom.liked.add(vend)
    custom.save()
    
    return redirect(f"/store/{vend.type}")


def book(request):
    if request.method=='POST':
        custom=Customer.objects.get(user=request.user)
        TYPE12=request.POST['TYPE12']
        start=request.POST['StartDate']
        reason=request.POST['Reason']
        check = Booking.objects.filter(startdate=start,Type=TYPE12).count()
        if check>0:
            return HttpResponse("Already Booked by someone")
        
    
        book=Booking(customer=custom,Type=TYPE12,startdate=start,reason=reason,status="Pending")
        book.save()
        return redirect("/")
    return render(request,'booking.html')


def deleteBooking(request,pk):
    booking=Booking.objects.get(id=pk)
    booking.delete()
    return redirect("/myorder")
    

def updateBooking(request,pk):
    book=Booking.objects.get(id=pk)
    form=BookingForm(instance=book)
    if request.method=="POST":
        form=BookingForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect("/myorder")
       
    context={'form':form}
    return render(request,'updatebook.html',context)

def aboutus(request):
    return render(request,"Aboutus.html")

def check(request):
    return render(request,'register2.html')