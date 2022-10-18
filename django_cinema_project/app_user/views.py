from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .models import User
from .serializers import UserSerializer
from bcrypt import hashpw, gensalt


class UserView(APIView):

    # get all users | user by username
    def get(self, request, username=None):
        if username:
            user = get_object_or_404(User.objects.all(), username=username)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    # create a new user
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            pwd = serializer.validated_data["password"].encode('utf-8')
            hashed_pwd = hashpw(pwd, gensalt())
            serializer.validated_data.update({"password": hashed_pwd})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # delete user by username
    def delete(self, request, username=None):
        user = get_object_or_404(User.objects.all(), username=username)
        user.delete()
        return Response({'success': 'Object is deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    # update user by username
    def put(self, request, username=None):
        user = get_object_or_404(User.objects.all(), username=username)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if "password" in serializer.validated_data:
                pwd = serializer.validated_data["password"].encode('utf-8')
                hashed_pwd = hashpw(pwd, gensalt())
                serializer.validated_data.update({"password": hashed_pwd})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
