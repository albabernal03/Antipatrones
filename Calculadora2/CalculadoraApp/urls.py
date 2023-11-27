from django.urls import path
from CalculadoraApp import views



urlpatterns = [
    path('',views.calculadora, name='calculadora')
]
