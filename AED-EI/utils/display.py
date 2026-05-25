def show_cities(cities):
  print("\n📍 Ciudades disponibles:")
  print("----------------------------")
  
  for c in cities:
    print(f"{c.id} - {c.name}")

def pick_city(cities, message):
  show_cities(cities)

  ids_validos = {c.id for c in cities}

  while True:
    seleccion = input(f"\n{message}: ")

    try:
      seleccion = int(seleccion)

      if seleccion in ids_validos:
        return seleccion
      else:
        print("⚠️ ID inválido. Intente nuevamente.")
    except ValueError:
      print("⚠️ Ingrese un número válido.")

def format_row(row, col_widths):
  return " | ".join(str(val).ljust(width) for val, width in zip(row, col_widths))

def print_results(headers, rows):
  # Calcular ancho máximo de cada columna según la cantidad 
  # máxima de caracteres de los valores
  col_widths = []

  for col in zip(headers, *rows):
    col_widths.append(max(len(str(value)) for value in col))

  # Imprimir encabezado
  print(format_row(headers, col_widths))
  print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

  # Imprimir filas
  for row in rows:
    print(format_row(row, col_widths))

  print("")