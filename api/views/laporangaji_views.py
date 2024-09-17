from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from api.serializers import LaporanPenggajianSerializer
from ..models.laporanpenggajian_models import LaporanPenggajian

@api_view(['GET'])
def getLaporanGaji(request) :
    querySet = LaporanPenggajian.objects.all()
    serializer = LaporanPenggajianSerializer(querySet, many=True)

    return Response({
        "data" : serializer.data
    })

@api_view(['POST'])
def postLaporanGaji(request) :
    serilizer = LaporanPenggajianSerializer(data=request.data)
    if serilizer.is_valid() :
        serilizer.save()
        return Response({
            "message" : "Berhasil menambah data",
            "data" : serilizer.data
        }, status=status.HTTP_201_CREATED)
    return Response({
        "errors" : serilizer._errors
    },status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) 
def updateLaporanGaji(request, id) :
    laporan = get_object_or_404(LaporanPenggajian, id=id)
    serilizer = LaporanPenggajianSerializer(laporan, data=request.data)
    if serilizer.is_valid() :
        serilizer.save()
        return Response({
            "message" : "Berhasil mengedit data",
            "data" : serilizer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "erros" : serilizer._errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) 
def deleteLaporanGaji(request, id) :
    laporan = get_object_or_404(LaporanPenggajian, id=id)
    laporan.delete()
    return Response({
        "message" : "Berhasil menghapus data"
    }, status=status.HTTP_204_NO_CONTENT)