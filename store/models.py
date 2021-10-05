from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import FileField
from ckeditor.fields import RichTextField

# Create your models here.
class Store(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = RichTextField(verbose_name="Descripción")
    book = models.FileField(verbose_name="Archivo", upload_to="store")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        ordering = ["-created"]

    def __str__(self):
        return self.title