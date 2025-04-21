from django.db import models

# Driver Model.
class Driver(models.Model):
    id_drive = models.AutoField(primary_key=True, editable=False)
    document = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.name}{self.last_name}'
    
#Vehicle Model.
class Vehicle(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE)
    plate = models.CharField(max_length=6, unique=True)
    

