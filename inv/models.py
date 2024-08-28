from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100, #Longitud maxima 100
        help_text= 'Descripción de la Categoría',
        unique=True
    )

    #Hacer referencia a la descripción
    def __str__(self):
        return '{}'.format(self.descripcion) #Toma el valor de descripción

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save() #Invocar el metodo save del padre

    class Meta:
        verbose_name_plural = "Categorias" #Guardar el nombre del modelo en pluar
