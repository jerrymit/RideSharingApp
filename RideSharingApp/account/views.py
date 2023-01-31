from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth 
from django.urls import reverse
from django.contrib import messages
from .models import DriverInfo
from .forms import DriverForm

def DriverDB(request):
    all_driver = DriverInfo.objects.all
    return render(request,"registration/DriverDB.html", {'all' : all_driver})
    
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def DriverRegister(request):
    if request.method == "POST":
        form = DriverForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
            return render(request, "registration/driver_info.html",{}) 
        user = request.POST['user']
        fname = request.POST['fname']
        lname = request.POST['lname']
        carType = request.POST['carType']
        license = request.POST['license']
        max_passenger = request.POST['max_passenger']
        user = request.user
        driver, created = DriverInfo.objects.update_or_create(
            user = user, 
            defaults= {'fname' : request.POST['fname'],
                'lname' : request.POST['lname'],
                'carType' : request.POST['carType'],
                'license' : request.POST['license'],
                'max_passenger' : request.POST['max_passenger'],
            }
        )
        return render(request, "registration/driver_page.html",{'carType':carType, 'fname':fname, 
                    'lname':lname, 'license':license, 'max_passenger':max_passenger})
    else:
        return render(request, "registration/driver_info.html",{})

def DriverPage(request):
    return render(request, "registration/driver_page.html")

def RideRequest(request):
    return render(request, "registration/ride_request.html")

def Owner(request):
    return render(request, "registration/owner_page.html")

def Ridesharer(request):
    return render(request, "registration/rideshare_page.html")
