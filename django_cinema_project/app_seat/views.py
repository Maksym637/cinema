from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from app_hall.models import Hall
from .models import Seat
from .serializers import SeatSerializer


class SeatView(APIView):

    # get all seats
    def get(self, request):
        seat = Seat.objects.all()
        serializer = SeatSerializer(seat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new seat
    def post(self, request):
        request_data = request.data
        is_free = request_data['is_free']
        hall = get_object_or_404(Hall.objects.all(), pk=request_data['hall_id'])

        try:
            Seat.create(hall, Seat.SEATING[1][0], is_free).save()
            return Response({'success': 'Object is created.'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)

    # delete seat by id
    def delete(self, request, id=None):
        seat = get_object_or_404(Seat.objects.all(), pk=id)
        seat.delete()
        return Response({'success': 'Object is deleted.'}, status=status.HTTP_204_NO_CONTENT)