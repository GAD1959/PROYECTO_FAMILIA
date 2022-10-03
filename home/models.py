from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fe_nacimiento = models.DateField(null=True)
    edad = models.IntegerField()
    descPariente = models.CharField(max_length=30)