from models.city import City
from models.route import Route
from models.event import Event

from db.queries import (
    retrieve_cities,
    retrieve_events,
    retrieve_event,
    retrieve_routes,
    db_insert_event,
    db_insert_route,
    update_incident_status,
    retrieve_not_resolved_events
)

VALID_STATUSES = {'pending', 'in_progress', 'resolved'}


class PostgresRepository:

    def __init__(self, conn):
        self.conn = conn

    def get_events(self):

        with self.conn.cursor() as cursor:
            rows = retrieve_events(cursor)

        return [Event(*r) for r in rows]

    def get_not_resolved_events(self):

        with self.conn.cursor() as cursor:
            rows = retrieve_not_resolved_events(cursor)

        return [Event(*r) for r in rows]

    def get_event(self, event_id):

        with self.conn.cursor() as cursor:
            row = retrieve_event(cursor, event_id)

        if row is None:
            return None

        return Event(*row)

    def insert_event(self, event):

        if not event:
            raise ValueError(
                "No se enviaron los datos del evento para guardar."
            )

        with self.conn.cursor() as cursor:

            data = (
                event.timestamp,
                event.category,
                event.priority,
                event.description,
                event.origin,
                event.destination
            )

            event_id = db_insert_event(cursor, data)

        self.conn.commit()

        return event_id

    def set_incident_status(self, incident_id, status):

        if status not in VALID_STATUSES:
            raise ValueError("Estado inválido")

        with self.conn.cursor() as cursor:
            update_incident_status(
                cursor,
                incident_id,
                status
            )

        self.conn.commit()

    def get_cities(self):

        with self.conn.cursor() as cursor:
            rows = retrieve_cities(cursor)

        return [City(*r) for r in rows]

    def get_routes(self):
        with self.conn.cursor() as cursor:
            rows = retrieve_routes(cursor)

        return [Route(*r) for r in rows]
    
    def insert_route(self, route):
      with self.conn.cursor() as cursor:
        data = (
        route.origin_id,
        route.destination_id,
        route.distance,
        route.time
        )

        route_id = db_insert_route(
        cursor,
        data
        )

        self.conn.commit()

        return route_id