def busqueda_binaria(lista, clave):
  inicio = 0
  fin = len(lista) - 1

  while inicio <= fin:
    medio = (inicio + fin) // 2

    if lista[medio] == clave:
      return medio
    elif lista[medio] < clave:
      inicio = medio + 1
    else:
      fin = medio - 1

  return -1

datos = [3, 7, 12, 19, 25, 31, 42]

resultado = busqueda_binaria(datos, 19)

print("Resultado en posición: ", resultado)