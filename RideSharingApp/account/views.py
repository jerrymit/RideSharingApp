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


def ViewRideDetail(request, id):
    object = RideRequestInfo.objects.get(id = id)
    return render(request, "registration/driver_claim_view.html", {'object': object})

def Comfirm(request, id):
    object = RideRequestInfo.objects.get(id = id)
    object.status = 'COMFIRM'
    object.driver = request.user.username
    user_points = DriverInfo.objects.get(user = request.user)
    object.driver_fname = user_points.fname
    object.driver_lname = user_points.lname
    object.license = user_points.license
    object.save()
    return redirect('DriverPage')

def DriverRideSearch(request):
    if request.method == "POST":
        carType = request.POST['carType']
        max_cap = request.POST['num_passenger']
        specialR = request.POST['specialRequest']
        objects = RideRequestInfo.objects.filter(status = 'OPEN').filter(carType = carType).filter(num_passenger__lte = max_cap)
        if specialR is not None:
           objects = objects.filter(specialRequest = specialR)
        if max_cap is None:
            return render(request, "registration/driver_page.html")
        return render(request, "registration/driver_search.html", {'objects':objects})
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
                owner = request.user.username,
                user = str(request.user.id),
            )
            return render(request, "registration/owner_page.html")
        else:
            return render(request, "registration/ride_request.html")
    else:    
        return render(request, "registration/ride_request.html")    

def RequestEdit(request):
    if request.method == "POST":
        form = RideRequestForm(request.POST or None)
        if form.is_valid():
            user = request.user
            defaults= {
                'address' : request.POST['address'],
                'dateTime' : request.POST['dateTime'],
                'carType' : request.POST['carType'],
                'num_passenger' : request.POST['num_passenger'],
                'isShared' : request.POST['isShared'],
                'specialRequest' : form.cleaned_data['specialRequest']
            }
            share=request.POST['isShared'], 
            share=(share=="True")
            ownerR = RideRequestInfo.objects.update_or_create(user = user, defaults=defaults)[0]
            return render(request, "registration/owner_page.html", {'ownerR':ownerR})
        else:
            return render(request, "registration/request_edit.html")
    else:    
        return render(request, "registration/request_edit.html")


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
            user = request.user
            defaults= {'fname' : request.POST['fname'],
                'lname' : request.POST['lname'],
                'carType' : request.POST['carType'],
                'license' : request.POST['license'],
                'max_passenger' : request.POST['max_passenger'],
            }
            
            driver = DriverInfo.objects.update_or_create(user = user, defaults=defaults)[0]
            
            #driver = DriverInfo.objects.filter(user = user)
            return render(request, "registration/driver_page.html",{'driver':driver})
        else:
            return render(request, "registration/driver_info.html",{})
    else:
        form = DriverForm()
        return render(request, "registration/driver_info.html",{})

def StatusView(request):
    all_status = RideRequestInfo.objects.all
    return render(request,"registration/StatusView_Owner.html", {'all' : all_status})

def DriverPage(request):
    user = request.user
    if DriverInfo.objects.filter(user=user).exists():
        driver = DriverInfo.objects.filter(user = user)[0]
        requests = RideRequestInfo.objects.filter(driver = request.user.username)
        return render(request, "registration/driver_page.html",{'driver':driver,'requests':requests})
    else:
        return redirect('DriverRegister')

def Owner(request):
    return render(request, "registration/owner_page.html")

def Ridesharer(request):
    return render(request, "registration/rideshare_page.html")
