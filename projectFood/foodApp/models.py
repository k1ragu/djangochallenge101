from django.db import models

# Create your models here.
class Car(models.Model):
   
    fuel_types ={
        "D":"Diesel",
        "P":"Petrol"
    }
    name = models.CharField(max_length=100)
    yop = models.IntegerField()
    descripton = models.CharField(max_length=250)
    fueltype = models.CharField(max_length=1, choices = fuel_types)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    PlantType = models.CharField()
    species = models.CharField(max_length=200)
    Bio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Animal(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    AnimalColor = models.CharField()
    species = models.CharField(max_length=200)
    Bio = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





