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


class SubCategoria(ClaseModelo): #Tiene relacion con el modelo Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 
    descripcion = models.CharField(
        max_length=100,
        help_text= 'Descripción de la Categoría'
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion') #Para que la descripcion no se repita por categorias


class Marca(ClaseModelo):
        descripcion = models.CharField(
            max_length=100,
            help_text='Descripción de la Marca',
            unique=True
        )

        def __str__(self):
            return '{}'.format(self.descripcion)
    
        def save(self):
            self.descripcion = self.descripcion.upper()
            super(Marca, self).save()

        class Meta:
            verbose_name_plural = "Marca"


class UnidadMedida(ClaseModelo):
    descripcion = models.CharField(
            max_length=100,
            help_text='Descripcion de la Unidad Medida',
            unique=True
        )
    
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(UnidadMedida, self).save()

    class Meta:
        verbose_name_plural = "Unidades de Medida"