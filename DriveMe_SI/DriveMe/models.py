from django.db import models
from django.contrib.gis.db import models as gis_models

# Driver Model.
class Driver(models.Model):
    id_drive = models.AutoField(primary_key=True, editable=False)
    document_driver = models.CharField(max_length=20)
    full_name_driver = models.CharField(max_length=50)
    email_driver = models.EmailField(unique=True)
    phone_driver = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.full_name
    
#Customer Model
class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True, editable=False)
    full_name_customer = models.CharField(max_length=100)
    phone_customer = models.CharField(max_length=20, unique=True)
    email_customer = models.EmailField(unique=True)

#Type of Vehicle
class TypeOfVehicle(models.Model):
    name_type_vehicle = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name_type_vehicle

#Vehicle Model.
class Vehicle(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    type_vehicle = models.ForeignKey(TypeOfVehicle, on_delete=models.SET_NULL, null=True)
    plate = models.CharField(max_length=6, unique=True)
    model = models.CharField(max_length=80)
    year = models.CharField(max_length=4)
    soat_expiration = models.DateField(null=True, blank=True)
    tecnico_mecanica_expiration = models.DateField(null=True, blank=True)

#Route Model
class Route(models.Model):
    id_route = models.AutoField(primary_key=True, editable=False)
    origin_name = models.CharField(max_length=100)
    origin_point = gis_models.PointField()
    destination_name = models.CharField(max_length=100)
    destinantion_point = gis_models.PointField()
    distancia = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estimated_time = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.origin_name} to {self.destination_name}'

#Trip Model
class Trip(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    id_driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    id_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    id_route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True)
    trip_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Trip #{self.id} - {self.status}"


