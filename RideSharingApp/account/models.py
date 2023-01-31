from django.db import models

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
    license = models.CharField(max_length = 200)
    max_passenger = models.CharField(max_length = 1)
    
    def __str__(self):
        return self.lname