from rest_framework import serializers
from .models import Schedule
from app_hall.serializers import HallSerializer
from app_film.serializers import FilmSerializer


class ScheduleSerializer(serializers.ModelSerializer):

    film = FilmSerializer(many=False, read_only=True)
    hall = HallSerializer(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'film', 'hall', 'time_start', 'time_end', 'date')
