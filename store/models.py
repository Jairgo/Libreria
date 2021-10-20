from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import FileField
from ckeditor.fields import RichTextField

class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    correo = models.EmailField(verbose_name="Email")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    direccion = models.CharField(max_length=200, verbose_name="Calle y Número", help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la calle y número</span>')
    colonia = models.CharField(max_length=200, verbose_name="Colonia o Fraccionamiento",
                               help_text='<span class="font-italic" style="font-size: 0.9rem">Nombre de la colonia o fraccionamiento</span>')
    total = models.DecimalField(verbose_name="Total", max_digits=8,  decimal_places=2,
                                help_text='<span class="text-danger" style="font-size: 0.9rem">Cantidad a pagar por su pedido</span>')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ["-fecha"]

    def __str__(self):
        return str(self.id)
        

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = RichTextField(verbose_name="Descripción")
    book = models.FileField(verbose_name="Archivo", upload_to="store")
    price = models.IntegerField(verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-created"]

    def __str__(self):
        return self.title