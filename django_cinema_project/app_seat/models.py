from email.policy import default
from django.db import models
from django.db.models.enums import Choices
from app_hall.models import Hall


class Seat(models.Model):
    seating_types = (
        (1, 'vip_seating'),
        (2, 'classical_seating'),
        (3, 'kid_seating')
    )

    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seating = models.CharField(choices=seating_types, default=2, max_length=50)
    is_free = models.BooleanField(default=False)

    @classmethod
    def create(cls, hall, seating, is_free):
        return cls(hall=hall, seating=seating, is_free=is_free)
    
    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"hall id    : {self.hall.pk}\n" \
               f"seating    : {self.seating}\n" \
               f"is_free    : {self.is_free}"  