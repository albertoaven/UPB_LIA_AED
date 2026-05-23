import time

def recorrer(n):
  for i in range(n):
    pass

for tamano in [1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
  inicio = time.time()

  recorrer(tamano)

  fin = time.time()

  print(f"Tamaño: { tamano } - Tiempo: { fin - inicio }")