from django.urls import path
from main.views import index

urlpatterns = [
    path('', index, name='index') # Dos comillas para llamar a la ruta raiz /
]