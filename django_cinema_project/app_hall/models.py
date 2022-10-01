from django.db import models


class Hall(models.Model):

    number = models.IntegerField()
    max_people = models.IntegerField()

    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"number     : {self.number}\n" \
               f"max_people : {self.max_people}\n"
