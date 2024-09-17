from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

from ..serializers import CalonKaryawanSerializers
from ..models.calonkaryawan_models import CalonKaryawan

@api_view(['GET'])
def getCalonKaryawan(request) :
    querySet = CalonKaryawan.objects.all()
    serializer = CalonKaryawanSerializers(querySet, many = True)

    return Response({
        "data": serializer.data
    })

@api_view(['POST'])
def createCalonKaryawan(request) :
    serializer = CalonKaryawanSerializers(data=request.data)
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
def editCalonKaryawan(request, id) :
    pewawancara = get_object_or_404(CalonKaryawan, id=id)
    serializer = CalonKaryawanSerializers(pewawancara, data=request.data)
    if serializer.is_valid() : 
        serializer.save()
        return Response({
            "message" : "Berhasil mengubah data",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)
    return Response({
        "errors" : serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCalonKaryawan(request, id) :
    pewawancara = get_object_or_404(CalonKaryawan, id=id)
    pewawancara.delete()
    return Response({
        "message" : "Data telah berhasil dihapus"
    }, status=status.HTTP_204_NO_CONTENT)
