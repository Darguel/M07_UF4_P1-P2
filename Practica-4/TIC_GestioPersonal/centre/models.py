from django.db import models

class Rol(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Usuari(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    cognom = models.CharField(max_length=100)
    assignatures = models.CharField(max_length=100)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)


    