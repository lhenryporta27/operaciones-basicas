"""
Este script contiene errores comunes que violan las normas PEP 8.

Errores identificados:
1. Falta de espacios alrededor de los operadores de asignación en las definiciones de variables globales.
2. Nombres de variables en mayúsculas que no representan constantes inmutables (numeros, num1, num2).
3. Métodos dentro de las clases que modifican atributos sin retornarlos explícitamente.
4. Falta de salto de línea entre clases y funciones según las normas PEP 8.
5. Uso de comentarios redundantes en la ejecución principal.
6. Líneas de código demasiado largas (más de 100 caracteres).

Clases:
- OperacionesBasicas: Realiza operaciones de suma y resta.
- CalculadoraPromedio: Calcula el promedio de una lista de valores.

Ejecución:
Al ejecutar este script, se instanciarán las clases y se mostrarán los resultados en la consola.
"""


class OperacionesBasicas:
    """Clase que realiza operaciones básicas de suma y resta."""

    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        """Suma dos números y almacena el resultado."""
        self.resultado = a + b

    def restar(self, a, b):
        """Resta dos números y almacena el resultado."""
        self.resultado = a - b

    def obtener_resultado(self):
        """Devuelve el resultado de la última operación realizada."""
        return self.resultado


class CalculadoraPromedio:
    """Clase que calcula el promedio de una lista de valores."""

    def __init__(self, valores):
        self.valores = valores

    def calcular_promedio(self):
        """Calcula y devuelve el promedio de los valores almacenados."""
        suma = sum(self.valores)
        return suma / len(self.valores)

    def cantidad_valores(self):
        """Devuelve la cantidad de valores en la lista."""
        return len(self.valores)


# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM_1 = 10
NUM_2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM_1, NUM_2)
    print(
        "El resultado de la suma es: "
        f"{operaciones.obtener_resultado()}"
    )

    operaciones.restar(NUM_1, NUM_2)
    print(
        "El resultado de la resta es: "
        f"{operaciones.obtener_resultado()}"
    )

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(
        "El promedio de los números es: "
        f"{promedio}"
    )
