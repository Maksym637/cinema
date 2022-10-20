from rest_framework.test import APITestCase
from rest_framework import status
from app_user.models import User


class USerViewTest(APITestCase):
    URL = '/user/'

    def test_get_all_users(self):
        response = self.client.get(self.URL, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_by_id(self):
        user_data = {
            "username": "u1",
            "first_name": "u1",
            "last_name": "u1",
            "email": "u1",
            "password": "u1",
            "phone": "2222",
            "is_admin": False
        }

        self.client.post(self.URL, data=user_data, format='json')

        username = list(User.objects.filter(username=user_data["username"]).values_list('username', flat=True))[0]
        response = self.client.get(self.URL + username + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.URL + 'u2/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_user(self):
        valid_user_data = {
            "username": "u2",
            "first_name": "u2",
            "last_name": "u2",
            "email": "u2",
            "password": "u2",
            "phone": "1111",
            "is_admin": False
        }

        invalid_user_data = {
            "username": "u2",
            "first_name": "u2",
            "last_name": "u2",
            "email": "u2",
            "password": "u2",
            "phone": "1111",
            "is_admin": "Hello"
        }

        response = self.client.post(self.URL, data=valid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(self.URL, data=invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_user(self):
        user_data = {
            "username": "u3",
            "first_name": "u3",
            "last_name": "u3",
            "email": "u3",
            "password": "u3",
            "phone": "3333",
            "is_admin": False
        }

        self.client.post(self.URL, data=user_data, format='json')
        username = list(User.objects.filter(username=user_data["username"]).values_list('username', flat=True))[0]

        valid_user_data_update = {
            "password": "4444"
        }

        response = self.client.put(self.URL + username+ '/', data=valid_user_data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        invalid_user_data_update = {
            "is_admin": "4444"
        }

        response = self.client.put(self.URL + username + '/', data=invalid_user_data_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_user(self):
        user_data = {
            "username": "u1",
            "first_name": "u1",
            "last_name": "u1",
            "email": "u1",
            "password": "u1",
            "phone": "2222",
            "is_admin": False
        }

        self.client.post(self.URL, data=user_data, format='json')
        username = list(User.objects.filter(username=user_data["username"]).values_list('username', flat=True))[0]

        response = self.client.delete(self.URL + username + '/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.delete(self.URL + 'u100/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
