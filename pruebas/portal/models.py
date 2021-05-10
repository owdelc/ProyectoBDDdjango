from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    is_suscribed = models.BooleanField(default=False)
    is_artist = models.BooleanField(default=False)
    is_moderatorA = models.BooleanField(default=False)
    is_moderatorB = models.BooleanField(default=False)

class Music(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)

    class Meta:
        db_table = "songs"
        # app_label="Proyecto2