from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class BolimViewSets(ModelViewSet):
    queryset = Bolim.objects.all()
    serializer_class = BolimSerializers

class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = PruductsSerializers