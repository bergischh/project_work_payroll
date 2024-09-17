from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from ..models.kehadirankaryawan_models import KehadiranKaryawan
from api.serializers import KehadiranKaryawanSerializer

@api_view(['GET'])
def getKehadiranKaryawan(request) :
    querySet = KehadiranKaryawan.objects.all()
    serializer = KehadiranKaryawanSerializer(querySet, many=True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postKehadiranKaryawan(request) :
    serializer = KehadiranKaryawanSerializer(data=request.data)
    if serializer.is_valid() : 
        serializer.save()
        return Response({
            "message" : "berhasil menambah data",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateKehadiranKaryawan(request, id) :
    kehadiran = get_object_or_404(KehadiranKaryawan, id=id)
    serializer = KehadiranKaryawanSerializer(kehadiran, data=request.data)
    if serializer.is_valid() : 
        serializer.save()
        return Response({
            "message" : "Berhasil mengubah data",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response ({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteKehadiranKaryawan(request, id) :
    kehadiran = get_object_or_404(KehadiranKaryawan, id=id)
    kehadiran.delete()
    return Response({
        "message" : "Berhasil menghapus data"
    }, status=status.HTTP_204_NO_CONTENT)