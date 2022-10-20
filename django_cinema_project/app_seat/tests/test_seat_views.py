from rest_framework.test import APITestCase
from rest_framework import status
from app_hall.models import Hall
from app_seat.models import Seat


class BookingViewTest(APITestCase):
    URL = '/seat/'

    def setUp(self):
        self.hall1 = Hall.create(1, 50)
        self.hall2 = Hall.create(2, 50)
        self.hall1.save()
        self.hall2.save()

    def test_get_all_seats(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_seat(self):
        valid_seat_data = {
            "hall_id": self.hall1.id,
            "seating": Seat.SEATING[0][1],
            "is_free": True
        }

        invalid_seat_data1 = {
            "hall_id": 1000,
            "seating": Seat.SEATING[0][1],
            "is_free": True
        }

        invalid_seat_data2 = {
            "hall_id": self.hall1.id,
            "seating": "",
            "is_free": "ASD"
        }

        response = self.client.post(self.URL, data=valid_seat_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.URL, data=invalid_seat_data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.post(self.URL, data=invalid_seat_data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_seat_by_id(self):
        seat_data = {
            "hall_id": self.hall1.id,
            "seating": Seat.SEATING[0][1],
            "is_free": True
        }

        self.client.post(self.URL, data=seat_data, format='json')
        id = list(Seat.objects.filter(hall=seat_data["hall_id"]).values_list('pk', flat=True))[0]

        response = self.client.delete(self.URL + str(id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
