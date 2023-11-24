from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse

def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            resultado = num1 / num2
        else:
            resultado = 'Operación no válida'

        return JsonResponse({'resultado': resultado})
    else:
        return render(request, 'calculadora/calculadora.html')