<h1 align="center">Spaghetti Code</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/Antipatrones)


<h2>¿De qué trata esta tarea?</h2>

Dada una porción de código Python escrita en estilo "Spaghetti Code", se te pide que identifiques las principales características de este antipatrón y refactorices el código para mejorar su legibilidad y mantenibilidad.

Considera el siguiente fragmento de código:

```
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")
```

**Se nos pide:**

1. Identificación de características de "Spaghetti Code": Debes ser capaz de identificar las características de "Spaghetti Code" en el código proporcionado. (20%)
2. Refactorización de código: Debes ser capaz de refactorizar el código para mejorar su legibilidad y mantenibilidad. Esto podría incluir la eliminación de la lógica de control basada en cadenas de texto, la modularización del código, y la mejora del manejo de errores. (60%)
3. Justificación de cambios: Debes ser capaz de justificar los cambios que has hecho al código, explicando cómo estos cambios mejoran el código y cómo evitan las características de "Spaghetti Code". (20%)

***


<h2>Indice</h2>

1. [1](#id1)
2. [2](#id2)
3. [3](#id3)
   

***
