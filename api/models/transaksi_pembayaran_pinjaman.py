from django.db import models

from .pinjamankaryawan_models import PinjamanKaryawan

class TransaksiPinjaman : 
    id = models.AutoField(primary_key=True)
    tanggal_pembayaran = models.DateField()
    jumlah_pembayaran = models.DecimalField(max_digits=12, decimal_places=2)

    # Relasi ke tabel pinjaman karyawan
    pinjaman_karyawan = models.ForeignKey(PinjamanKaryawan, on_delete=models.CASCADE, related_name='transaksipembayaranpinjaman', null=True, blank=True)