from django.shortcuts import render
from rest_framework import generics
from .models import Specie,Place,Sighting
from .serializers import SpecieSerializer , PlaceSerializer, SightingSerializer
# Create your views here.

class SpecieCreate(generics.CreateAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

class SpecieList(generics.ListAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

class SpecieUpdate(generics.UpdateAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer

class SpecieDelete(generics.DestroyAPIView):
    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer



#===================  Places =============================

class PlaceCreate(generics.CreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceUpdate(generics.UpdateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDelete(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

#===================  Sighting =============================

class SightingCreate(generics.CreateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer

class SightingList(generics.ListAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer

class SightingUpdate(generics.UpdateAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer

class SightingDelete(generics.DestroyAPIView):
    queryset = Sighting.objects.all()
    serializer_class = SightingSerializer

