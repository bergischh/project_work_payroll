from django.db import models

class Departement(models.Model) :
    id = models.AutoField(primary_key=True)
    nama_departement = models.CharField(max_length=100)
