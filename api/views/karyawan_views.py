from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import KaryawanSerializers
from ..models.karyawan_models import Karyawan
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class karyawanViewSet(viewsets.ModelViewSet):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializers

@api_view(['GET'])
def getKaryawan(request) :
    querySet = Karyawan.objects.all()
    serializer = KaryawanSerializers(querySet, many = True)

    return Response({
        "data": serializer.data
    })

@api_view(['POST'])
def createKaryawan(request) :
    serializer = KaryawanSerializers(data=request.data)
    parser_classes = [MultiPartParser, FormParser]
    if serializer.is_valid() :
        serializer.save()
        return Response({
            "message" : "Berhasil menambah data",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def editKaryawan(request, id) : 
    dataKaryawan = get_object_or_404(Karyawan, id=id)
    serializer = KaryawanSerializers(dataKaryawan, data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response({
            "massage": "Berhasil mengubah data",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteKaryawan(request, id):
    Karyawan = get_object_or_404(Karyawan, id=id)
    Karyawan.delete()
    return Response({
        "message": "User deleted successfully"
    }, status=status.HTTP_204_NO_CONTENT)