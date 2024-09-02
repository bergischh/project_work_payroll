from django.db import models

class periodePenggajian(models.Model) :
    class status(models.TextChoices):
        active = 'active', 'Active'
        non_active = 'non_active', 'Non Active'
       

    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=status.choices, default=None)