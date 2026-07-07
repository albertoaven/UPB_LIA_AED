from repositories.memory_repository import MemoryRepository
from repositories.postgres_repository import PostgresRepository

class DataSource:
  def __init__(self, use_database=False, conn=None):
    if use_database:
      self.repository = PostgresRepository(conn)
    else:
      self.repository = MemoryRepository()

  def get_events(self):
    return self.repository.get_events()

  def insert_event(self, event):
    return self.repository.insert_event(event)

  def get_cities(self):
    return self.repository.get_cities()

  def get_not_resolved_events(self):
    return self.repository.get_not_resolved_events()

  def set_incident_status(self, event_id, status):
    return self.repository.set_incident_status(
        event_id,
        status
    )

  def add_city(self, city_name, latitude, longitude):
    if hasattr(self.repository, "add_city"):
        return self.repository.add_city(city_name, latitude, longitude)

    raise Exception(
        "Agregar ciudades no implementado para PostgreSQL"
    )
  
  def get_routes(self):
    return self.repository.get_routes()
  
  def insert_route(self, route):
    return self.repository.insert_route(route)