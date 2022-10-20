from rest_framework import serializers
from .models import Booking
from app_user.serializers import UserSerializer
from app_seat.serializers import SeatSerializer
from app_schedule.serializers import ScheduleSerializer


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    seat = SeatSerializer(many=False, read_only=True)
    schedule = ScheduleSerializer(many=False, read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
