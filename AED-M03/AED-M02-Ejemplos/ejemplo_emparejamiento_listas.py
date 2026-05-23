def emparejar_listas(a, b):
  i = j = 0
  resultado = []

  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      resultado.append(a[i])
      i += 1
      j += 1
    elif a[i] < b[j]:
      i += 1
    else:
      j += 1
  
  return resultado
  
a = [10, 15, 20, 23, 45, 67, 70]
b = [20, 21, 22, 23, 24]

print(f"Valores comunes: {emparejar_listas(a, b)}")