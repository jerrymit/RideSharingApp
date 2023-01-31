from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


CAR_CHOICES = (
    ('SUV','SUV'),
    ('Sedan', 'Sedan'),
    ('Crossover','Crossover'),
    ('Minivan','Minivan'),
)

# Create your models here.
class DriverInfo(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    carType = models.CharField(max_length=20, choices=CAR_CHOICES, default='SUV')
    max_passenger = models.CharField(max_length = 1)
    license = models.CharField(max_length = 200)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.lname