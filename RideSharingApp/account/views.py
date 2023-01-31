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
from .models import DriverInfo, RideRequestInfo
from .forms import DriverForm, RideRequestForm


def DriverRideSearch(request):
    if request.method == "POST":
        carType = request.POST['carType']
        max_cap = request.POST['num_passenger']
        specialR = request.POST['specialRequest']
        objects = RideRequestInfo.objects.filter(status = 'OPEN').filter(carType = carType).filter(num_passenger__lte = max_cap)
        #if specialR is not None:
         #   objects = objects.filter(specialRequest = specialR)
        if carType or max_cap is not None:
            return render(request, "registration/driver_search.html", {'objects':objects})
        return render(request, "registration/driver_page.html")
    else:
        return render(request, "registration/driver_page.html")

def RideRequest(request):
    if request.method == "POST":
        form = RideRequestForm(request.POST or None)
        if form.is_valid():
            share=(request.POST['isShared']=="True")
            RideRequest = RideRequestInfo.objects.create(
                address = request.POST['address'], 
                dateTime = request.POST['dateTime'],
                carType = request.POST['carType'],
                num_passenger = request.POST['num_passenger'],
                specialRequest = request.POST['specialRequest'],
                isShared=share,
                user = str(request.user.id),
            )
            return render(request, "registration/owner_page.html")
        else:
            return render(request, "registration/ride_request.html")
    else:    
        return render(request, "registration/ride_request.html")    


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
            #form.save()
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            carType = form.cleaned_data['carType']
            license = form.cleaned_data['license']
            max_passenger = form.cleaned_data['max_passenger']
            user = request.user
            defaults= {'fname' : request.POST['fname'],
                'lname' : request.POST['lname'],
                'carType' : request.POST['carType'],
                'license' : request.POST['license'],
                'max_passenger' : request.POST['max_passenger'],
            }
            DriverInfo.objects.update_or_create(user = user, defaults=defaults)
        else:
            return render(request, "registration/driver_info.html",{})
        return render(request, "registration/driver_page.html",{'carType':carType, 'fname':fname, 
                    'lname':lname, 'license':license, 'max_passenger':max_passenger})
    else:
        form = DriverForm()
        return render(request, "registration/driver_info.html",{})

def DriverPage(request):
    return render(request, "registration/driver_page.html")

def Owner(request):
    return render(request, "registration/owner_page.html")

def Ridesharer(request):
    return render(request, "registration/rideshare_page.html")
