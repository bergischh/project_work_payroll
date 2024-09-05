from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models.tunjangan_models import tunjanganKaryawan
from api.serializers import tunjanganSerializers

@api_view(['GET'])
def getTunjangan(request) :
    querySet = tunjanganKaryawan.objects.all()
    serializer = tunjanganSerializers(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postTunjangan(request) :
    serializer = tunjanganSerializers(data=request.data)
    if serializer.is_valid() :
        serializer.save()
        return Response({
            "message": "Berhasil menambah periode penggajian",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors": serializer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def editTunjangan(request, id) : 
    periode = get_object_or_404(tunjanganKaryawan, id=id)
    serializer = tunjanganSerializers(periode, data=request.data)
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
def deleteTunjangan(request, id) :
    periode = get_object_or_404(tunjanganKaryawan, id=id)
    periode.delete()
    return Response({
        "massage": "Berhasil hapus data",
    }, status=status.HTTP_204_NO_CONTENT)