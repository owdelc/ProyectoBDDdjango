from django.db import models

from django.contrib.auth.models import AbstractUser

from simple_history.models import HistoricalRecords

import pghistory

# Create your models here.


#@pghistory.track(pghistory.AfterInsertOrUpdate('CustomUser'))
class CustomUser(AbstractUser):
    is_suscribed = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_moderatorA = models.BooleanField(default=False)
    is_moderatorB = models.BooleanField(default=False)
    history = HistoricalRecords()


#@pghistory.track(pghistory.AfterInsertOrUpdate('Music'))
class Music(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    reprodu = models.IntegerField(default=0)
    link = models.URLField(default = 'https://www.w3schools.com')
    history = HistoricalRecords()
    

    class Meta:
        db_table = "songs"
        # app_label="Proyecto2

    def __str__(self):
        texto = "({0}) ({1}) ({2}) ({3}) ({4}) ({5}) "
        return texto.format(self.name, self.album ,self.artista, self.year,  self.genero, self.reprodu)


class ReproduccionesModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha = models.DateField()
    

    class Meta:
        db_table = "reproducciones"
        # app_label="Proyecto2

    def __str__(self):
        texto = "({0}) ({1}) ({2}) ({3})"
        return texto.format(self.name, self.album ,self.artista, self.fecha,)


class PlaylistModel(models.Model):
    user = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    class Meta:
        db_table = 'playlist'

    def __str__(self):
        texto = "({0}) ({1}) ({2})"
        return texto.format(self.user, self.name ,self.genero,)
    
