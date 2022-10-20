from rest_framework.test import APITestCase
from rest_framework import status
from app_hall.models import Hall
from app_film.models import Film
from app_user.models import User
from app_seat.models import Seat
from app_schedule.models import Schedule
from app_booking.models import Booking


class BookingViewTest(APITestCase):
    URL = '/booking/'

    def setUp(self):
        self.hall1 = Hall.create(1, 50)
        self.hall2 = Hall.create(2, 50)
        self.hall1.save()
        self.hall2.save()

        self.film1 = Film.create('Interstellar', 'science-fiction', 'ua', None, '2012-10-10', 10)
        self.film2 = Film.create('Avatar', 'science-fiction', 'ua', None, '2021-10-10', 9)
        self.film1.save()
        self.film2.save()

        self.seat1 = Seat.create(self.hall1, Seat.SEATING[0][0], True)
        self.seat2 = Seat.create(self.hall2, Seat.SEATING[1][0], False)
        self.seat1.save()
        self.seat2.save()

        self.schedule1 = Schedule.create(self.film1, self.hall1, "16:00:00", "17:30:00", "2022-10-24")
        self.schedule2 = Schedule.create(self.film2, self.hall2, "10:00:00", "12:00:00", "2022-10-10")
        self.schedule1.save()
        self.schedule2.save()

        self.user1 = User.create('user1', 'u1fn', 'u1ln', 'u1@text.com', 'hello world1', '11111', False)
        self.user2 = User.create('user2', 'u2fn', 'u2ln', 'u2@text.com', 'hello world2', '22222', False)
        self.user1.save()
        self.user2.save()

    def test_get_all_bookings(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_booking_by_id(self):
        booking_data = {
            "price": 100,
            "user_id": self.user1.id,
            "seat_id": self.seat1.id,
            "schedule_id": self.schedule1.id
        }

        self.client.post(self.URL, data=booking_data, format='json')

        id = list(Booking.objects.filter(price=booking_data["price"]).values_list('pk', flat=True))[0]
        response = self.client.get(self.URL + str(id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["price"], booking_data["price"])

        response = self.client.get(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_booking(self):
        valid_booking_data = {
            "price": 50,
            "user_id": self.user2.id,
            "seat_id": self.seat2.id,
            "schedule_id": self.schedule1.id
        }

        invalid_booking_data1 = {
            "price": 100,
            "user_id": 1000,
            "seat_id": self.seat2.id,
            "schedule_id": self.schedule1.id
        }

        invalid_booking_data2 = {
            "price": "asd",
            "user_id": self.user1.id,
            "seat_id": self.seat2.id,
            "schedule_id": self.schedule1.id
        }

        response = self.client.post(self.URL, data=valid_booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.URL, data=invalid_booking_data1, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.post(self.URL, data=invalid_booking_data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_booking_by_id(self):
        booking_data = {
            "price": 100,
            "user_id": self.user1.id,
            "seat_id": self.seat1.id,
            "schedule_id": self.schedule1.id
        }

        self.client.post(self.URL, data=booking_data, format='json')
        id = list(Booking.objects.filter(price=booking_data["price"]).values_list('pk', flat=True))[0]

        response = self.client.delete(self.URL + str(id) + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.URL + '1000/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)