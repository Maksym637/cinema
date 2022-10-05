from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Film(models.Model):
    class Meta:
        db_table = "films"
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    year = models.IntegerField()
    rate = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    duration = models.IntegerField()
    time = ArrayField(models.DateTimeField())
