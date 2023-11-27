class Calculadora:
    def suma(self, num1, num2):
        return num1 + num2

    def resta(self, num1, num2):
        return num1 - num2

    def multiplicacion(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")

    def calcular(self, operacion, num1, num2):
        if operacion == 'suma':
            return self.suma(num1, num2)
        if operacion == 'resta':
            return self.resta(num1, num2)
        if operacion == 'multiplicacion':
            return self.multiplicacion(num1, num2)
        if operacion == 'division':
            return self.division(num1, num2)
        else:
            print("Operación no soportada.")

# Uso de la clase
calculadora = Calculadora()
resultado_suma = calculadora.calcular('suma', 5, 3)
print(f"Resultado de la suma: {resultado_suma}")

resultado_resta = calculadora.calcular('resta', 5, 3)
print(f"Resultado de la resta: {resultado_resta}")

resultado_multiplicacion = calculadora.calcular('multiplicacion', 5, 3)
print(f"Resultado de la multiplicación: {resultado_multiplicacion}")

resultado_division = calculadora.calcular('division', 5, 3)
print(f"Resultado de la división: {resultado_division}")
