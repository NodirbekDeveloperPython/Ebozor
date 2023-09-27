from .models import *
from rest_framework.serializers import ModelSerializer

class BolimSerializers(ModelSerializer):
    class Meta:
        model = Bolim
        fields = '__all__'

class PruductsSerializers(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'