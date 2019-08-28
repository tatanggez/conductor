from django.db import models
# Create your models here.



class Comuna(models.Model):
    Comuna = (
        ('Peñalolen', 'Peñalolen'),
        ('La Reina', 'La Reina'),
        ('Vitacura', 'Vitacura'),
        ('Las Condes', 'Las Condes'),
        ('Lo Barnechea', 'Lo Barnechea'),
        ('La Dehesa', 'La Dehesa'),
        ('Estación Central', 'Estación Central'),
        ('Quinta Normal', 'Quinta Normal'),
        ('Pedro Aguirre Cerda', 'Pedro Aguirre Cerda'),
        ('Lo Prado', 'Lo Prado'),
        ('Pudahuel', 'Pudahuel'),
        ('Cerro Navia', 'Cerro Navia'),
        ('Lo Espejo', 'Lo Espejo'),
        ('Cerrillos', 'Cerrillos'),
        ('Maipú', 'Maipú'),
    )
    comuna = models.CharField(max_length=50, choices = Comuna)
    Direccion = models.CharField(max_length=5,blank=False)
    def __str__(self):
        return self.comuna+ '// Dirección: ' +self.Direccion

