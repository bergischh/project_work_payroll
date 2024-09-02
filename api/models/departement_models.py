from django.db import models

class departement(models.Model) :
    nama_departement = models.CharField(max_length=100)
