import time

def suma_for(n):
  total = 0
  
  for i in range(1, n+1):
    total += i

  return total

def suma_formula(n):
  return n * (n + 1) // 2


n = 1000000

# Suma con for
inicio = time.time()

suma_for(n)

fin = time.time()

print(f"Tiempo suma con for: { fin - inicio }")

# Suma con fórmula
inicio = time.time()

suma_formula(n)

fin = time.time()

print(f"Tiempo suma con fórmula: { fin - inicio }")