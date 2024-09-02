from django.shortcuts import get_object_or_404

# Create your views here.
from ..models.user_models import Users
from rest_framework.response import Response
from api.serializers import UsersSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

@api_view(['GET'])
def getUsers(request) : 
    querySet = Users.objects.all()
    serializer = UsersSerializer(querySet, many = True)

    return Response({
        "data" : serializer.data
    })


@api_view(['POST'])
def register(request) :
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Berhasil Menambah User",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request) :
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password :
        return Response({
            "error": "Username atauu Password salah, silahkan coba lagi"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    user = get_object_or_404(Users, username=username)

    if user.check_password(password):
        return Response({
            "message": "Login Berhasil",
            "user": UsersSerializer(user).data
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            "error": "Terjadi Kesalahan"
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    
@api_view(['PUT'])
def updateUser(request, user_id) :
    user = get_object_or_404(Users, user_id=user_id)
    serializer =    UsersSerializer(user, data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response({
            "message" : "User Berhasil di Update",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def PartialUpdateUser(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)
    serializer = UsersSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "User partially updated successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteUser(request, user_id):
    user = get_object_or_404(Users, user_id=user_id)
    user.delete()
    return Response({
        "message": "User deleted successfully"
    }, status=status.HTTP_204_NO_CONTENT)