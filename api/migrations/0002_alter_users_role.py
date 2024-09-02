# Generated by Django 5.1 on 2024-08-16 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('karyawan', 'Karyawan'), ('calon_karyawan', 'Calon Karyawan')], default='calon_karyawan', max_length=100),
        ),
    ]
