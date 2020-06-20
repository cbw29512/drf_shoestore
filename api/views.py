from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import ShoeSerializer, ShoeColorSerializer, ShoeTypeSerializer, ManufacturerSerializer
from api.models import Shoe, ShoeColor, ShoeType, Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer

    #https://www.django-rest-framework.org/tutorial/quickstart/