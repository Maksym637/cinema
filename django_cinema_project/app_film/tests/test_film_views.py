from rest_framework.test import APITestCase
from rest_framework import status


class FilmViewTest(APITestCase):
    URL = '/film/'
    FILM_DATA_CORRECT = {"name": "name1", "genre": 'Comedy', "language": 'English', "image": None, "year": "2020-10-10", "rate": 3}
    FILM_DATA_INCORRECT = {"name": "name2", "genre": "genre2", "language": "language2", "image": None, "year": 10, "rate": 10}

    def test_get_films(self):
        responce = self.client.get(self.URL, format='json')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_get_film(self):
        create = self.client.post(self.URL, data=self.FILM_DATA_CORRECT, format='json')

        responce = self.client.get(self.URL + str(create.data["id"]) + '/', format='json')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertEqual(responce.data["name"], "name1")

        responce = self.client.get(self.URL + '1000/', format='json')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_film(self):
        responce = self.client.post(self.URL, data=self.FILM_DATA_CORRECT, format='json')
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(responce.data["rate"], 3)

        responce = self.client.post(self.URL, data=self.FILM_DATA_INCORRECT, format='json')
        self.assertEqual(responce.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_film(self):
        create = self.client.post(self.URL, data=self.FILM_DATA_CORRECT, format='json')

        responce = self.client.delete(self.URL + str(create.data["id"]) + '/', format='json')
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)

        responce = self.client.delete(self.URL + '1000/', format='json')
        self.assertEqual(responce.status_code, status.HTTP_404_NOT_FOUND)
