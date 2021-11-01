from django.shortcuts import render
from rest_framework import generics, viewsets, filters
from rest_framework.serializers import Serializer
from .models import Person
from .serializers import PersonSerializer

# Create your views here.


class PersonSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all().order_by("birthdate")
        person_gender = self.request.query_params.get("gender")
        if person_gender is not None:
            queryset = queryset.filter(gender=person_gender)
        return queryset


class FemaleMereenSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.filter(city="Meeren", gender="F")
