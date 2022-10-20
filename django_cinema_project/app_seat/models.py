from django.db import models
from app_hall.models import Hall


class Seat(models.Model):
    class Meta:
        db_table = 'seats'

    VIP = 'vip seating'
    CLS = 'classical seating'
    KID = 'kid seating'

    SEATING = (
        (VIP, 'vip seating'),
        (CLS, 'classical seating'),
        (KID, 'kid seating')
    )

    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    seating = models.CharField(max_length=50, choices=SEATING, default=CLS)
    is_free = models.BooleanField(default=False)
    
    @classmethod
    def create(cls, hall, seating, is_free):
        return cls(hall=hall, seating=seating, is_free=is_free)
    
    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"hall id    : {self.hall.pk}\n" \
               f"seating    : {self.seating}\n" \
               f"is_free    : {self.is_free}"
