import sys

lista_pequena = list(range(10))
lista_grande = list(range(100000))

print(f"Tamaño lista pequeña (bytes): { sys.getsizeof(lista_pequena) }")
print(f"Tamaño lista grande (bytes): { sys.getsizeof(lista_grande) }")