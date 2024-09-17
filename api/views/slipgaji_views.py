from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.serializers import SlipGajiSerializer
from ..models.slipgaji_models import SlipGaji 

@api_view(['GET'])
def getSlipGaji(request) : 
    querySet = SlipGaji.objects.all()
    serializer = SlipGajiSerializer(querySet, data=request.data)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postSlipGaji(request) : 
    seriliazer = SlipGajiSerializer(data=request.data)
    if seriliazer.is_valid() : 
        seriliazer.save()
        return Response({
            "message" : "Berhasil menambah data",
            "data" : seriliazer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors" : seriliazer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateTransaksi(request, id) : 
    periode = get_object_or_404(SlipGaji, id=id)
    serializer = SlipGajiSerializer(periode, data=request.data)
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
def deletetransaksi(request, id) :
    pinjaman = get_object_or_404(SlipGaji, id=id)
    pinjaman.delete()
    return Response({
        "message" : "Data telah berhasil dihapus"
    }, status=status.HTTP_204_NO_CONTENT)