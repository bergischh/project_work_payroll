from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.transaksi_pembayaran_pinjaman import TransaksiPinjaman
from api.serializers import TransaksiPinjamanSerializers

@api_view(['GET'])
def getTransaksi(request) :
    querySet = TransaksiPinjaman.objects.all()
    serializer  = TransaksiPinjamanSerializers(querySet, many = True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postTransaksi(request) : 
    serializer = TransaksiPinjamanSerializers(data=request.data)
    if serializer.is_valid() : 
        serializer.save()
        return Response({
            "message" : "Data berhasil ditambahkan",
            "data" : serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateTransaksi(request, id) : 
    periode = get_object_or_404(TransaksiPinjaman, id=id)
    serializer = TransaksiPinjamanSerializers(periode, data=request.data)
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
    pinjaman = get_object_or_404(TransaksiPinjaman, id=id)
    pinjaman.delete()
    return Response({
        "message" : "Data telah berhasil dihapus"
    }, status=status.HTTP_204_NO_CONTENT)