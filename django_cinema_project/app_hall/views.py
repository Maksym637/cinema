from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Hall
from .serializers import HallSerializer


class HallView(APIView):

    # get all halls | hall by id
    def get(self, request, id=None):
        if id:
            hall = get_object_or_404(Hall.objects.all(), pk=id)
            serializer = HallSerializer(hall, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            hall = Hall.objects.all()
            serializer = HallSerializer(hall, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new hall
    def post(self, request):
        hall = HallSerializer(data=request.data)
        if hall.is_valid():
            hall.save()
            return Response(hall.data, status=status.HTTP_201_CREATED)   
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)

    # delete hall by id
    def delete(self, request, id=None):
        hall = get_object_or_404(Hall.objects.all(), pk=id)
        hall.delete()
        return Response({'success': 'Object is deleted.'}, status=status.HTTP_204_NO_CONTENT)
