def retrieve_events(cursor):
    """Recupera todos los incidentes registrados con nombres de ciudades.

    Args:
        cursor: Cursor activo de base de datos.

    Returns:
        list[tuple]: Filas con los datos de incidentes y sus ciudades asociadas.
    """
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
    """Recupera incidentes cuyo estado es distinto de resolved.

    Args:
        cursor: Cursor activo de base de datos.

    Returns:
        list[tuple]: Filas con los datos de incidentes pendientes.
    """
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
    """Recupera un incidente por su identificador.

    Args:
        cursor: Cursor activo de base de datos.
        id: Identificador del incidente.

    Returns:
        tuple | None: Fila del incidente si existe, de lo contrario None.
    """
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
    """Inserta un incidente en la base de datos y devuelve su id.

    Args:
        cursor: Cursor activo de base de datos.
        data: Tupla con timestamp, categoria, prioridad, descripcion,
            id de origen e id de destino.

    Returns:
        int: Identificador generado para el incidente insertado.
    """
    cursor.execute("""
        INSERT INTO incidents (timestamp, category, priority, description, origin_id, destination_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """, data)

    return cursor.fetchone()[0]

def update_incident_status(cursor, incident_id, status):
    """Actualiza el estado de un incidente por su id.

    Args:
        cursor: Cursor activo de base de datos.
        incident_id: Identificador del incidente a actualizar.
        status: Nuevo estado del incidente.
    """
    cursor.execute("""
        UPDATE incidents
        SET status = %s
        WHERE id = %s
    """, (status, incident_id))

def retrieve_cities(cursor):
    """Recupera todas las ciudades desde la base de datos.

    Args:
        cursor: Cursor activo de base de datos.

    Returns:
        list[tuple]: Filas con id, nombre, latitud y longitud de cada ciudad.
    """
    cursor.execute("""
        SELECT id, name, latitude, longitude FROM cities
    """)
    return cursor.fetchall()

def retrieve_routes(cursor):
    """Recupera las rutas entre ciudades con distancia y tiempo.

    Args:
        cursor: Cursor activo de base de datos.

    Returns:
        list[tuple]: Filas con ciudad origen, ciudad destino, distancia y tiempo.
    """
    cursor.execute("""
        SELECT c1.name, c2.name, r.distance, r.time
        FROM routes r
        JOIN cities c1 ON r.origin_id = c1.id
        JOIN cities c2 ON r.destination_id = c2.id
    """)
    return cursor.fetchall()