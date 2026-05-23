import heapq

from db.connection import conectar
from db.repositories import get_events, get_event, insert_event, get_cities
from utils.display import pick_city
from models.event import Event
from services.priority_queue import PriorityHeap

def show_event_list(conn):
    """Muestra en consola todos los eventos almacenados en la base de datos.
    Args:
        conn: Conexión activa a la base de datos.
    """
    events = get_events(conn)

    # Definir los encabezados de la tabla
    headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description"]

    # Convertir eventos a filas
    rows = []
    for e in events:
        rows.append([
            e.id,
            str(e.timestamp),
            e.category,
            e.priority,
            e.origin,
            e.destination,
            e.description
        ])

    # Calcular ancho máximo de cada columna según la cantidad 
    # máxima de caracteres de los valores
    col_widths = []
    for col in zip(headers, *rows):
        col_widths.append(max(len(str(value)) for value in col))

    # Formato de impresión
    def format_row(row):
        return " | ".join(str(val).ljust(width) for val, width in zip(row, col_widths))

    # Imprimir encabezado
    print(format_row(headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Imprimir filas
    for row in rows:
        print(format_row(row))

    print("")

def create_event(conn, heap):
    """Solicita datos por consola, crea un evento y lo persiste en la base.
    Args:
        conn: Conexión activa a la base de datos.
    """

    print("Ingrese los datos del evento: ")
    print("")

    cities = get_cities(conn)

    # Solicitar los datos al usuario
    date = input("Fecha y hora del evento en formato 'YYYY-MM-DD HH:mm': ")
    category = input("Ingrese la categoría del evento: ")
    priority = int(input("Ingrese la prioridad del evento: "))
    description = input("Ingrese la descripción del evento: ")
    origin = pick_city(cities, "Ingrese la ciudad cuidad del origen: ")
    destination = pick_city(cities, "Ingrese la ciudad cuidad de destino: ")

    # Armar el objeto
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

    if result > 0:
        print(f"Evento creado exitosamente (Id = {result})")

        # Añadimos el Id al objeto para añadirlo a la cola
        new_event.id = result

        # Insertamos el evento a la cola de prioridad
        heap.insert(new_event, new_event.priority)

    else:
        print("Hubo un error al crear el evento.")

    print("")

def resolution_by_priority(conn, heap):
    """Muestra los eventos ordenados por prioridad usando una cola de prioridad.
    Args:
        conn: Conexión activa a la base de datos.
    """
    print("La cola con la prioridad por 'Prioridad' es:")
    print("")

    copied_heap = heap.heap.copy()

    # Definir los encabezados de la tabla
    headers = ["ID", "Timestamp", "Category", "Priority", "Origin", "Destination", "Description"]
    rows = []

    while copied_heap:
        priority, _, event = heapq.heappop(copied_heap)

        rows.append([
            event.id,
            str(event.timestamp),
            event.category,
            event.priority,
            event.origin,
            event.destination,
            event.description
        ])

    # Calcular ancho máximo de cada columna según la cantidad 
    # máxima de caracteres de los valores
    col_widths = []
    for col in zip(headers, *rows):
        col_widths.append(max(len(str(value)) for value in col))

    # Formato de impresión
    def format_row(row):
        return " | ".join(str(val).ljust(width) for val, width in zip(row, col_widths))

    # Imprimir encabezado
    print(format_row(headers))
    print("-" * (sum(col_widths) + 3 * (len(headers) - 1)))

    # Imprimir filas
    for row in rows:
        print(format_row(row))

    print("")

def main():
    """Ejecuta el menú principal del sistema de gestión de incidentes."""

    # Declaramos la cola de prioridades que se usa en la aplicación
    heap = PriorityHeap()

    # Tomamos los eventos que ya están registrados y están pendientes.
    events = get_events(conn)

    for event in events:
        heap.insert(event, event.priority)

    print("Bienvenido el sistema de gestión de incidentes")
    print("")

    conn = conectar()

    while True:
        print("Elija una opción para continuar:")
        print("")
        print("01 - Ver todos los eventos.")
        print("02 - Crear un evento.")
        print("03 - Eventos ordenados por su prioridad (columna 'Priority').")
        print("XX - Salir del sistema.")
        print("")

        option = input("Opción elegida: ")

        print("")
    
        if option == "01":
            show_event_list(conn)

        elif option == "02":
            create_event(conn, heap)

        elif option == "03":
            resolution_by_priority(conn)

        elif option.upper() == "XX":
            break

        else:
            print(f"'{option}' no es una opción válida.")

    print("Gracias por utilizar el sistema de gestión de incidentes.")
    print("")

if __name__ == "__main__":
    main()