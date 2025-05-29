from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import TypeOfVehicle

class TypeOfVehicleTestCase(APITestCase):

    def setUp(self):
        self.type_of_vehicle = TypeOfVehicle.objects.create(
            name_type_vehicle="Camioneta"
        )

    def test_list_type_of_vehicle(self):
        response = self.client.get
        ("/api/type_of_vehicle/")
        self.assertEqual(response.status_code,
                          status.HTTP_200_OK)
        print("List status:", 
              response.status_code)

    def test_create_type_of_vehicle(self):
        data = {
            'name_type_vehicle': "Sedan",
        }
        response = self.client.post("/api/type_of_vehicle/", 
                                    data, format='json')
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)
        print("Create response data:", response.data)

    def test_update_type_of_vehicle(self):
        update_data = {"name_type_vehicle":
                        "Camioneta 4x4"}
        url = f"/api/type_of_vehicle/{self.type_of_vehicle.
                                      id_type_vehicle}/"
        response = self.client.put(url, update_data, 
                                   format='json')
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)

    def test_delete_type_of_vehicle(self):
        url = f"/api/type_of_vehicle/{self.type_of_vehicle
                                      .id_type_vehicle}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.
                         HTTP_204_NO_CONTENT)
