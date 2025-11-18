'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

'''

def sum_odd_numbers(list_numbers):
    # Primero revisamos las precondiciones
    for num in list_numbers:
        if isinstance(num,int)==False: #Uno de los elementos de la lista no es tipo entero
            raise ValueError ("Uno de los elementos NO es de tipo entero")
        elif num < 0: #Sabiendo que el elemento es entero, reviso que sea mayor que cero
            raise ValueError ("Uno de los elemento es menor que cero")
    #Cumplidas las precondiciones, calculo la suma de los impares
    suma_impares = 0 #Inicializo el resultado de todos los numeros impares de la lista
    for num in list_numbers:
        if num%2 != 0: #El número es impar, se suma al total
            suma_impares = suma_impares + num
    return suma_impares
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 

#print(sum_odd_numbers([-1, 2, 3, 4, 5, 10, 21, 100]))
