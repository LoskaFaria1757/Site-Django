import math
import numpy


lista_antes = [1,2,3,4,5,6,7,8,9,10,10]

lista_depois = []

for elemento in lista_antes:
    if elemento not in lista_depois:
        lista_depois.append(elemento)

print(f"Antes: {lista_antes}")
print(f"Depois: {lista_depois}")te