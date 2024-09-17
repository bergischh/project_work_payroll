from django.db import models
from .user_models import Users
from .tunjangan_models import tunjanganKaryawan
from .periodGaji_models import periodePenggajian

class LaporanPenggajian(models.Model) :
    
    id = models.AutoField(primary_key=True)
    tanggal_gaji = models.DateField()
    gaji_mentah = models.DecimalField(max_digits=12, decimal_places=2)
    pinjaman = models.DecimalField(max_digits=12, decimal_places=2)
    gaji_total = models.DecimalField(max_digits=12, decimal_places=2)
    jumlah_izin = models.IntegerField()
    jumlah_sakit = models.IntegerField()

    # relasi ke tabel user
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='laporanpenggajian', null=True, blank=True)

    # relasi ke tabel tunjangan
    tunjangan = models.ForeignKey(tunjanganKaryawan, on_delete=models.CASCADE, related_name='laporanpenggajian', null=True, blank=True)

    # relasi ke tabel periode penggajian 
    periodegaji = models.ForeignKey(periodePenggajian, on_delete=models.CASCADE, related_name='laporanpenggajian', null=True, blank=True)


    