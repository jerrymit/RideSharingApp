from django.urls import path

from .views import *
from . import views


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("driver_info/", views.DriverRegister, name="DriverRegister"),
    path("driver_info/driver_page/", views.DriverPage, name="DriverPage"),
    path("driver_info/driver_page/search/", views.DriverRideSearch, name="DriverRideSearch"),
    path('rideRequest/', views.RideRequest, name='RideRequest'),
    path('shareride/', views.Ridesharer, name='Ridesharer'),
    path('owner/', views.Owner, name='Owner'),
    path('Driverdb/', views.DriverDB, name = 'DriverDB')
]