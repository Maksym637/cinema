from django.db import models
from django_enumfield import enum


class Languages(enum.Enum):
    ENG, SPA, FRE, UKR = 1, 2, 3, 4

    __labels__ = {
        ENG: 'English',
        SPA: 'Spanish',
        FRE: 'French',
        UKR: 'Ukrainian'
    }


class Genres(enum.Enum):
    ACTION, COMEDY, DRAMA, FANTASY, HORROR = 1, 2, 3, 4, 5

    __labels__ = {
        ACTION: 'Action',
        COMEDY: 'Comedy',
        DRAMA: 'Drama',
        FANTASY: 'Fantasy',
        HORROR: 'Horror'
    }


class Film(models.Model):
    class Meta:
        db_table = "films"
        ordering = ['year']

    name = models.CharField(max_length=100)
    genre = enum.EnumField(Genres, default=Genres.ACTION)
    language = enum.EnumField(Languages, default=Languages.ENG)
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
               f"image url  : {self.image}\n" \
               f"year       : {self.year}\n" \
               f"rate       : {self.rate}"