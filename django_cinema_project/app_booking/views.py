from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Booking
from app_user.models import User
from app_seat.models import Seat
from app_schedule.models import Schedule
from .serializers import BookingSerializer


# Create your views here.
class BookingView(APIView):

    # get all bookings | booking by id
    def get(self, request, id=None):
        if id:
            booking = get_object_or_404(Booking.objects.all(), pk=id)
            serializer = BookingSerializer(booking, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # post new booking
    def post(self, request):
        requested_data = request.data
        try:
            user = get_object_or_404(User.objects.all(), pk=requested_data['user_id'])
            seat = get_object_or_404(Seat.objects.all(), pk=requested_data['seat_id'])
            schedule = get_object_or_404(Schedule.objects.all(), pk=requested_data['schedule_id'])
            Booking.create(price=requested_data["price"], user=user, schedule=schedule, seat=seat).save()
            return Response({'success': 'Object is created.'}, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)

    # delete booking by id
    def delete(self, request, id=None):
        booking = get_object_or_404(Booking.objects.all(), pk=id)
        booking.delete()
        return Response({'success': 'Object is deleted.'}, status=status.HTTP_204_NO_CONTENT)

