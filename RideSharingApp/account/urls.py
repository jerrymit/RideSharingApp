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
    path("shareride/search/", views.SharerRideSearch, name="SharerRideSearch"),
    path('owner/', views.Owner, name='Owner'),
    path('Driverdb/', views.DriverDB, name = 'DriverDB'),
    path('<int:id>/Request_edit/', views.RequestEdit, name = 'RequestEdit'),
    path('StatusView_Owner/', views.StatusView, name = 'StatusView'),
    path('<int:id>/Comfirm/', views.Comfirm, name = 'Comfirm'),
    path('<int:id>/Join/', views.Join, name = 'Join'),
    path('<int:id>/Complete/', views.Complete, name = 'Complete'),
    path('<int:id>/ViewRideDetail/', views.ViewRideDetail, name = 'ViewRideDetail'),
]