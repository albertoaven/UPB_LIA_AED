def build_index_by_id(events):
    """Construye un indice en memoria de eventos por su identificador.

    Args:
        events: Coleccion de eventos que contienen el atributo `id`.

    Returns:
        dict: Diccionario con clave `id` y valor el objeto evento.
    """
    index = {}

    for event in events:
        index[event.id] = event

    return index