from rest_framework import serializers
from .models import Driver, Customer, Routes, Trips, Estimates, Vehicle

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class customerSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class RoutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Routes
        fields = '__all__'  

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'  

class EstimatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimates
        fields = '__all__'  

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'  
