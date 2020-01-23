from django.db import models

# Create your models here.
class Carcomponent(models.Model):
    model = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    price = models.FloatField()
    airConditioning=models.IntegerField()
    breakingSystem =models.IntegerField()
    coolingSystem = models.IntegerField()
    electrical =models.IntegerField()
    engine=models.IntegerField()
    fuelSystem =models.IntegerField()
    gearBox = models.IntegerField()     
    steeringSystem = models.IntegerField()
    transmission = models.IntegerField()
    link = models.CharField(max_length=200) 

    def __str__(self):
        return self.company