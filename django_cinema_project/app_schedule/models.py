from django.db import models
from app_film.models import Film
from app_hall.models import Hall


class Schedule(models.Model):
    class Meta:
        db_table = 'schedules'
        ordering = ['date']

    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    time_start = models.TimeField()
    time_end = models.TimeField()
    date = models.DateField()

    @classmethod
    def create(cls, film, hall, time_start, time_end, date):
        return cls(film=film, hall=hall, time_start=time_start, time_end=time_end, date=date)
    
    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"film id    : {self.film.pk}\n" \
               f"hall id    : {self.hall.pk}\n" \
               f"start time : {self.time_start}\n" \
               f"end time   : {self.time_end}\n" \
               f"date       : {self.date}"
