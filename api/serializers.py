from rest_framework import serializers
from .models.user_models import Users
from .models.calonkaryawan_models import calonKaryawan
from .models.departement_models import departement
from .models.karyawan_models import karyawan
from .models.periodGaji_models import periodePenggajian
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
        return super().update(instance, self.validated_data)
    
class karyawanSerializers(serializers.ModelSerializer) :
    class Meta :
        model = karyawan
        fields = '__all__'

    def update(self, instance, validate_data) :
        instance.role = validate_data.get('role', instance.role)
        instance.nik = validate_data.get('nik', instance.nik)
        instance.nama_karyawan = validate_data('nama_karyawan', instance.nama_karyawan)
        instance.tempat_lahir = validate_data('tempat_lahir', instance.tempat_lahir)
        instance.tanggal_lahir = validate_data('tanggal_lahir', instance.tanggal_lahir)
        instance.agama = validate_data('agama', instance.agama)
        instance.status = validate_data('status', instance.status)
        instance.jumlah_anak = validate_data('jumlah_anak', instance.jumlah_anak)
        instance.alamat = validate_data('alamat', instance.alamat)
        instance.no_telpon = validate_data('no_telpon', instance.no_telpon)
        instance.email = validate_data('email', instance.email)
        instance.jabatan = validate_data('jabatan', instance.jabatan)
        instance.foto = validate_data('foto', instance.foto)
            
        return instance
    
class DepartementSerializers(serializers.ModelSerializer) :
        class Meta : 
            model = departement
            fields = [
                'nama_departement'
            ]

        def update(self, instance, validate_data) :
            instance.nama_departement = validate_data.get('nama_departement', instance.nama_departement)
            return instance
        
class PeriodeGajiSerializers(serializers.ModelSerializer) :
    class Meta : 
        model = periodePenggajian 
        fields = '__all__'
    
    def create(self, validated_data):
        # Jangan gunakan nama kelas sebagai nama variabel
        periode = periodePenggajian(
            start_date=validated_data['start_date'],
            end_date=validated_data['end_date'],
            status_periode=validated_data.get('statusPeriode', periodePenggajian.Status.non_active)
        )
        periode.save()
        return periode

        
