from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from bcrypt import hashpw, checkpw, gensalt


@api_view(['POST', 'GET'])
def post_user(request):
    """
    Create user
    """
    if request.method == 'GET':
        seats = User.objects.all()
        serializer = UserSerializer(seats, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            pwd = serializer.validated_data["password"].encode('utf-8')
            hashed_pwd = hashpw(pwd, gensalt())
            serializer.validated_data.update({"password": hashed_pwd})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, username):
    """
    Get or change user details
    """
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if "password" in serializer.validated_data:
                pwd = serializer.validated_data["password"].encode('utf-8')
                hashed_pwd = hashpw(pwd, gensalt())
                serializer.validated_data.update({"password": hashed_pwd})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
