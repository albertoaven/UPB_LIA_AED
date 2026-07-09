def busqueda_lineal(lista, clave):
  for indice, elemento in enumerate(lista):
    if elemento == clave:
      return indice
    
  return -1

datos = [42, 7, 19, 23, 5, 88]

resultado = busqueda_lineal(datos, 23)

if(resultado > -1):
  print(f"El valor 23 se encuenta en la posición {resultado}.")
else:
  print(f"El valor 23 no se encuentra en la lista.")