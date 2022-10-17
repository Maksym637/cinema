from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Film
from .serializers import FilmSerializer


class FilmView(APIView):

    # get all films | film by id
    def get(self, request, id=None):
        if id:
            film = get_object_or_404(Film.objects.all(), pk=id)
            serializer = FilmSerializer(film, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            film = Film.objects.all()
            serializer = FilmSerializer(film, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new film
    def post(self, request):
        film = FilmSerializer(data=request.data)
        if film.is_valid():
            film.save()
            return Response(film.data, status=status.HTTP_201_CREATED)
        return Response({'detail': 'Incorrect input.'}, status=status.HTTP_400_BAD_REQUEST)

    # delete film by id
    def delete(self, request, id=None):
        film = get_object_or_404(Film.objects.all(), pk=id)
        film.delete()
        return Response({'success': 'Object is deleted'}, status=status.HTTP_204_NO_CONTENT)

"""
Add resizing of image !
"""
