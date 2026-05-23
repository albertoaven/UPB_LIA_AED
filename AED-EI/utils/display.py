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