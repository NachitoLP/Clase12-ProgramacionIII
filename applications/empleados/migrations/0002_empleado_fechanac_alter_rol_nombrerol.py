# Generated by Django 5.2 on 2025-04-29 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='fechaNac',
            field=models.DateField(default='2000-01-01', verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombreRol',
            field=models.CharField(blank=True, max_length=20, verbose_name='Rol'),
        ),
    ]
