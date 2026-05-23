# Este programa calcula estadísticas de temperaturas 

# Importaciones

import statistics 

# Fin importaciones

# Funciones

# Función para convertir Celsius a Fahrenheit 
def celsius_a_fahrenheit(celsius):
  """Convierte temperatura de Celsius a Fahrenheit""" 
  return (celsius * 9/5) + 32 

# Fin funciones

# Código principal 

datos_celsius = [20, 22, 18, 25, 19] 

print("Temperaturas en Celsius:", datos_celsius) 

total = sum(datos_celsius) 
promedio = total / len(datos_celsius) 

print(f"Promedio: {promedio:.2f}°C") 

datos_fahrenheit = [celsius_a_fahrenheit(t) for t in datos_celsius] 

print("Temperaturas en Fahrenheit:", datos_fahrenheit) 

desv_std = statistics.stdev(datos_celsius) 

print(f"Desv. Estándar: {desv_std:.2f}")