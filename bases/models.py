from django.db import models

from django.contrib.auth.models import User #Importar modelo User
from django_userforeignkey.models.fields import UserForeignKey

#Todas las clases que hereden de ClaseModelo seran secundarias
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) 
    fc = models.DateTimeField(auto_now_add=True) #Guardar fecha de creación
    fm = models.DateTimeField(auto_now=True) #Guardar fecha de cuando se realizan modificacioens
    uc = models.ForeignKey(User, on_delete=models.CASCADE) #Relacion de 1 a N
    um = models.IntegerField(blank=True, null=True) #Guadar valores nulos o blnacos para el ID hasta que se modifique

    class Meta:
        #No tomar en cuenta el modelo en las migraciones, pero si para herencias
        abstract=True

#Nueva forma de ClaseModelo
class ClaseModelo2(models.Model):
    estado = models.BooleanField(default=True) 
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = UserForeignKey(auto_user_add = True, related_name='+')
    um = UserForeignKey(auto_user = True,related_name='+')

    class Meta:
        abstract=True