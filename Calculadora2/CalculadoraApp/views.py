from django.shortcuts import render


# Create your views here.

def calculadora(request):
    return render(request, 'CalculadoraApp/calculadora.html')