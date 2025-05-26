from rest_framework import serializers
from .models import Driver, Customer, Route, Trip, Vehicle, TypeOfVehicle

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
        model = Route
        fields = '__all__'  

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'  

class TypeofvehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfVehicle
        fields = '__all__'  

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'  
