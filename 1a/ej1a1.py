'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.
Asimismo, si el valor no es numérico, o es menor a cero, se debe lanzar 
una excepción ValueError("mensaje"), la cual puede incluir un mensaje que debería 
corresponder con el tipo de error durante la validación.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

'''

def fibonacci(fibonacci_number):
    #Primero intrducimos las precondiciones de tipo de dato
    if isinstance(fibonacci_number,int)==False:
        raise ValueError("El valor introducido no es un entero")
    elif fibonacci_number<0: #Ya sabemos que es un valor númerico, comprobamos que sea mayor que 0
        raise ValueError("Posición menor que 0")
    else:
    #Una vez que se han cumplido las precondiciones, calculamos la serie de Fibonacci
        x,y = 0,1
        for aux in range(fibonacci_number):
            z = x+y
            x=y 
            y = z
        return x 


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 

#print(fibonacci(-1))
