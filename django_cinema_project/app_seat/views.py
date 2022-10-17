from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SeatSerializer
from .models import Seat


# Create your views here.
@api_view(['GET', 'POST'])
def get_post_seat(request):
    """
    Get list of all seats or create seat
    """
    if request.method == 'GET':
        seats = Seat.objects.all()
        serializer = SeatSerializer(seats, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_seat_by_id(request, pk):
    """
    Delete seat by id
    """
    try:
        seat = Seat.objects.get(pk=pk)
    except Seat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    seat.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)