import time

def suma_lista(numeros):
    """Calcula la suma de una lista de números"""
    
    total = 0

    for numero in numeros:
        total += numero

    return total

# Datos pequeños: 10 números
numeros = [i for i in range(1, 100001)]

inicio = time.time()
resultado = suma_lista(numeros)
fin = time.time()

print(f"Tamaño de lista: {len(numeros)}")
print(f"Suma: {resultado}")
print(f"Tiempo de ejecución: {(fin - inicio) * 1000:.6f} ms")