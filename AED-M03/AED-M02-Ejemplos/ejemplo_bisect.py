from bisect import bisect_left

umbrales = [0.2, 0.4, 0.6, 0.8]
valor = 0.65

indice = bisect_left(umbrales, valor)

print(f"El valor debe ubicarse en la posición: {indice}")