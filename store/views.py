from django.shortcuts import render
from django.urls.base import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Store
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import CompraForm, createBookForm, updateBookForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
class storeCreateCompra(CreateView):
    form_class = CompraForm
    template_name = 'store/compra_cliente.html'
    success_url = reverse_lazy('libros:success_pedido')

    def form_valid(self, form):
        # Guardar los datos del pedido
        compra = form.save(commit=False)
        compra.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # Coloca el request disponible para el formulario
        kwargs = super(storeCreateCompra, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class compraSuccess(TemplateView):
    template_name = 'store/compra_success.html'


def _crear_diccionario(datos_compra):
    diccionario = {}
    datos_compra = datos_compra[:-1]
    librosComprados = datos_compra.split("|")
    for libroComprado in librosComprados:
        detalle = libroComprado.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario

def comprar(request):
    pedido = list()
    if request.method == 'POST':
        datos_compra = request.POST['datos_compra']
        librosComprados = _crear_diccionario(datos_compra)
        total = 0
        for codigo in librosComprados.keys():
            cantidad = librosComprados[codigo]
            if cantidad > 0:
                dict_libros = {}
                libro = Store.objects.get(pk=codigo)
                dict_libros['id'] = libro.id
                dict_libros['title'] = libro.title
                dict_libros['description'] = libro.description
                dict_libros['price'] = libro.price
                total += cantidad * libro.price
                pedido.append(dict_libros)
        # Se guarda el total en una variable de sesión
        request.session['total'] = float(total)

    return render(request, "store/detalle_compra.html", {"pedido": pedido, "total":total})

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
@method_decorator(staff_member_required,name='dispatch')
class StoreCreateView(CreateView):
    model = Store
    form_class = createBookForm
    # fields = ['title', 'description', 'book']
    success_url = reverse_lazy('libros:libros')

    def form_valid(self, form):
        # Guardar los datos del libro
        libro = form.save(commit=False)
        libro.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # Coloca el request disponible para el formulario
        kwargs = super(StoreCreateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
@method_decorator(staff_member_required,name='dispatch')
class StoreUpdateView(UpdateView):
    model = Store
    form_class = updateBookForm
    # fields = ['title', 'description', 'book']
    template_name_suffix = '_update_form'
    # success_url = reverse_lazy('libros:update')

    def get_success_url(self):
        print("Hola")
        return reverse_lazy('libros:update', args=[self.object.id]) + '?ok'

    def form_valid(self, form):
        # Guardar los datos del libro
        libro = form.save(commit=False)
        libro.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        # Coloca el request disponible para el formulario
        kwargs = super(StoreUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
@method_decorator(staff_member_required,name='dispatch')
class StoreDeleteView(DeleteView):
    model = Store
    success_url = reverse_lazy('libros:libros')

    