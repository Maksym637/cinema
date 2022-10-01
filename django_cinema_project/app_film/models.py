from django.db import models


class Film(models.Model):

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    languange = models.CharField(max_length=50)
    year = models.DateTimeField()
    rate = models.IntegerField()

    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"name       : {self.name}\n" \
               f"genre      : {self.genre}\n" \
               f"language   : {self.languange}\n" \
               f"year       : {self.year}\n" \
               f"rate       : {self.rate}\n"
