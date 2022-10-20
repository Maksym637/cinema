from django.db import models
from app_user.models import User
from app_schedule.models import Schedule
from app_seat.models import Seat


class Booking(models.Model):
    class Meta:
        db_table = 'bookings'

    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

    @classmethod
    def create(cls, price, user, seat, schedule):
        return cls(price=price, user=user, seat=seat, schedule=schedule)
    
    def __str__(self):
        return f"id          : {self.pk}\n" \
               f"price       : {self.price}\n" \
               f"user id     : {self.user.pk}\n" \
               f"seat id     : {self.seat.pk}\n" \
               f"schedule id : {self.schedule.pk}\n"
