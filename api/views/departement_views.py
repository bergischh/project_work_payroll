from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from api.serializers import DepartementSerializers
from ..models.departement_models import Departement

@api_view(['GET'])
def getdepartement(request) : 
    querySet = Departement.objects.all()
    serializer = DepartementSerializers(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def createdepartement(request) :
    serializer = DepartementSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Berhasil Menambah Departement",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def editDepartement(request, id) : 
    departemen = get_object_or_404(Departement, id=id)
    serializer = DepartementSerializers(departemen, data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response({
        "message" : "Berhasil mengedit data",
        "data" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) 
def deleteDepartement(request, id) : 
    departemen = get_object_or_404(Departement, id=id)
    departemen.delete()
    return Response({
        "message" : "Berhasil menghapus data"
    }, status=status.HTTP_204_NO_CONTENT)