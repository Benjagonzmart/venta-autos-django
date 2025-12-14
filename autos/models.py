from django.db import models


#clase del auto con sus respectivos atributos
class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=50)
    year = models.IntegerField()
    precio = models.PositiveIntegerField()
    kilometraje = models.PositiveIntegerField()
    BODY_CHOICES = [
        ("SUV", "SUV"),
        ("SEDAN", "Sedán"),
        ("HATCHBACK", "Hatchback"),
        ("PICKUP", "Pickup"),
        ("COUPE", "Coupé"),
        ("MINIVAN", "Minivan"),
    ]

    body = models.CharField(max_length=20, choices=BODY_CHOICES)
    color = models.CharField(max_length=100)

    TRANSMISION_CHOICES = [
        ("manual", "Manual"),
        ("automatica", "Automática"),
    ]

    COMBUSTIBLE_CHOICES = [
        ("bencina", "Bencina"),
        ("diesel", "Diésel"),
        ("electrico", "Eléctrico"),
        ("hibrido", "Híbrido"),
    ]

    transmision = models.CharField(max_length=20, choices=TRANSMISION_CHOICES)
    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES)
    motor = models.CharField(
        max_length=50,
        help_text="Ej: 1.6, 2.0 Turbo, V6 3.5"
    )
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to="autos/", blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} {self.year}"


# Create your models here.
