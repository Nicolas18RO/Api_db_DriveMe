from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import Customer
from django.test import TestCase

class CostumerTestCase(APITestCase):
    def setUp(self):
        #crear la inatacia de la clase Driver
        self.customer =Customer.objects.create(
            full_name_customer="Juan Perez",
            phone_customer="3001234567",
            email_customer="JuanPerez@gmail.com"
        )
    #test for list costumers
    def test_list_customers(self):
        response=self.client.get("/api/customer/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(status.HTTP_200_OK)


    def test_create_customer(self):
        data={
            'full_name_customer':'Camilo Perez',
            'phone_customer':'300234567',
            'email_customer':'CamiloPerez20@gmail.com',  
        }
        response=self.client.post("/api/customer/",data, format='json')
        print("respuesta crear cliente", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name_customer'],'Camilo Perez')

    def test_update_customer(self):
        self.customer=Customer.objects.create(
            full_name_customer='Juan Perez',
            phone_customer='30234567',
            email_customer='Juan@gmail.com'
        )
        update_data = {
            'full_name_customer':'Juan Perez Acostas ',
            'phone_customer':'3032234351',
            'email_customer':'Jua20@gmail.com'
        }
        url =f'/api/customer/{self.customer.id_customer}/'
        response =self.client.put(url,update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name_customer'], "Juan Perez Acostas")

    def test_delete_customer(self):
        url =f'/api/customer/{self.customer.id_customer}/'
        response =self.client.delete(url)
        print("respuesta:",response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response_check =self.client.get (url)
        self.assertEqual(response_check.status_code,status.HTTP_404_NOT_FOUND)



