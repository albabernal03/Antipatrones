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

## Respuesta punto 1:<a name="id1"></a>

El código espagueti a menudo se caracteriza por la falta de estructura clara, la presencia de bucles y condicionales anidados en exceso; como podemos ver en el código anterior se observa un uso recurrente de sentencias condicionales anidadas (if), a esta característica se la denomina "Código Convolucionado", la cual complica en gran manera el seguimiento y la comprensión del algoritmo, siendo este además el ambiente propicio para errores de programación (bugs).

Por otro lado, vemos el uso de cadenas de texto para la lógica de control, esto puede ocasionar que  sea difícil de entender y mantener. En este caso, la cadena 'operacion' se utiliza para determinar la operación a realizar.

Asi mismo, notamos una clara falta de modulación, pues la función 'calcular' tiene múltiples responsabilidades, ya que maneja la lógica de todas las operaciones y también imprime mensajes de error. Esto viola el principio de "una función, una responsabilidad". Uno de los principios SOLID que se conoce como Single Responsibility.

Por último, hay un manejo de error insuficiente,pues e realiza mediante impresiones directas en lugar de lanzar excepciones, lo que no es una práctica robusta.

***

## Respuesta punto 2:<a name="id2"></a>

Refactorización del código:

```
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("No se puede dividir entre cero.")


def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return suma(num1, num2)
    if operacion == 'resta':
        return resta(num1, num2)
    if operacion == 'multiplicacion':
        return multiplicacion(num1, num2)
    if operacion == 'division':
        return division(num1, num2)
    else:
        print("Operación no soportada.")

        

```
## Respuesta punto 3:<a name="id3"></a>

Aquí vemos como mejoramos todo lo que mencionamos anteriormente:

1.**Eliminación de lógica de control basada en cadenas de texto:** Se reemplazaron las cadenas de texto con funciones específicas para cada operación. Esto hace que el código sea más legible y evita el uso de cadenas como control de flujo.

2.**Modularización del código:** Se crearon funciones separadas para cada operación, siguiendo el principio de "una función, una responsabilidad". Esto mejora la organización del código y facilita su mantenimiento.

3.**Mejora del manejo de errores:** Se reemplazaron las impresiones directas por el lanzamiento de excepciones con mensajes descriptivos. Esto proporciona un manejo de errores más robusto y comprensible.









