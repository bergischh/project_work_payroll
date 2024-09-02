from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from ..serializers import calonKaryawanSerializers
from ..models.calonkaryawan_models import calonKaryawan

class createCalonKaryawan(APIView) :
    serializer_class = calonKaryawanSerializers
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request) :
        request.user = calonKaryawan.objects.first()
        serializer = self.serializer_class(request.user, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)