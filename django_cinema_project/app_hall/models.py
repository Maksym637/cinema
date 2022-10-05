from django.db import models
from app_seat.models import Seat


# Create your models here.
class Hall(models.Model):
    class Meta:
        db_table = "halls"
        verbose_name = "Зал"
        verbose_name_plural = "Залы"

    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    max_people = models.IntegerField()
    number = models.IntegerField()
