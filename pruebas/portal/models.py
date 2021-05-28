from django.db import models

from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords

import pghistory

# Create your models here.


class CustomUser(AbstractUser):
    is_expert = models.BooleanField(default=False)
    



class Reports(models.Model):
    especie = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    link = models.URLField(default = 'https://www.google.com')
    ubicacion = models.URLField(default = 'https://www.google.com/maps/?hl=es')
    
    

    class Meta:
        db_table = "Reportes"
        # app_label="Proyecto2

    def __str__(self):
        texto = "({0}) ({1}) ({2}) ({3}) ({4}) ({5}) "
        return texto.format(self.especie, self.usuario ,self.lugar, self.region,  self.link, self.ubicacion)




class Articulos(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    enlace = models.CharField(max_length=100)

    class Meta:
        db_table = 'articulos'

    def __str__(self):
        texto = "({0}) ({1}) ({2})"
        return texto.format(self.titulo, self.autor ,self.enlace)
    
