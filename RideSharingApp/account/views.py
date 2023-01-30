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


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def DriverRegister(request):
    return render(request, "registration/driver_info.html")

def DriverPage(request):
    return render(request, "registration/driver_page.html")

def RideRequest(request):
    return render(request, "registration/ride_request.html")

def Owner(request):
    return render(request, "registration/owner_page.html")

def Ridesharer(request):
    return render(request, "registration/rideshare_page.html")
