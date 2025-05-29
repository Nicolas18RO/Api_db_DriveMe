from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import Route

class RouteTestCase(APITestCase):
    def setUp(self):
        self.route = Route.objects.create(
            origin_name="Plaza Central",
            origin_point="5.3096,-73.8149",
            destination_name="Universidad",
            destinantion_point="5.3200,-73.8100",
            distancia=2.5,
            estimated_time=10
        )

    def test_list_routes(self):
        response = self.client.get("/api/route/")
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)

    def test_create_route(self):
        data = {
            "origin_name": "Parque Principal",
            "origin_point": "5.3100,-73.8150",
            "destination_name": "Hospital",
            "destinantion_point": "5.3250,-73.8120",
            "distancia": 3.0,
            "estimated_time": 12
        }
        response = self.client.post("/api/route/", 
                                    data, format="json")
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)

    def test_update_route(self):
        update_data = {
            "origin_name": "Plaza Central",
            "origin_point": "5.3096,-73.8149",
            "destination_name": "Centro Comercial",
            "destinantion_point": "5.3220,-73.8125",
            "distancia": 2.7,
            "estimated_time": 11
        }
        url = f"/api/route/{self.route.id_route}/"
        response = self.client.put(url, update_data,
                                    format="json")
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)

    def test_delete_route(self):
        url = f"/api/route/{self.route.id_route}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code,
                          status.HTTP_204_NO_CONTENT)