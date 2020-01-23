from django.db import models

# Create your models here.
class CompanyDetail(models.Model):
    
    model = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    price = models.FloatField()
    Engine = models.IntegerField()
    seat_capacity = models.IntegerField()
    mileage=models.FloatField()

    
    first_kms = models.IntegerField()
    first_engine_oil=models.IntegerField()
    first_oil_filter=models.FloatField()
    first_air_filter=models.IntegerField()
    first_fuel_filter=models.IntegerField()
    first_service_cost=models.FloatField()
    first_Brake_oil=models.IntegerField()

    second_kms = models.IntegerField()
    second_engine_oil=models.IntegerField()
    second_oil_filter=models.FloatField()
    second_air_filter=models.IntegerField()
    second_fuel_filter=models.IntegerField()
    second_service_cost=models.FloatField()
    second_Brake_oil=models.IntegerField()

    third_kms = models.IntegerField()
    third_engine_oil=models.IntegerField()
    third_oil_filter=models.FloatField()
    third_air_filter=models.IntegerField()
    third_fuel_filter=models.IntegerField()
    third_service_cost=models.FloatField()
    third_Brake_oil=models.IntegerField()

    four_kms = models.IntegerField()
    four_engine_oil=models.IntegerField()
    four_oil_filter=models.FloatField()
    four_air_filter=models.IntegerField()
    four_fuel_filter=models.IntegerField()
    four_service_cost=models.FloatField()
    four_Brake_oil=models.FloatField()

    five_kms = models.IntegerField()
    five_engine_oil=models.IntegerField()
    five_oil_filter=models.FloatField()
    five_air_filter=models.IntegerField()
    five_fuel_filter=models.IntegerField()
    five_service_cost=models.FloatField()
    five_Brake_oil=models.IntegerField()

    six_kms = models.IntegerField()
    six_engine_oil=models.IntegerField()
    six_oil_filter=models.FloatField()
    six_air_filter=models.FloatField()
    six_fuel_filter=models.FloatField()
    six_service_cost=models.FloatField()
    six_Brake_oil=models.FloatField()

    first_maintenance_cost =models.FloatField()
    second_maintenance_cost =models.FloatField()
    third_maintenance_cost =models.FloatField()
    four_maintenance_cost =models.FloatField()
    five_maintenance_cost =models.FloatField()
    six_maintenance_cost =models.FloatField()

    Average_maintenance_cost = models.IntegerField()
    reliability_index = models.IntegerField()
    link =models.CharField(max_length=200)
    def __str__(self):
        return self.company

