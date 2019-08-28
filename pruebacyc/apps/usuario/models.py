from django.db import models

# Create your models here.

class Contrato(models.Model):
    Contratos = (
        ('interno', 'Interno'),
        ('externo', 'Externo'),
    )
    tipoContrato = models.CharField(max_length=15, choices = Contratos)
    def __str__(self):
        return self.tipoContrato

class FichaUsuario(models.Model):
    rut     = models.CharField(max_length=8, blank=False, primary_key = True)
    dv = models.CharField(max_length=1)
    pNombre = models.CharField(max_length=30)
    sNombre = models.CharField(max_length=30)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    def __str__(self):
        return self.rut + ' ' + self.dv + ' ' + self.pNombre + ' ' + self.sNombre + ' ' + self.apPaterno + ' ' + self.apMaterno  