"""
Enunciado:

Implementa una función llamada find_max(lst) que encuentre el valor máximo en una
lista de números utilizando recursión. La función debe devolver el valor
máximo de la lista.

Parámetros:
    lst (List): lista de números enteros o flotantes

Ejemplo:
    Entrada:
    numbers_list = [1, 5, 2, 7, 3]
    find_max(numbers_list)

    Salida:
    7
"""


def find_max(lst):
    if len(lst)==1: #Si la lista sólo tiene 1 elemento, ese es su máximo
        return lst[0]
    else: #Si tiene más de 1 elemento, calculo el máximo entre ese elemento  el resto de elementos recursivamente
        return max(lst[0],find_max(lst[1:]))



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#numbers_list = [1, 5, 2, 7, 3]
#print(find_max(numbers_list))
