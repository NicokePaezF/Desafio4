datos = []

with open("test.txt") as fname:
    lineas = fname.readlines()
    for linea in lineas:
        #print(linea.strip("\n"))
        datos.append(linea.strip('\n'))
print(datos)

lista = []
with open("test.txt") as fname:
    for lineas in fname:
        lista.extend(lineas.split())

for x in lista:
    print(x)




