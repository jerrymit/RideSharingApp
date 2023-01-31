from django import forms
from .models import DriverInfo

class DriverForm(forms.ModelForm):
    class Meta:
        model = DriverInfo
        fields = ['fname','lname','carType','license','max_passenger']