from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import Vehicle

class VehicleTestCase(APITestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            document_driver="54321",
            full_name_driver="Pedro Gomez",
            email_driver="pedro@gmail.com",
            phone_driver="3001230000"
        )
        self.type_vehicle = TypeOfVehicle.objects.create(name_type_vehicle="Taxi")
        self.vehicle = Vehicle.objects.create(
            driver=self.driver,
            type_vehicle=self.type_vehicle,
            plate="XYZ123",
            model="Toyota Corolla",
            year="2020"
        )

    def test_list_vehicles(self):
        response = self.client.get("/api/vehicle/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_vehicle(self):
        data = {
            "driver": self.driver.id_drive,
            "type_vehicle": self.type_vehicle.id_type_vehicle,
            "plate": "ABC456",
            "model": "Kia Rio",
            "year": "2021"
        }
        response = self.client.post("/api/vehicle/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_vehicle(self):
        update_data = {
            "driver": self.driver.id_drive,
            "type_vehicle": self.type_vehicle.id_type_vehicle,
            "plate": "XYZ123",
            "model": "Toyota Yaris",
            "year": "2022"
        }
        url = f"/api/vehicle/{self.vehicle.plate}/"
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_vehicle(self):
        url = f"/api/vehicle/{self.vehicle.plate}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
