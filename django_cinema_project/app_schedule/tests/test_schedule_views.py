from rest_framework.test import APITestCase
from rest_framework import status

from app_hall.models import Hall
from app_film.models import Film
from app_schedule.models import Schedule


class ScheduleViewTest(APITestCase):
    URL = '/schedule/'

    def setUp(self):
        self.hall1 = Hall.create(10, 100)
        self.hall2 = Hall.create(20, 200)
        self.hall1.save()
        self.hall2.save()

        self.film1 = Film.create('film1', 'comedy', 'English', None, '2022-10-3', 3)
        self.film2 = Film.create('film2', 'drama', 'French', None, '2022-10-3', 3)
        self.film1.save()
        self.film2.save()

    def tearDown(self):
        self.hall1.delete()
        self.hall2.delete()
        self.film1.delete()
        self.film2.delete()
    
    def test_get_schedules(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_schedule(self):
        schedule_data = {
            "time_start": "16:00:00", 
            "time_end": "17:30:00", 
            "date": "2022-10-24", 
            "film_id": self.film1.id, 
            "hall_id": self.hall1.id
            }
        
        self.client.post(self.URL, data=schedule_data, format='json')
        id = list(Schedule.objects.filter(time_start=schedule_data['time_start']).values_list('pk', flat=True))[0]

        response = self.client.get(self.URL + str(id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["time_start"], schedule_data["time_start"])

        response = self.client.get(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_schedule(self):
        schedule_data_correct = {
            "time_start": "18:00:00", 
            "time_end": "20:00:00", 
            "date": "2022-10-24", 
            "film_id": self.film2.id, 
            "hall_id": self.hall2.id
            }
        
        response = self.client.post(self.URL, data=schedule_data_correct, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        schedule_data_incorrect = {
            "time_start": ".....",
            "time_end": ".....",
            "date": "2022-10-24",
            "film_id": self.film2.id, 
            "hall_id": self.hall2.id
        }

        response = self.client.post(self.URL, data=schedule_data_incorrect, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post(self.URL, data=schedule_data_correct, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_delete_schedule(self):
        schedule_data = {
            "time_start": "16:00:00", 
            "time_end": "17:30:00", 
            "date": "2022-10-24", 
            "film_id": self.film1.id, 
            "hall_id": self.hall1.id
            }
        
        self.client.post(self.URL, data=schedule_data, format='json')
        id = list(Schedule.objects.filter(time_start=schedule_data['time_start']).values_list('pk', flat=True))[0]

        response = self.client.delete(self.URL + str(id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_schedule(self):
        schedule_data_correct = {
            "time_start": "18:00:00", 
            "time_end": "20:00:00", 
            "date": "2022-10-24", 
            "film_id": self.film2.id, 
            "hall_id": self.hall2.id
            }
        self.client.post(self.URL, data=schedule_data_correct, format='json')
        id = list(Schedule.objects.filter(time_start=schedule_data_correct['time_start']).values_list('pk', flat=True))[0]

        schedule_data_update_correct = {
            "time_start": "20:15:00", 
            "time_end": "22:00:00", 
            "date": "2022-10-24",
        }
        
        response = self.client.put(self.URL + str(id) + '/', data=schedule_data_update_correct, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        schedule_data_update_incorrect = {
            "time_start": ".....", 
            "time_end": ".....", 
            "date": "2022-10-24",
        }

        response = self.client.put(self.URL + str(id) + '/', data=schedule_data_update_incorrect, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
