from django.db import models


# Create your models here.
class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=500)
    cantidad=models.IntegerField()
    activo=models.BooleanField()