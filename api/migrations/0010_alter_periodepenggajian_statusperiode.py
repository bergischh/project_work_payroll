# Generated by Django 5.1 on 2024-09-03 06:31

import api.models.periodGaji_models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_status_periodepenggajian_statusperiode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodepenggajian',
            name='statusPeriode',
            field=models.CharField(choices=[('active', 'Active'), ('non_active', 'Non Active')], default=api.models.periodGaji_models.periodePenggajian.Status, max_length=50),
        ),
    ]
