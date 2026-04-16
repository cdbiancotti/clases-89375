from django.db import models


class JabonLiquido(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    fecha = models.DateField()