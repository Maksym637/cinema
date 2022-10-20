from django.db import models


class Film(models.Model):
    class Meta:
        db_table = 'films'
        ordering = ['year']

    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    year = models.DateField()
    rate = models.IntegerField()

    @classmethod
    def create(cls, name, genre, language, image, year, rate):
        return cls(name=name, genre=genre, language=language, image=image, year=year, rate=rate)

    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"name       : {self.name}\n" \
               f"genre      : {self.genre}\n" \
               f"language   : {self.language}\n" \
               f"image url  : {self.image.url}\n" \
               f"year       : {self.year}\n" \
               f"rate       : {self.rate}"
