from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..models.periodGaji_models import periodePenggajian
from api.serializers import PeriodeGajiSerializers

@api_view(['GET'])
def getPeriodeGaji(request) :
    querySet = periodePenggajian.objects.all()
    serializer = PeriodeGajiSerializers(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postPeriodeGaji(request) :
    serializer = PeriodeGajiSerializers(data=request.data)
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
def editPeriodeGaji(request, id) : 
    periode = get_object_or_404(periodePenggajian, id=id)
    serializer = PeriodeGajiSerializers(periode, data=request.data)
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
def deletePeriodeGaji(request, id) :
    periode = get_object_or_404(periodePenggajian, id=id)
    periode.delete()
    return Response({
        "massage": "Berhasil hapus data",
    }, status=status.HTTP_204_NO_CONTENT)