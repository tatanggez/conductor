from django.db import models

class Ubicacion(models.Model):
    lat = models.DecimalField(max_digits=50, decimal_places=20)
    lng = models.DecimalField(max_digits=50, decimal_places=20)
    fecha = models.DateField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)

class UbicacionFinal(models.Model):
	lat = models.DecimalField(max_digits=50, decimal_places=20)
	lng = models.DecimalField(max_digits=50, decimal_places=20)
	fecha = models.DateField(auto_now_add=True)
	hora = models.TimeField(auto_now_add=True)
# Create your models here.
