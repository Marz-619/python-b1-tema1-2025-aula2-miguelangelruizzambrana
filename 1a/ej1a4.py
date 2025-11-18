'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

'''

def count_vowels(text_chain:str):
    cnt_vocales = 0 #Inciializamos el contador de vocales
    #Convertimos la cadena a minúsculas para no tener que evaluar el doble de casos
    text_chain = text_chain.lower()
    for aux in text_chain:
        if aux=='a' or aux=='e' or aux=='i' or aux=='o' or aux=='u': #Es vocal
            cnt_vocales +=1
        else: 
            pass
    return cnt_vocales

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
#print(count_vowels("Hello world, this is an example."))
