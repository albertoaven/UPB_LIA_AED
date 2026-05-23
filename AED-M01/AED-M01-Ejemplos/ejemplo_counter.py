from collections import Counter

etiquetas = [0, 1, 1, 0, 1, 1, 0]
conteo = Counter(etiquetas)

print (f"Frecuencias: {conteo}")
print (f"Cantidad de clase 1: {conteo[1]}")