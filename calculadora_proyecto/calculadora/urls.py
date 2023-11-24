from django.urls import path
from . import views
urlpatterns = [
    path('', views.calcular, name='calcular'),  # Puedes ajustar esto según tus necesidades
]