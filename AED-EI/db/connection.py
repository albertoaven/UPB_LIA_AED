import psycopg2
from config import DB_CONFIG

def conectar():
    """Crea y devuelve una conexion a la base de datos PostgreSQL.

    Returns:
        connection: Objeto de conexion generado por psycopg2.
    """
    return psycopg2.connect(**DB_CONFIG)