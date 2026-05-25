# --------------- Importación de los módulos a usar en el sistema ---------------
import timeit
from collections import deque
from db.connection import conectar
from db.repositories import get_events, insert_event, get_cities, set_incident_status, get_not_resolved_events
from utils.display import pick_city, format_row, print_results
from models.event import Event
from services.priority_queue import PriorityHeap
from algorithms.bs import bs
from algorithms.quick_sort import quick_sort
from algorithms.insertion_sort import insertion_sort
from services.indexing import build_index_by_id
# --------------- Fin Importación de los módulos a usar en el sistema ------------

def show_pending_event_list(conn):
  """Muestra en consola todos los eventos almacenados en la base de datos.
  Args:
    conn: Conexión activa a la base de datos.
  """
  events = get_not_resolved_events(conn)
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

def create_event(conn):
  """Solicita datos por consola, crea un evento y lo persiste en la base.
  Args:
    conn: Conexión activa a la base de datos.
  """
  print("Ingrese los datos del evento: ")
  print("")

  cities = get_cities(conn)

  date = input("Fecha y hora del evento en formato 'YYYY-MM-DD HH:mm': ")
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
    destination = destination
  )

  result = insert_event(conn, new_event)

  print("")

  if result > 0:
    print(f"Evento creado exitosamente (Id = {result})")
  else:
    print("Hubo un error al crear el evento.")

  print("")

def show_incidents_by_priority(conn):
  """Muestra los eventos ordenados por prioridad usa sorted().
  Args:
    conn: Conexión activa a la base de datos.
  """
  events = process_incidents_by_priority(conn)
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
      lambda: process_incidents_by_priority(conn),
      number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_priority(conn):
  """Obtiene y ordena eventos pendientes por prioridad ascendente.
  Args:
    conn: Conexión activa a la base de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por prioridad.
  """
  events = deque(get_not_resolved_events(conn))
  event_sorted = sorted(events, key=lambda e: e.priority)

  return event_sorted

def show_incidents_by_priority_quicksort(conn):
  """Muestra los eventos ordenados por prioridad usando el algoritmo de ordenamiento quicksort.
  Args:
    conn: Conexión activa a la base de datos.
  """

  events = process_incidents_by_priority_quicksort(conn)

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
    lambda: process_incidents_by_priority_quicksort(conn),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_priority_quicksort(conn):
  """Obtiene y ordena eventos pendientes por prioridad usando quick sort.
  Args:
    conn: Conexión activa a la base de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por prioridad.
  """
  events = deque(get_not_resolved_events(conn))
  event_sorted = quick_sort(events, True)

  return event_sorted

def show_incidents_by_age(conn):
  """Muestra los eventos ordenados por edad usando una cola de prioridad.
  Args:
    conn: Conexión activa a la base de datos.
  """
  events = process_incidents_by_age(conn)
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
    lambda: process_incidents_by_age(conn),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_age(conn):
  """Obtiene y ordena eventos pendientes por antiguedad descendente. Usa sorted()
  Args:
    conn: Conexión activa a la base de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados del mas antiguo al mas reciente.
  """
  events = get_not_resolved_events(conn)
  events_sorted = sorted(events, key=lambda e: e.age, reverse=True)

  return events_sorted

def show_incidents_by_age_insertionsort(conn):
  """Muestra los eventos ordenados por edad usando una cola de prioridad. Usa el algoritmo insertion sort
  Args:
    conn: Conexión activa a la base de datos.
  """
  events = process_incidents_by_age_insertionsort(conn)

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
    lambda: process_incidents_by_age_insertionsort(conn),
    number=50
  )

  print(f"Tiempo total: {time}")
  print(f"Promedio: {time/50}")
  print("")

def process_incidents_by_age_insertionsort(conn):
  """Obtiene y ordena eventos pendientes por antiguedad usando insertion sort.
  Args:
    conn: Conexión activa a la base de datos.
  Returns:
    list[Event]: Eventos pendientes ordenados por antiguedad.
  """
  events = get_not_resolved_events(conn)
  events_sorted = insertion_sort(events, False)

  return events_sorted

def resolve_next_priority_incident(conn):
  """Resuelve el siguiente incidente segun prioridad y antiguedad.
  Args:
    conn: Conexión activa a la base de datos.
  """
  heap = PriorityHeap()

  events = get_not_resolved_events(conn)

  for event in events:
    heap.insert(event, event.priority, -event.age)

  if heap.emptyheap():
    print("La cola de incidentes está vacía.")
    return

  event, _ = heap.pickmax()

  print(f"Atendiendo el incidente {event.id}")
  print(f"Quedan por atender {heap.heaplength()} eventos.")
  print("")

  set_incident_status(conn, event.id, "resolved")

def resolve_older_incident(conn):
  """Resuelve el incidente pendiente mas antiguo.
  Args:
    conn: Conexión activa a la base de datos.
  """
  heap = PriorityHeap()

  events = get_not_resolved_events(conn)

  for event in events:
    heap.insert(event, event.age)

  if heap.emptyheap():
    print("La cola de incidentes está vacía.")
    return

  event, _ = heap.pickmax()

  print(f"Atendiendo el incidente {event.id} (más antiguo)")
  print(f"Quedan por atender {heap.heaplength()} eventos.")
  print("")

  set_incident_status(conn, event.id, "resolved")

def find_incident_by_id_sequential(conn, id):
  """Busca un incidente por ID con busqueda secuencial y muestra el resultado.
  Args:
    conn: Conexión activa a la base de datos.
    id: Identificador del incidente a buscar.
  """
  events = get_events(conn)
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

def find_incident_by_id_binary(conn, id):
  """Busca un incidente por ID con busqueda binaria y muestra el resultado.
  Args:
    conn: Conexión activa a la base de datos.
    id: Identificador del incidente a buscar.
  """
  events = get_events(conn)

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

def find_incident_by_id_indexes(conn, id):
  """Busca un incidente por ID usando un indice en memoria y muestra el resultado.
  Args:
    conn: Conexión activa a la base de datos.
    id: Identificador del incidente a buscar.
  """
  events = get_events(conn)

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

def main():
  """Ejecuta el menú principal del sistema de gestión de incidentes."""

  # Establecemos la conexión a la base de datos
  conn = conectar()

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
    print("XX - Salir del sistema.")
    print("")

    option = input("Opción elegida: ")

    print("")

    if option == "01":
      show_pending_event_list(conn)

    elif option == "02":
      create_event(conn)

    elif option == "03":
      show_incidents_by_priority(conn)

    elif option == "04":
      show_incidents_by_priority_quicksort(conn)

    elif option == "05":
      show_incidents_by_age(conn)

    elif option == "06":
      show_incidents_by_age_insertionsort(conn)

    elif option == "07":
      resolve_next_priority_incident(conn)

    elif option == "08":
      resolve_older_incident(conn)

    elif option == "09":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_sequential(conn, id)

    elif option == "10":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_binary(conn, id)

    elif option == "11":
      id = int(input("Ingrese el ID a buscar: "))

      find_incident_by_id_indexes(conn, id)

    elif option.upper() == "XX":
      break

    else:
      print(f"'{option}' no es una opción válida.")

  print("Gracias por utilizar el sistema de gestión de incidentes.")
  print("")

if __name__ == "__main__":
  main()