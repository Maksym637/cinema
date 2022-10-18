from rest_framework import serializers
from .models import Seat
from app_hall.serializers import HallSerializer


class SeatSerializer(serializers.ModelSerializer):

    hall = HallSerializer(many=False, read_only=True)

    class Meta:
        model = Seat
        fields = "__all__"
