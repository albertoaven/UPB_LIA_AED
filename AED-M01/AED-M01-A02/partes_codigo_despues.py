# IMPORTACIONES

import time
import statistics 

# DEFINICIÓN DE FUNCIONES

def celsius_a_fahrenheit(celsius):
  """Convierte temperatura de Celsius a Fahrenheit""" 
  
  return (celsius * 9/5) + 32 

def calcular_estadisticas(datos_celsius):
  """Calcula las estadísticas con las temperaturas recibidas"""
  
  if(len(datos_celsius) == 0):
    return None
  
  total = sum(datos_celsius) 
  promedio = total / len(datos_celsius) 
  desv_std = statistics.stdev(datos_celsius) 

  return promedio, desv_std

#PROGRAMA PRINCIPAL

if __name__ == "__main__":
  print ("Calculadora de temperaturas y estadíscticas")
  print()

  temperaturas = []

  while True:
    temperatura = input("Ingrese una temperatura en grados Celsius ('salir' para parar): ")

    if temperatura == "salir":
      break;
    
    try:
      temperaturas.append(int(temperatura))
    except:
      print("Ingrese un número entero válido.")

  inicio = time.time()

  print("Temperaturas en Celsius:", temperaturas) 

  datos_fahrenheit = [celsius_a_fahrenheit(t) for t in temperaturas] 

  print("Temperaturas en Fahrenheit:", datos_fahrenheit) 

  promedio, desv_Est = calcular_estadisticas(temperaturas)

  fin = time.time()
  tiempo = fin - inicio

  print(f"Promedio: {promedio:.2f}°C") 
  print(f"Desv. Estándar: {desv_Est:.2f}")
  print()
  print(f"Tiempo del cálculo: {tiempo:.2f}")
  print()