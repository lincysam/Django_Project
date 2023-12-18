from rest_framework import serializers
from .models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand
        fields = ['brandname','brand_image']

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = phonemodel
        fields = '__all__'
