def retrieve_cities(cursor):
    cursor.execute("""
        SELECT id, name, latitude, longitude FROM cities
    """)
    return cursor.fetchall()

def retrieve_routes(cursor):
    cursor.execute("""
        SELECT c1.name, c2.name, r.distance, r.time
        FROM routes r
        JOIN cities c1 ON r.origin_id = c1.id
        JOIN cities c2 ON r.destination_id = c2.id
    """)
    return cursor.fetchall()

def retrieve_events(cursor):
    cursor.execute("""
        SELECT
            i.id, 
            i.timestamp, 
            i.category, 
            i.priority, 
            i.description, 
            o.name AS origin,
            d.name AS destination,
            i.status
        FROM public.incidents i
        INNER JOIN public.cities o ON i.origin_id = o.id
        INNER JOIN public.cities d ON i.destination_id = d.id
    """)

    return cursor.fetchall()

def retrieve_not_resolved_events(cursor):
    cursor.execute("""
        SELECT
            i.id, 
            i.timestamp, 
            i.category, 
            i.priority, 
            i.description, 
            o.name AS origin,
            d.name AS destination,
            i.status
        FROM public.incidents i
        INNER JOIN public.cities o ON i.origin_id = o.id
        INNER JOIN public.cities d ON i.destination_id = d.id
        WHERE status != 'resolved';
    """)

    return cursor.fetchall()

def retrieve_event(cursor, id):
    cursor.execute("""
        SELECT
            i.id, 
            i.timestamp, 
            i.category, 
            i.priority, 
            i.description, 
            o.name AS origin,
            d.name AS destination,
            i.status
        FROM public.incidents i
        INNER JOIN public.cities o ON i.origin_id = o.id
        INNER JOIN public.cities d ON i.destination_id = d.id
        WHERE i.id = %s;
    """, (id,))

    row = cursor.fetchone()
    
    if row is None:
        return None
    else:
        return row

def db_insert_event(cursor, data):
    cursor.execute("""
        INSERT INTO incidents (timestamp, category, priority, description, origin_id, destination_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """, data)

    return cursor.fetchone()[0]

def update_incident_status(cursor, incident_id, status):
    cursor.execute("""
        UPDATE incidents
        SET status = %s
        WHERE id = %s
    """, (status, incident_id))
