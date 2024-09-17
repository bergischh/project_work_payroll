from django.db import models
from .user_models import Users
from .departement_models import Departement


class Karyawan(models.Model):
    class Role(models.TextChoices):
        admin = 'admin', 'Admin'
        manager = 'manager', 'Manager'
        karyawan = 'karyawan', 'Karyawan'
        calon_karyawan = 'calon_karyawan', 'Calon Karyawan'

    # role = models.CharField(max_length=50,choices=Role.choices,default=Role.calon_karyawan)
    id = models.AutoField(primary_key=True)
    nik = models.IntegerField()
    nama_karyawan = models.CharField(max_length=100)
    role = models.CharField(max_length=50,choices=Role.choices,default=Role.calon_karyawan)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    agama = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    jumlah_anak = models.IntegerField()
    alamat = models.CharField(max_length=100)
    no_telpon = models.IntegerField()
    email = models.CharField(max_length=100)
    jabatan = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='foto_karyawan/', null=True, blank=True)

    # relasi ke tabel users
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='karyawan', null=True, blank=True)

    # relasi ke tabel departement
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name='departement', null=True, blank=True)

    def __str__(self) -> str:
        return super().__str__(self) 
    