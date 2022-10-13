from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hall
from .serializers import HallSerializer


class HallView(APIView):

    # get all halls
    def get(self, request, id=None):
        if id:
            if Hall.objects.filter(pk=id).exists():
                hall = Hall.objects.get(pk=id)
                serializer = HallSerializer(hall, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'FATAL': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)
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
        return Response({'FATAL': 'Incorrect input'}, status=status.HTTP_400_BAD_REQUEST)

    # delete hall by id
    def delete(self, request, id=None):
        if Hall.objects.filter(pk=id).exists():
            hall = Hall.objects.get(pk=id)
            hall.delete()
            return Response({'SUCCESS': 'Object is deleted'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'FATAL': 'Object not found'}, status=status.HTTP_404_NOT_FOUND) 
