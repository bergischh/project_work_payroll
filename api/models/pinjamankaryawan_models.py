from django.db import models

class PinjamanKaryawan(models.Model) :

    id = models.AutoField(primary_key=True)
    jumlah_pinjaman = models.DecimalField(max_digits=12, decimal_places=2)
    tanggal_pinjaman = models.DateField()
    tenggat_pinjam = models.DateField()