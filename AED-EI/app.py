# --------------- Importación de los módulos a usar en el sistema ---------------
import timeit
from collections import deque
from datetime import datetime

from db.connection import conectar

from repositories.postgres_repository import PostgresRepository
from repositories.datasource import DataSource

from utils.display import pick_city, format_row, print_results

from services.priority_queue import PriorityHeap
from services.indexing import build_index_by_id
from services.avl import build_event_avl

from algorithms.bs import bs
from algorithms.quick_sort import quick_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.bfs import bfs, find_bfs
from algorithms.dfs import recursive_dfs, find_dfs
from algorithms.dijkstra import dijkstra, find_path_dijkstra
from algorithms.prim import prim

from models.event import Event
from models.graph import create_graph, draw_graph
from models.route import Route




# --------------- Fin Importación de los módulos a usar en el sistema ------------

def show_pending_event_list(datasource):
  """Muestra en consola todos los eventos almacenados en la base de datos.
  Args:
    datasource: Origen de datos.
  """
  events = datasource.get_not_resolved_events()
  headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description"]
  rows = []

  for e in events:
    rows.append([
      e.id,
      str(e.timestamp),
      e.category,
      e.priority,
      e.origin,
      e.destination,
      e.description,
      e.age
    ])

  print_results(headers, rows)
  print(f"Se encontraron {len(events)} eventos pendientes de resolver.")
  print("")

def create_event(datasource):
  """Solicita datos por consola, crea un evento y lo persiste en la base.
  Args:
    datasource: Origen de datos.
  """
  print("Ingrese los datos del evento: ")
  print("")

  cities = datasource.get_cities()

  date = input("Fecha y hora del evento en formato 'YYYY-MM-DD HH:mm': ")

  date = datetime.strptime(
    date,
    "%Y-%m-%d %H:%M"
  )

  category = input("Ingrese la categoría del evento: ")
  priority = int(input("Ingrese la prioridad del evento: "))
  description = input("Ingrese la descripción del evento: ")

  #Primero muestro un listado para que el usuario vea el ID de la ciudad
  origin = pick_city(cities, "Ingrese la ciudad cuidad del origen: ")
  #Primero muestro un listado para que el usuario vea el ID de la ciudad
  destination = pick_city(cities, "Ingrese la ciudad cuidad de destino: ")

  new_event = Event(
    id = None,
    timestamp = date,
    category = category,
    priority = priority,
    description = description,
    origin = origin,
    destination = destination,
    status= "pending"
  )

  result = datasource.insert_event(new_event)

  print("")

  if result > 0:
    print(f"Evento creado exitosamente (Id = {result})")
  else:
    print("Hubo un error al crear el evento.")

  print("")

def create_city(datasource):
    print()

    name = input("Ingrese el nombre de la ciudad: ")
    latitude = input("Ingrese la latitud de la ciudad: ")
    longitude = input("Ingrese la longitud de la ciudad: ")

    city_id = datasource.add_city(name, latitude, longitude)

    print(f"Ciudad creada correctamente. ID={city_id}")

    print()

def show_incidents_by_priority(datasource):
  """Muestra los eventos ordenados por prioridad usa sorted().
  Args:
    datasource: Origen de datos.
  """
  events = process_incidents_by_priority(datasource)
  queue = deque(events)

  print("La cola con la prioridad por 'Prioridad' es:")
  print("")

  headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description"]
  rows = []

  while queue:
    event = queue.popleft()

    rows.append([
      event.id,
      str(event.timestamp),
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description,
      event.age
    ])

  print_results(headers, rows)
  
  time = timeit.timeit(
      lambda: process_incidents_by_priority(datasource),
      number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_priority(datasource):
  """Obtiene y ordena eventos pendientes por prioridad ascendente.
  Args:
    datasource: Origen de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por prioridad.
  """
  events = deque(datasource.get_not_resolved_events())
  event_sorted = sorted(events, key=lambda e: e.priority)

  return event_sorted

def show_incidents_by_priority_quicksort(datasource):
  """Muestra los eventos ordenados por prioridad usando el algoritmo de ordenamiento quicksort.
  Args:
    datasource: Origen de datos.
  """

  events = process_incidents_by_priority_quicksort(datasource)

  print("La cola con la prioridad por 'Prioridad' es:")
  print("")

  headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description"]
  rows = []

  for event in events:
    rows.append([
      event.id,
      str(event.timestamp),
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description,
      event.age
    ])

  print_results(headers, rows)  

  time = timeit.timeit(
    lambda: process_incidents_by_priority_quicksort(datasource),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_priority_quicksort(datasource):
  """Obtiene y ordena eventos pendientes por prioridad usando quick sort.
  Args:
    datasource: Origen de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por prioridad.
  """
  events = deque(datasource.get_not_resolved_events())
  event_sorted = quick_sort(events, True)

  return event_sorted

def show_incidents_by_age(datasource):
  """Muestra los eventos ordenados por edad usando una cola de prioridad.
  Args:
    datasource: Origen de datos.
  """
  events = process_incidents_by_age(datasource)
  queue = deque(events)

  print("La cola con la prioridad por 'Edad' es:")
  print("")

  # Definir los encabezados de la tabla
  headers = ["ID", "Timestamp", "Age", "Category", "Priority", "Origin", "Destination", "Description"]
  rows = []

  while queue:
    event = queue.popleft()

    rows.append([
      event.id,
      str(event.timestamp),
      event.age,
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description
    ])

  print_results(headers, rows)

  time = timeit.timeit(
    lambda: process_incidents_by_age(datasource),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_age(datasource):
  """Obtiene y ordena eventos pendientes por antiguedad descendente. Usa sorted()
  Args:
    datasource: Origen de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados del mas antiguo al mas reciente.
  """
  events = datasource.get_not_resolved_events()
  events_sorted = sorted(events, key=lambda e: e.age, reverse=True)

  return events_sorted

def show_incidents_by_age_insertionsort(datasource):
  """Muestra los eventos ordenados por edad usando una cola de prioridad. Usa el algoritmo insertion sort
  Args:
    datasource: Origen de datos.
  """
  events = process_incidents_by_age_insertionsort(datasource)

  print("La cola con la prioridad por 'Edad' es:")
  print("")

  headers = ["ID", "Timestamp", "Age", "Category", "Priority", "Origin", "Destination", "Description"]
  rows = []

  for event in events:
    rows.append([
      event.id,
      str(event.timestamp),
      event.age,
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description
    ])

  print_results(headers, rows)

  time = timeit.timeit(
    lambda: process_incidents_by_age_insertionsort(datasource),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_age_insertionsort(datasource):
  """Obtiene y ordena eventos pendientes por antiguedad usando insertion sort.
  Args:
    datasource: Origen de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por antiguedad.
  """
  events = datasource.get_not_resolved_events()
  events_sorted = insertion_sort(events, False)

  return events_sorted

def resolve_next_priority_incident(datasource):
  """Resuelve el siguiente incidente segun prioridad y antiguedad.
  Args:
    datasource: Origen de datos.
  """
  heap = PriorityHeap()

  events = datasource.get_not_resolved_events(datasource)

  for event in events:
    heap.insert(event, event.priority, -event.age)

  if heap.emptyheap():
    print("La cola de incidentes está vacía.")
    return

  event, _ = heap.pickmax()

  print(f"Atendiendo el incidente {event.id}")
  print(f"Quedan por atender {heap.heaplength()} eventos.")
  print("")

  datasource.set_incident_status(event.id, "resolved")

def resolve_older_incident(datasource):
  """Resuelve el incidente pendiente mas antiguo.
  Args:
    datasource: Origen de datos.
  """
  heap = PriorityHeap()

  events = datasource.get_not_resolved_events()

  for event in events:
    heap.insert(event, event.age)

  if heap.emptyheap():
    print("La cola de incidentes está vacía.")
    return

  event, _ = heap.pickmax()

  print(f"Atendiendo el incidente {event.id} (más antiguo)")
  print(f"Quedan por atender {heap.heaplength()} eventos.")
  print("")

  datasource.set_incident_status(event.id, "resolved")

def find_incident_by_id_sequential(datasource, id):
  """Busca un incidente por ID con busqueda secuencial y muestra el resultado.
  Args:
    datasource: Origen de datos
    id: Identificador del incidente a buscar.
  """
  events = datasource.get_events()
  comparisons = 0
  foundevent = None

  for event in events:
    comparisons += 1

    if event.id == id:
      foundevent = event
  
  print("")

  if(foundevent == None):
    print(f"El incidente con el ID indicado no existe. Se realizaron {comparisons} comparaciones.")
    print("")
  else:
    print(f"Se encontró el incidente después de {comparisons} comparaciones:")
    print("")

    # Definir los encabezados de la tabla
    headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description", "Status"]
    rows = []

    rows.append([
      event.id,
      str(event.timestamp),
      event.age,
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description,
      event.status
    ])

    print_results(headers, rows)

def find_incident_by_id_binary(datasource, id):
  """Busca un incidente por ID con busqueda binaria y muestra el resultado.
  Args:
    datasource: Origen de datos
    id: Identificador del incidente a buscar.
  """
  events = datasource.get_events()

  events.sort(key=lambda e: e.id)

  foundevent, comparisons = bs(events, id)

  print("")

  if foundevent == -1 or foundevent == None:
    print(f"El incidente con el ID indicado no existe. Se realizaron {comparisons} comparaciones.")
    print("")
  else:
    print(f"Se encontró el incidente después de {comparisons} comparaciones:")
    print("")

    # Definir los encabezados de la tabla
    headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description", "Status"]
    rows = []

    rows.append([
      foundevent.id,
      str(foundevent.timestamp),
      foundevent.age,
      foundevent.category,
      foundevent.priority,
      foundevent.origin,
      foundevent.destination,
      foundevent.description,
      foundevent.status
    ])

    print_results(headers, rows)

def find_incident_by_id_indexes(datasource, id):
  """Busca un incidente por ID usando un indice en memoria y muestra el resultado.
  Args:
    datasource: Origen de datos
    id: Identificador del incidente a buscar.
  """
  events = datasource.get_events()

  index = build_index_by_id(events)

  event = index.get(id)

  print("")

  if event is None:
    print(f"El incidente con el ID indicado no existe")
    print("")
  else:
    print(f"Se encontró el incidente:")
    print("")

    # Definir los encabezados de la tabla
    headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description", "Status"]
    rows = []

    rows.append([
      event.id,
      str(event.timestamp),
      event.age,
      event.category,
      event.priority,
      event.origin,
      event.destination,
      event.description,
      event.status
    ])

    print_results(headers, rows)

def find_incident_by_id_avl(datasource, event_id, show_tree):
  """
  Busca un incidente utilizando un Árbol AVL.

  Args:
    datasource: Fuente de datos activa.
    event_id: ID a buscar.
  """

  # Obtiene todos los eventos
  events = datasource.get_events()

  # Construye el árbol AVL
  tree = build_event_avl(events)

  if show_tree:
    print("\nÁrbol AVL generado:\n")

    tree.print_tree()

  # Busca el evento
  event = tree.search(event_id)

  print()

  if event is None:
    print(f"No existe un incidente con ID {event_id}")

  else:
    print(f"Incidente encontrado:")
    print(f"ID: {event.id}")
    print(f"Categoría: {event.category}")
    print(f"Prioridad: {event.priority}")
    print(f"Descripción: {event.description}")
    print(f"Origen: {event.origin}")
    print(f"Destino: {event.destination}")

  print()

  return event

def build_graph(datasource):
  routes = []

  db_routes = datasource.get_routes()

  for route in db_routes:
    routes.append(
      (
        route.id,
        route.origin_id,
        route.destination_id,
        route.distance,
        route.time
      )
    )

  return create_graph(routes)

def find_path_bfs(datasource, source, destination):
  graph = build_graph(
    datasource
  )

  draw_graph(graph)

  result = find_bfs(graph, source, destination)

  print()

  print("Recorrido BFS: ", result)

  print()

def find_path_dfs(datasource, source, destination):
  graph = build_graph(
    datasource
  )

  draw_graph(graph)

  result = find_dfs(graph, source, destination)

  print()

  print("Recorrido DFS: ", result)

  print()

def explore_bfs(datasource):

  graph = build_graph(
    datasource
  )

  city = input(
    "Ciudad origen: "
  )

  result = bfs(
    graph,
    city
  )

  print()

  print("Recorrido BFS")

  print(result)

  print()

def explore_dfs(datasource):

  graph = build_graph(
    datasource
  )

  city = input(
    "Ciudad origen: "
  )

  result = recursive_dfs(
    graph,
    city
  )

  print()

  print("Recorrido DFS")

  print(result)

  print()

def shortest_route(datasource, source, destination):
  graph = build_graph(
    datasource
  )

  draw_graph(graph)

  distance, path = find_path_dijkstra(graph, source, destination)

  print()
  print(f"Menor camino entre ciudades: {source} - {destination}")
  print()
  print(f"Recorrido: {path}")
  print(f"Distancia total: {distance} KM")
  print()

def minimum_spanning_tree(datasource):
  graph = build_graph(
    datasource
  )

  city = input(
    "Ciudad inicial: "
  )

  mst = prim(
    graph,
    city
  )

  print()

  print("Árbol de expansión mínima")

  for edge in mst:
    print(edge)

  print()

def create_route(datasource):
  print()
  print("Creación de ruta")
  print()

  cities = datasource.get_cities()

  origin = pick_city(cities, "Ciudad origen: ")
  destination = pick_city( cities, "Ciudad destino: ")

  distance = float(
    input(
      "Distancia (km): "
    )
  )

  time = float(
    input(
      "Tiempo (min): "
    )
  )

  route = Route(
    None,
    origin,
    destination,
    distance,
    time
  )

  route_id = datasource.insert_route(
    route
  )

  print()
  print(
    f"Ruta creada correctamente. ID={route_id}"
  )

  print()

def main():
  """Ejecuta el menú principal del sistema de gestión de incidentes."""

  datasource = DataSource(use_database=False)

  print("Modo de ejecución:")
  print("1 - PostgreSQL")
  print("2 - Memoria")

  option = input("Seleccione una opción: ")

  if option == "1":
    conn = conectar()

    datasource = DataSource(
        use_database=True,
        conn=conn
    )

  else:
    datasource = DataSource(
        use_database=False
    )

  conn = None

  print("Bienvenido el sistema de gestión de incidentes")
  print("")

  while True:
    print("Elija una opción para continuar:")
    print("")
    print("01 - Ver todos los eventos pendientes.")
    print("02 - Crear un evento.")
    print("03 - Eventos ordenados por su prioridad (sorted).")
    print("04 - Eventos ordenados por su prioridad (quick sort).")
    print("05 - Eventos ordenados por antigüedad (sorted).")
    print("06 - Eventos ordenados por antigüedad (insertion sort).")
    print("07 - Atender siguiente incidente por prioridad")
    print("08 - Atender siguiente incidente más antiguo")
    print("09 - Buscar incidente por ID (secuencial)")
    print("10 - Buscar incidente por ID (binaria)")
    print("11 - Buscar incidente por ID (índices)")
    print("12 - Crear ciudad")
    print("13 - Buscar incidente por AVL")
    print("14 - Buscar camino con BFS")
    print("15 - Buscar camino con DFS")
    print("16 - Buscar camino más corto con Dijkstra")
    print("17 - Buscar caminos más cortos con Prim")
    print("18 - Crear ruta")
    print("XX - Salir del sistema.")
    print("")

    option = input("Opción elegida: ")

    print("")

    if option == "01" or option == "1":
      show_pending_event_list(datasource)

    elif option == "02" or option == "2":
      create_event(datasource)

    elif option == "03" or option == "3":
      show_incidents_by_priority(datasource)

    elif option == "04" or option == "4":
      show_incidents_by_priority_quicksort(datasource)

    elif option == "05" or option == "5":
      show_incidents_by_age(datasource)

    elif option == "06" or option == "6":
      show_incidents_by_age_insertionsort(datasource)

    elif option == "07" or option == "7":
      resolve_next_priority_incident(datasource)

    elif option == "08" or option == "8":
      resolve_older_incident(datasource)

    elif option == "09" or option == "9":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_sequential(datasource, id)

    elif option == "10":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_binary(datasource, id)

    elif option == "11":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_indexes(datasource, id)

    elif option == "12":
      create_city(datasource)

    elif option == "13":
      event_id = int(input("Ingrese el ID del incidente: "))

      find_incident_by_id_avl(
        datasource,
        event_id,
        True
      )

    elif option == "14":
      event_id = int(input("Ingrese el ID del incidente: "))

      incident = find_incident_by_id_avl(
        datasource,
        event_id,
        False
      )

      if incident is not None:
        find_path_bfs(datasource, incident.origin, incident.destination)

    elif option == "15":
      event_id = int(input("Ingrese el ID del incidente: "))

      incident = find_incident_by_id_avl(
        datasource,
        event_id,
        False
      )

      if incident is not None:
        find_path_dfs(datasource, incident.origin, incident.destination)

    elif option == "16":
      event_id = int(input("Ingrese el ID del incidente: "))

      incident = find_incident_by_id_avl(
        datasource,
        event_id,
        False
      )

      if incident is not None:
        shortest_route(datasource, incident.origin, incident.destination)

    elif option == "17":
      minimum_spanning_tree(datasource)

    elif option == "18":
      create_route(datasource)

    elif option.upper() == "XX":
      break

    else:
      print(f"'{option}' no es una opción válida.")

  print("Gracias por utilizar el sistema de gestión de incidentes.")
  print("")

if __name__ == "__main__":
  main()