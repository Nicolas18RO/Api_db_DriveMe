from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import Vehicle, Driver, TypeOfVehicle

class VehicleTestCase(APITestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            document_driver="1898444",
            full_name_driver="Juan Perez",
            email_driver="juanPerez@gmail.com",
            phone_driver="3001234567"
        )
        self.type_vehicle = TypeOfVehicle.objects.create(name_type_vehicle="Taxi")
        self.vehicle = Vehicle.objects.create(
            driver=self.driver,
            type_vehicle=self.type_vehicle,
            plate="XYZ123",
            model="Toyota Corolla",
            year="2020"
        )
        self.driver_id=self.driver.id_drive
        self.type_vehicle_id=self.type_vehicle.id_type_vehicle

    def test_list_vehicles(self):
        response = self.client.get("/api/vehicle/")
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)

    def test_create_vehicle(self):
        new_driver=Driver.objects.create(
            document_driver="1002345643",
            full_name_driver="Camila Paez",
            email_driver="CamilaPaez@gmail.com",
            phone_driver="3122581587"
        )

        data = {
            "driver": new_driver.id_drive,
            "type_vehicle": self.type_vehicle_id,
            "plate": "ABC456",
            "model": "Kia Rio",
            "year": "2021"
        }
        response = self.client.post("/api/vehicle/", 
                                    data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)

    def test_update_vehicle(self):  
        update_data = {
            "driver": self.driver_id,
            "type_vehicle": self.type_vehicle_id,
            "plate": "XYZ123",
            "model": "Toyota Yaris",
            "year": "2022"
        }
        url = f"/api/vehicle/{self.vehicle.plate}/"
        response = self.client.put(url, update_data,
                                    format='json')
        print(response.data)
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)

    def test_delete_vehicle(self):
        url = f"/api/vehicle/{self.vehicle.plate}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code,
                          status.HTTP_204_NO_CONTENT)
