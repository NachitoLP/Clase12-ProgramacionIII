from django.db import models
from ..departamentos.models import Departamento

from django_ckeditor_5.fields import CKEditor5Field

class Habilidades(models.Model):
    nombreHab = models.CharField('Habilidad', max_length=35, blank=True)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['nombreHab']
    
    def __str__(self):
        return f'{self.nombreHab}'


class Rol(models.Model):
    nombreRol = models.CharField('Rol', max_length = 40, blank=True)
    habilidadesRol = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name = 'Rol/Trabajo'
        verbose_name_plural = 'Roles/Trabajos'
        ordering = ['nombreRol']
    
    def __str__(self):
        return f'{self.nombreRol}'


class Empleado (models.Model):
    nombreEmp = models.CharField('Nombre del Empleado', max_length=20)
    apellidoEmp = models.CharField('Apellido del Empleado', max_length=20)
    rolEmp = models.ForeignKey(Rol,on_delete=models.SET_NULL, null=True,blank=True)
    departamentoEmp = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True,blank=True)
    fechaNac = models.DateField('Fecha de Nacimiento', default='2000-01-01')
    observaciones = CKEditor5Field(config_name='default', blank = True)
    
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellidoEmp','nombreEmp', 'rolEmp']

    def __str__(self):
        return f'{self.apellidoEmp} {self.nombreEmp} - {self.rolEmp}'