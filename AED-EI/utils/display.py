def show_cities(cities):
  """Muestra por consola el listado de ciudades disponibles.

  Args:
    cities: Coleccion de objetos ciudad con atributos `id` y `name`.
  """
  print("\n📍 Ciudades disponibles:")
  print("----------------------------")
  
  for c in cities:
    print(f"{c.id} - {c.name}")

def pick_city(cities, message):
  """Solicita al usuario una ciudad valida y retorna su id.

  Args:
    cities: Coleccion de ciudades disponibles para seleccionar.
    message: Mensaje a mostrar al momento de pedir la entrada.

  Returns:
    int: Identificador de la ciudad elegida.
  """
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
  """Formatea una fila tabular ajustando cada valor al ancho indicado.

  Args:
    row: Fila de valores a mostrar.
    col_widths: Lista de anchos por columna.

  Returns:
    str: Fila formateada con separador de columnas.
  """
  return " | ".join(str(val).ljust(width) for val, width in zip(row, col_widths))

def print_results(headers, rows):
  """Imprime una tabla con encabezados y filas de resultados.

  Args:
    headers: Encabezados de las columnas.
    rows: Filas de datos a imprimir.
  """

  col_widths = []

  for col in zip(headers, *rows):
    col_widths.append(max(len(str(value)) for value in col))

  print(format_row(headers, col_widths))
  print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

  for row in rows:
    print(format_row(row, col_widths))

  print("")