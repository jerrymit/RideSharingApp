from django import forms
from .models import DriverInfo, RideRequestInfo

class DriverForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = ['fname','lname','carType','license','max_passenger']

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = RideRequestInfo
        fields = ['address','dateTime','carType','num_passenger','isShared']