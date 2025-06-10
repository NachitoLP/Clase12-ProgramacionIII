from django.db import models

# Create your models here.

class Departamento (models.Model):
    nombreDto = models.CharField('Departamento',max_length=50,blank=True)
    siglaDto = models.CharField('Sigla', max_length=4, unique=True)
    isActivo = models.BooleanField('¿Está activo?', default=False)
    pisoDto = models.CharField('Piso', max_length=5, blank=True)
    oficinaDto = models.CharField('Oficina N°', max_length=10, blank=True)
    
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['siglaDto']
        # unique_together = ('nombreDto','siglaDto')
    
    def __str__(self):
        return f'{self.siglaDto} - {self.nombreDto}'
