from django.db import models


class Hall(models.Model):
    class Meta:
        db_table = "halls"

    number = models.IntegerField()
    max_people_count = models.IntegerField()

    @classmethod
    def create(cls, number, max_people_count):
        return cls(number=number, max_people_count=max_people_count)
    
    def __str__(self):
        return f"id               : {self.pk}\n" \
               f"number           : {self.number}\n" \
               f"max_people_count : {self.max_people_count}"