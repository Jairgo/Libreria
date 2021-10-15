from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Store
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import createBookForm

# from django.views.generic.list import ListView

#Create your views here.
# def store(request):
#     libros = Store.objects.all()
#     return render(request, 'store/libros.html', {"libros":libros})

class storeListView(ListView):
    model = Store

class storeDetailView(DetailView):
    model = Store

# def libro(request,libro_id):
#     libro = Store.objects.get(id=libro_id)
#     return render(request, 'store/libro.html', {"libro":libro})

class StoreCreateView(CreateView):
    model = Store
    fields = ['title', 'description', 'book']
    success_url = reverse_lazy('libros:libros')

class StoreUpdateView(UpdateView):
    model = Store
    fields = ['title', 'description', 'book']
    template_name_suffix = '_update_form'
    # success_url = reverse_lazy('libros:update')

    def get_success_url(self):
        return reverse_lazy('libros:update', args=[self.object.id]) + '?ok'

class StoreDeleteView(DeleteView):
    model = Store
    success_url = reverse_lazy('libros:libros')

    