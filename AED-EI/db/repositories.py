from models.city import City
from models.route import Route
from models.event import Event
from db.queries import retrieve_cities, retrieve_events, retrieve_event, retrieve_routes, db_insert_event

def get_cities(conn):
  with conn.cursor() as cursor:
    rows = retrieve_cities(cursor)

  cities = [City(*r) for r in rows]

  return cities

def get_routes(conn):
  with conn.cursor() as cursor:
    rows = retrieve_routes(cursor)

  routes = [Route(*r) for r in rows]

  return routes

def get_events(conn):
  with conn.cursor() as cursor:
    rows = retrieve_events(cursor)

  events = [Event(*r) for r in rows]

  return events

def get_event(conn, id):
  with conn.cursor() as cursor:
    row = retrieve_event(cursor, id)

  if row is None:
    return None
  else:
    return Event(*row)

def insert_event(conn, event):
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