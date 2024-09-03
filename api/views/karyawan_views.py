from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from api.serializers import karyawanSerializers
from ..models.karyawan_models import karyawan

class createKaryawan(APIView) :
    serializer_class = karyawanSerializers
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request) :
        request.user = karyawan.objects.first()
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)