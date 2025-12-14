from django.db import models


#clase del auto con sus respectivos atributos
class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    year = models.IntegerField()
    precio = models.IntegerField()
    kilometraje = models.IntegerField()
    puertas = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.year}"


# Create your models here.
