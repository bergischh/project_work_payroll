from django.db import models

class calonKaryawan(models.Model) : 
    class JenisKelamin(models.TextChoices) :
        laki_laki = 'laki_laki', 'Laki Laki'
        perempuan = 'perempuan', 'Perempuan'
        
    class Status(models.TextChoices) : 
        kawin = 'kawin', 'Kawin'
        belum_kawin = 'belum_kawin', 'Belum Kawin'

    class StatusWawancara(models.TextChoices):
        diterima = 'diterima', 'Diterima'
        tidak_diterima = 'tidak_diterima', 'Tidak Diterima'

    nik = models.IntegerField()
    nama_karyawan = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10, choices=JenisKelamin.choices, default=None)
    agama = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=Status.choices, default=None)
    jumlah_anak = models.CharField(max_length=50)
    alamat = models.CharField(max_length=100)
    no_telephone = models.IntegerField()
    photo = models.ImageField(upload_to='images_profile/', null=True, blank=True)
    ktp = models.FileField(upload_to='ktp_pdf/', null=True, blank=True)
    ijazah = models.FileField(upload_to='ijazah_pdf/', null=True, blank=True)
    status_wawancara = models.CharField(max_length=20, choices=StatusWawancara.choices, default=None)
    upload_at = models.DateTimeField(null=True, blank=True)
    
     # relasi ke tabel karyawan
    user = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='calon_karyawan', null=True, blank=True)
 



    def __str__(self) :
        return self.nama_karyawan

