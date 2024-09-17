from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from api.serializers import PinjamanKaryawanSerializer
from ..models.pinjamankaryawan_models import PinjamanKaryawan

@api_view(['GET'])
def getPinjamanKaryawan(request) :
    querySet = PinjamanKaryawan.objects.all()
    serializer  = PinjamanKaryawanSerializer(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postPinjaman(request) :
    serializer = PinjamanKaryawanSerializer(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response({
            "message" : "Berhasil menambah data",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response ({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updatePinjaman(request, id) : 
    pinjaman = get_object_or_404(PinjamanKaryawan, id=id)
    serializer = PinjamanKaryawanSerializer(pinjaman, data=request)
    if serializer.is_valid() : 
        serializer.save()
        return Response({
            "message" : "Berhasil mengubah data",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors" : serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletePinjaman(request, id) :
    pinjaman = get_object_or_404(PinjamanKaryawan, id=id)
    pinjaman.delete()
    return Response({
        "message" : "Data telah berhasil dihapus"
    }, status=status.HTTP_204_NO_CONTENT)
