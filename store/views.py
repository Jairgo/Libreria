from django.shortcuts import render
from .models import Store

# Create your views here.
def store(request):
    libros = Store.objects.all()
    return render(request, 'store/libros.html', {"libros":libros})

def libro(request,libro_id):
    libro = Store.objects.get(id=libro_id)
    return render(request, 'store/libro.html', {"libro":libro})