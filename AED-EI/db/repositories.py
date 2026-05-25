from models.city import City
from models.route import Route
from models.event import Event
from db.queries import retrieve_cities, retrieve_events, retrieve_event, retrieve_routes, db_insert_event, update_incident_status,retrieve_not_resolved_events

VALID_STATUSES = {'pending', 'in_progress', 'resolved'}

def get_events(conn):
  """Obtiene todos los incidentes y los mapea a objetos Event.

  Args:
    conn: Conexion activa a la base de datos.

  Returns:
    list[Event]: Lista completa de incidentes.
  """
  with conn.cursor() as cursor:
    rows = retrieve_events(cursor)

  events = [Event(*r) for r in rows]

  return events

def get_not_resolved_events(conn):
  """Obtiene los incidentes no resueltos y los mapea a objetos Event.

  Args:
    conn: Conexion activa a la base de datos.

  Returns:
    list[Event]: Lista de incidentes con estado distinto de resolved.
  """
  with conn.cursor() as cursor:
    rows = retrieve_not_resolved_events(cursor)

  events = [Event(*r) for r in rows]

  return events

def get_event(conn, id):
  """Busca un incidente por su identificador.

  Args:
    conn: Conexion activa a la base de datos.
    id: Identificador del incidente.

  Returns:
    Event | None: Evento encontrado o None si no existe.
  """
  with conn.cursor() as cursor:
    row = retrieve_event(cursor, id)

  if row is None:
    return None
  else:
    return Event(*row)

def insert_event(conn, event):
  """Inserta un nuevo incidente en la base de datos.

  Args:
    conn: Conexion activa a la base de datos.
    event: Objeto con los datos del incidente a guardar.

  Returns:
    int: Identificador generado para el incidente insertado.

  Raises:
    ValueError: Si no se recibe un evento valido.
  """
  if not event:
    raise ValueError("No se enviaron los datos del evento para guardar.")
  
  with conn.cursor() as cursor:
    data = (
      event.timestamp,
      event.category,
      event.priority,
      event.description,
      event.origin,
      event.destination
    )

    return db_insert_event(cursor, data)
  
  conn.commit()

def set_incident_status(conn, incident_id, status):
  """Actualiza el estado de un incidente validando estados permitidos.

  Args:
    conn: Conexion activa a la base de datos.
    incident_id: Identificador del incidente a actualizar.
    status: Nuevo estado del incidente.

  Raises:
    ValueError: Si el estado no pertenece a los valores permitidos.
  """
  if status not in VALID_STATUSES:
    raise ValueError("Estado inválido")

  with conn.cursor() as cursor:
    update_incident_status(cursor, incident_id, status)

  conn.commit()

def get_cities(conn):
  """Obtiene todas las ciudades y las mapea a objetos City.

  Args:
    conn: Conexion activa a la base de datos.

  Returns:
    list[City]: Lista de ciudades recuperadas.
  """
  with conn.cursor() as cursor:
    rows = retrieve_cities(cursor)

  cities = [City(*r) for r in rows]

  return cities

def get_routes(conn):
  """Obtiene todas las rutas y las mapea a objetos Route.

  Args:
    conn: Conexion activa a la base de datos.

  Returns:
    list[Route]: Lista de rutas recuperadas.
  """
  with conn.cursor() as cursor:
    rows = retrieve_routes(cursor)

  routes = [Route(*r) for r in rows]

  return routes