from django.db import models
from django.contrib.postgres.fields import ArrayField
from app_film.models import Film
from app_hall.models import Hall


# Create your models here.
class Schedule(models.Model):
    class Meta:
        db_table = "schedules"
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"

    std_price = models.IntegerField()
    rental_duration = models.DateField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
