from django.db import models
from django.contrib.auth.hashers import make_password

class Users(models.Model):
    class Role(models.TextChoices):
        admin = 'admin', 'Admin'
        manager = 'manager', 'Manager'
        karyawan = 'karyawan', 'Karyawan'
        calon_karyawan = 'calon_karyawan', 'Calon Karyawan'

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=50,choices=Role.choices,default=Role.calon_karyawan)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=200)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
