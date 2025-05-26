from django.urls import path 
from .views import (
    ListCreateDriver,
    RetrieveUpdateDeleteDriver,
    ListCreateCustomer,
    RetrieveUpdateDeleteCustomer,
    ListCreateTrips,
    RetrieveUpdateDeleteTrips,
    ListCreateVehicle,
    RetrieveUpdaterDeleteVehicle, 
    ListCreateTypeOfVehicle,
    RetrieveUpdateDeleteTypeOfVehicle,

)
urlpatterns = [
    path("driver/", ListCreateDriver.as_view(), name="list_create_driver"),
    path("driver/<int:pk>/", RetrieveUpdateDeleteDriver.as_view(), name="retrieve_update_delete_driver"),  
    path("customer/", ListCreateCustomer.as_view(), name="list_create_customer"),
    path("customer/<int:pk>/", RetrieveUpdateDeleteCustomer.as_view(), name="retrieve_update_delete_customer"),
    path("trips/", ListCreateTrips.as_view(), name="list_create_trips"),
    path("trips/<int:pk>/", RetrieveUpdateDeleteTrips.as_view(), name="retrieve_update_delete_trips"),
    path("vehicle/", ListCreateVehicle.as_view(), name="list_create_vehicle"),
    path("vehicle/<int:pk>/", RetrieveUpdaterDeleteVehicle.as_view(), name="retrieve_update_delete_vehicle" ),
    path("type_of_vehicle/", ListCreateTypeOfVehicle.as_view(), name="list_create_type_of_vehicle"),
    path("type_of_vehicle/<int:pk>/", RetrieveUpdateDeleteTypeOfVehicle.as_view(), name="retrieve_update_delete_type_of_vehicle"),
]
 
 