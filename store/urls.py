from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from .views import StoreCreateView, StoreUpdateView, StoreDeleteView, compraSuccess, storeCreateCompra, storeDetailView, storeListView

store_patterns = ([
    # path('', views.store, name="store"),
    path('', storeListView.as_view(), name="libros"),
    path('libro/<int:pk>', storeDetailView.as_view(), name="libro"),
    # path('libros/<int:libro_id>', views.libro, name="libro"),
    # path('libro/<int:pk>/', storeDetailView.as_view(), name="libro"),
    path('create/', StoreCreateView.as_view(), name="create"),
    path('update/<int:pk>', StoreUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', StoreDeleteView.as_view(), name="delete"),

    path('compra/', views.comprar, name="detalle_compra"),
    path('create_compra/', storeCreateCompra.as_view(), name="create_compra"),
    path('success_pedido/', compraSuccess.as_view(), name="success_compra"),

], 'libros')