import sys

programa = sys.argv[0]
sol_peruano = sys.argv[1]
peso_argentino = sys.argv[2]
dolar_americano = sys.argv[3]
peso_chileno = sys.argv[4]

sp = float(peso_chileno) * float(sol_peruano)
pa = float(peso_chileno) * float(peso_argentino)
da = float(peso_chileno) * float(dolar_americano)

print("Los ", str(peso_chileno), " pesos equivalen a:")
print(sp, " Soles")
print(pa, " Pesos Argentinos")
print(da, " Dólares")




