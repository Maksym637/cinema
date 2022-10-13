from rest_framework.test import APITestCase
from rest_framework import status
from app_hall.models import Hall
from app_hall.serializers import HallSerializer


class HallViewTest(APITestCase):
    URL = '/hall/'
    HALL_DATA_CORRECT = {"number": 10, "max_people_count": 100}
    HALL_DATA_INCORRECT = {"number": "...", "max_people_count": "..."}

    def test_get_halls(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_hall(self):
        create = self.client.post(self.URL, data=self.HALL_DATA_CORRECT, format='json')

        response = self.client.get(self.URL + str(create.data["id"]) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["max_people_count"], self.HALL_DATA_CORRECT["max_people_count"])

        response = self.client.get(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_hall(self):
        response = self.client.post(self.URL, data=self.HALL_DATA_CORRECT, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["number"], self.HALL_DATA_CORRECT["number"])

        response = self.client.post(self.URL, data=self.HALL_DATA_INCORRECT, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_delete_hall(self):
        create = self.client.post(self.URL, data=self.HALL_DATA_CORRECT, format='json')

        response = self.client.delete(self.URL + str(create.data["id"]) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
