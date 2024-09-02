from ..models.user_models import Users
from rest_framework.response import Response
from api.serializers import DepartementSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

@api_view(['GET'])
def getdepartement(request) : 
    querySet = Users.objects.all()
    serializer = DepartementSerializers(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def createdepartement(request) :
    serializer = DepartementSerializers(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Berhasil Menambah Departement",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)