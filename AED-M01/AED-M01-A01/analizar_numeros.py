import time

def sumar_numeros(numeros):
    """Suma una lista de números y devuelve el resultado."""

    return sum(numeros)

def promediar_numeros(numeros):
    """Calcula el promedio de una lista de números y devuelve el resultado."""

    cantidad = len(numeros)

    if cantidad == 0:
      return 0
    
    suma = sumar_numeros(numeros)

    return suma / cantidad

def encontrar_maximo(numeros):
   """Devuelve el máximo número dentro a lista de números."""

   cantidad = len(numeros)

   if cantidad == 0:
      return None
   
   maximo = numeros[0]

   for numero in numeros:
      if(numero > maximo):
         maximo = numero

   return maximo

def encontrar_minimo(numeros):
   """Devuelve el mínimo número dentro a lista de números."""

   cantidad = len(numeros)

   if cantidad == 0:
      return None
   
   minimo = numeros[0]

   for numero in numeros:
      if(numero < minimo):
         minimo = numero

   return minimo

def analizar_numeros(numeros):
   """Analiza una lista de números y devuelve la suma, el promedio, el máximo y el mínimo"""

   cantidad = len(numeros);

   if(cantidad == 0):
      print("debe ingresar una lista de números para poder analizarlos.")

   suma = sumar_numeros(numeros)
   promedio = promediar_numeros(numeros)
   maximo = encontrar_maximo(numeros)
   minimo = encontrar_minimo(numeros)

   analisis = {
      "Suma": suma,
      "Promedio": promedio,
      "Máximo": maximo,
      "Mínimo": minimo
   }

   return analisis


if __name__ == "__main__":
   numeros = []

   while True:
      numero = input("Ingrese un número entero (o 'salir' para terminar): ")

      if numero.lower() == 'salir':
         break
      
      try:
        numeros.append(int(numero))
      except ValueError:
         print("Por favor, ingrese un número entero válido.")

   inicio = time.time()

   resultado = analizar_numeros(numeros)

   print(resultado)

   fin = time.time()
   tiempo = fin - inicio;

   print(f"Ejecutado en {tiempo} segundos.")