from .models import Driver, Customer, Routes, Trips, Estimates, Vehicle
from django_filter.rest_framework import DjangoFilterBackend
from .serializers import DriverSerializer, customerSerializaer,RoutesSerializer, TripsSerializer, EstimatesSerializer, VehicleSerializer
from rest_framework import generics, filters

# Create your views here.
# --------CRUD Driver--------
class ListCreateDriver(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class RetrieveUpdateDeleteDriver(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

#----------CRUD Customer--------
class ListCreateCustomer(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializaer

class RetrieveUpdateDeleteCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = customerSerializaer

#----------CRUD Routes--------
class ListCreateRoutes(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

class RetrieveUpdateDeleteRoutes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

#----------CRUD Trips--------
class ListCreateTrips(generics.ListCreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

class RetrieveUpdateDeleteTrips(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer

#----------CRUD Estimates--------
class ListCreateEstimates(generics.ListCreateAPIView):
    queryset = Estimates.objects.all()
    serializer_class = EstimatesSerializer
    
class RetrieveUpdaterDeleteEstimates(generics.RetrieveUpdateDestroyAPIView):
    queryset =Estimates.objects.all()
    sarializer_class =EstimatesSerializer 
    

#----------CRUD Vehicle--------
class ListrCreateVehicle(generics.ListCreateAPIView):
    queryset =Vehicle.objects.all()
    sarializer_class =VehicleSerializer

class RetrieveUpdaterDeleteVehicle(generics.RetrieveUpdateDestroyAPIView):
    queryset =Vehicle.objects.all()
    sarializer_class =VehicleSerializer 
    