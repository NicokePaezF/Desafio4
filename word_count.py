#Cuente la cantidad de caracteres distintos que componen un texto.
#Cuente el número de palabras distintas que componen el texto ingresado.Para separar un texto por espacios puede utilizar el método .split("").

#hola como estas hola
#15 caracteres

total = 0
cont = 0
repetidas = 0
totalDistinto = 0
letras_dic = dict()

with open('lorem_ipsum.txt', 'r', encoding="utf-8") as archivo:
    palabra = archivo.read()

    lista = palabra.split(' ')
    lista_unica = list(set(lista))
    total_unicos = len(lista_unica)

    for letra in palabra:  # Por cada palabra
        if palabra.count(letra) >= 1:
            totalDistinto += 1
            palabra = ''.join(x for x in palabra if x not in letra)

print("El número de caracteres distintos es: ", totalDistinto)
print("El número de palabras distintas es: ", total_unicos)

