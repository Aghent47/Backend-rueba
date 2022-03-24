from pyexpat import model
from django.db import models

# Create your models here.

class Specie(models.Model):
    
    kingdom = models.CharField(max_length=50)
    edge = models.CharField(max_length=50)
    classe =  models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    gender  = models.CharField(max_length=20)
    specie  = models.CharField(max_length=50)

class Place(models.Model):
    country = models.CharField(max_length=50)
    departament = models.CharField(max_length=50)
    town = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

class Sighting(models.Model):
   
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    scientific_name = models.CharField(max_length=100)
    #place = models.CharField(max_length=100)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    grades = models.CharField(max_length=50)


