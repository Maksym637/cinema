from django.db import models


# Create your models here.
class Seat(models.Model):
    class Meta:
        db_table = "seats"
        verbose_name = "Сиденье"
        verbose_name_plural = "Сиденья"

    VIP = 'VIP'
    STANDARD = 'STD'
    SEAT_CHOICES = [
        (VIP, 'VIP'),
        (STANDARD, 'Standard')
    ]

    seat_type = models.CharField(max_length=3, choices=SEAT_CHOICES, default=STANDARD)
    is_free = models.BooleanField(default=True)

