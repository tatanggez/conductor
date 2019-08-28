from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tvehiculo(models.Model):
    tipos = (
        ('Auto', 'CyC L'),
        ('Van', 'CyC XL'),
    )
    tipovehiculo = models.CharField(max_length=15, choices = tipos)
    def __str__(self):
        return self.tipovehiculo

class Tlicencia(models.Model):
    licencias = (
        ('Licencia A', 'A'),
        ('Licencia B', 'B'),
    )
    tipolicencia = models.CharField(max_length=15, choices = licencias)
    def __str__(self):
        return self.tipolicencia

class FichaConductor(models.Model):
    rut     = models.CharField(max_length=9, blank=False, primary_key = True)
    pNombre = models.CharField(max_length=30)
    sNombre = models.CharField(max_length=30)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    fNacimiento = models.DateField()
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=9)
    licencia = models.ForeignKey(Tlicencia, on_delete=models.CASCADE)
    Vehiculo = models.ForeignKey(Tvehiculo, on_delete=models.CASCADE)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.rut + ' ' + self.pNombre + ' ' + self.sNombre + ' ' + self.apPaterno + ' ' + self.apMaterno + ' ' + self.direccion
