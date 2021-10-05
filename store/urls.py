from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.store, name="store"),
     path('libros/<int:libro_id>', views.libro, name="libro")
]