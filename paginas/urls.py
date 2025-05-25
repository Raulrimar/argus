from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    #path('endereço', minha view.as_view(),name='nome da url')
    path('', PaginaInicial.as_view(),name='inicio'),
]