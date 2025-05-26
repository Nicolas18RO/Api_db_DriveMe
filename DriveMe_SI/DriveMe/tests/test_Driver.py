from rest_framework.test import APITestCase
from rest_framework import status
from DriveMe.models import Driver
from django.test import TestCase

 
class DriverTestCase(APITestCase):
    def setUp(self):
        #crear la inatacia de la clase Driver
        self.driver =Driver.objects.create(
            document_driver="1898444",
            full_name_driver="Juan Perez",
            email_driver="juanPerez@gmail.com",
            phone_driver="3001234567"
        )
    #Test for list drivers 
    def test_list_drivers(self):
        response =self.client.get("/api/driver/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(status.HTTP_200_OK)
    #Test for create driver 
    def test_create_driver(self):
        data ={
            'document_driver':'18444',
            'full_name_driver':'Juan Perez',
            'email_driver':'juanPerez20@gmail.com',
            'phone_driver':'300234567'
        }
        response=self.client.post('/api/driver/', data, format='json')
        print("Respuesta crear conductor:", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertEqual(response.data['full_name_driver'], "Juan Perez")
       
    #Test for update driver
    def test_update_driver(self):
        self.driver=Driver.objects.create(
            document_driver='18444',
            full_name_driver='Juan Perez',
            email_driver='juanAraujoPerez@gmail.com',
            phone_driver='3098145')
        update_data = {
            'document_driver':'189823467',
            'full_name_driver':'Juan Perez Acostas ',
            'email_driver':'juanPerezAcostasq@gmail.com',
            'phone_driver':'303221'
        }
        url =f'/api/driver/{self.driver.id_drive}/'
        response =self.client.put(url,update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name_driver'], "Juan Perez Acostas")
    #Test for delete driver    
    def test_delete_driver(self):
        url =f'/api/driver/{self.driver.id_drive}/'
        response =self.client.delete(url)
        print("respuesta:",response.data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response_check =self.client.get (url)
        self.assertEqual(response_check.status_code,status.HTTP_404_NOT_FOUND)