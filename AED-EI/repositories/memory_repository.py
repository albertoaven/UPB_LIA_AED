from models.city import City
from models.route import Route

class MemoryRepository:
  def __init__(self):
    self.cities = [
        City(1, "Córdoba", -31.399, -64.183),
        City(2, "Río Ceballos", -31.167, -64.317),
        City(3, "Villa Allende", -31.295, -64.295),
        City(4, "La Cumbre", -30.982, -64.491)
    ]

    self.routes = [
          Route(
            1,
            1,  # origen
            2,  # destino
            35, # distancia
            40  # tiempo
          ),
          Route(
            2,
            2,
            3,
            12,
            15
          ),
          Route(
            3,
            3,
            4,
            50,
            55
          )
        ]

    self.events = []

    self.next_event_id = 1

  # ----------------------
  # CIUDADES
  # ----------------------

  def get_cities(self):
    return self.cities

  def add_city(self, name, latitude, longitude):

    city_id = max([c.id for c in self.cities],default=0) + 1

    city = City(city_id, name, latitude, longitude)

    self.cities.append(city)

    return city_id

  # ----------------------
  # EVENTOS
  # ----------------------

  def insert_event(self, event):
    event.id = self.next_event_id
    self.next_event_id += 1

    event.status = "pending"

    self.events.append(event)

    return event.id

  def get_events(self):
    return self.events

  def get_not_resolved_events(self):
    return [
        e
        for e in self.events
        if getattr(e, "status", "pending") == "pending"
    ]

  def set_incident_status(self, event_id, status):
    for event in self.events:
        if event.id == event_id:
            event.status = status
            return True

    return False
  
  def get_routes(self):
    return self.routes
  
  def insert_route(self, route):
    route.id = self.next_route_id

    self.routes.append(route)

    self.next_route_id += 1

    return route.id