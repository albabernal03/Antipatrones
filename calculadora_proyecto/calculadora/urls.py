from django.urls import path
from .views import calcular

urlpatterns = [
    path('', calcular, name='calcular'),  # Puedes ajustar esto según tus necesidades
]