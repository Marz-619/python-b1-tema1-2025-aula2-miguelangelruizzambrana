'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain:str):
    cadena_invertida = "" #Inicializamos a 0 la cadena invertida que el programa va a devolver
    aux = len(text_chain)-1 #Calculamos la longitud de la cadena a invertir y restamos 1 para no salirnos de la palabra
    while aux>=0: #Condición de recorrer la cadena entera
        cadena_invertida = cadena_invertida + str(text_chain[aux])
        aux-=1
    return cadena_invertida
    

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
#print(invert_text("Hello world!"))
