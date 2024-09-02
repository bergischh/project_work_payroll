from rest_framework import serializers
from .models.user_models import Users
from .models.calonkaryawan_models import calonKaryawan
from .models.departement_models import departement
from django.utils import timezone

class UsersSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Users
        fields = [
            "user_id",
            "username",
            "role", 
            "email",
            "password",
        ]
    
    def create(self, validated_data):
        user = Users(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', Users.Role.CALON_KARYAWAN)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validate_data) :
        instance.username = validate_data.get('username', instance.username)
        instance.email = validate_data.get('email', instance.email)
        instance.role = validate_data.get('role', instance.role)
        password = validate_data.get('password')
        if password : 
            instance.set_password(password)
            instance.save()
        return instance
    

class calonKaryawanSerializers(serializers.ModelSerializer) :
    upload_at = serializers.DateTimeField(read_only=True)
    class Meta :
        model = calonKaryawan
        fields = '__all__'

    def update(self, instance, validate_data) :
        instance.upload_at = timezone.now()
        return super().update(instance, validated_data)
    
class DepartementSerializers(serializers.ModelSerializer) :
        class Meta : 
            model = departement
            fields = [
                'nama_departement'
            ]

        def update(self, instance, validate_data) :
            instance.nama_departement = validate_data.get('nama_departement', instance.nama_departement)
            return instance