from django.db import models

class tunjanganKaryawan (models.Model) :
    tunjangan_makan = models.IntegerField()
    tunjangan_kesehatan = models.IntegerField()
    tunjangan_jabatan = models.IntegerField()
    THR = models.IntegerField()
    bonus = models.IntegerField()
