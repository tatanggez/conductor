from django.db import models

# Create your models here.

class Canal(models.Model):
    Canales = (
        ('Casa', 'Interno'),
        ('depa', 'Externo'),
        ('ajja', 'Go'),
    )
    tipoCanal = models.CharField(max_length=15, choices = Canales)
    def __str__(self):
        return self.tipoCanal
class FichaCliente(models.Model):
    rut     = models.CharField(max_length=9, blank=False, primary_key = True)
    pNombre = models.CharField(max_length=30)
    sNombre = models.CharField(max_length=30)
    apPaterno = models.CharField(max_length=30)
    apMaterno = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    fNacimiento = models.DateField()
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=9)
    Centro = models.ForeignKey(Canal, on_delete=models.CASCADE)
    def __str__(self):
        return self.rut + ' ' + self.pNombre + ' ' + self.sNombre + ' ' + self.apPaterno + ' ' + self.apMaterno + ' ' + self.direccion 