from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description =  models.TextField()

class Generos(models.Model):
    id = models.AutoField(primary_key=True)
    generos = models.CharField(max_length=100)

class Usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    generos = models.ForeignKey(Generos,on_delete= models.PROTECT,default=False )
