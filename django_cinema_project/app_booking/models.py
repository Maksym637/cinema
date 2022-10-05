from django.db import models
from app_user.models import User
from app_seat.models import Seat
from app_schedule.models import Schedule


# Create your models here.
class Booking(models.Model):
    class Meta:
        db_table = "bookings"
        verbose_name = "Бронь"
        verbose_name_plural = "Бронирование"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
