from DriveMe.models import Driver, Customer, Route, Trip

class TripTestCase(APITestCase):
    def setUp(self):
        self.driver = Driver.objects.create(
            document_driver="1122334455",
            full_name_driver="Laura Sánchez",
            email_driver="laura@example.com",
            phone_driver="3114567890"
        )
        self.customer = Customer.objects.create(
            full_name_customer="Carlos Ruiz",
            phone_customer="3204567890",
            email_customer="carlos@example.com"
        )
        self.route = Route.objects.create(
            origin_name="Terminal",
            origin_point="5.3110,-73.8100",
            destination_name="Centro",
            destinantion_point="5.3200,-73.8110",
            distancia=1.8,
            estimated_time=8
        )
        self.trip = Trip.objects.create(
            id_driver=self.driver,
            id_customer=self.customer,
            id_route=self.route,
            status="pending"
        )

    def test_list_trips(self):
        response = self.client.get("/api/trip/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_trip(self):
        data = {
            "id_driver": self.driver.id_drive,
            "id_customer": self.customer.id_customer,
            "id_route": self.route.id_route,
            "status": "in_progress"
        }
        response = self.client.post("/api/trip/", 
                                    data, format="json")
        self.assertEqual(response.status_code, 
                         status.HTTP_201_CREATED)

    def test_update_trip_status(self):
        url = f"/api/trip/{self.trip.id}/"
        update_data = {
            "id_driver": self.driver.id_drive,
            "id_customer": self.customer.id_customer,
            "id_route": self.route.id_route,
            "status": "completed"
        }
        response = self.client.put(url, 
                                   update_data, format="json")
        self.assertEqual(response.status_code, 
                         status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "completed")

    def test_delete_trip(self):
        url = f"/api/trip/{self.trip.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code,
                          status.HTTP_204_NO_CONTENT)