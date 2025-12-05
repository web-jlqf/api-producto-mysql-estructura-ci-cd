import os
import time
import mysql.connector
from mysql.connector import Error

def get_connection(retries: int = 5, delay: int = 2):
    """
    Intenta conectarse a MySQL con algunos reintentos.
    retries: número de intentos
    delay: segundos de espera entre intentos
    """
    last_error = None
    for intento in range(1, retries + 1):
        try:
            print(f"[DB] Intento {intento} de conexión a MySQL...")
            conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST", "mysql-productos"),
                user=os.getenv("MYSQL_USER", "web"),
                password=os.getenv("MYSQL_PASSWORD", "web123456"),
                database=os.getenv("MYSQL_DATABASE", "web-dbase"),
            )
            print("[DB] Conexión a MySQL exitosa")
            return conn
        except Error as e:
            print(f"[DB] Error en intento {intento}: {e}")
            last_error = e
            time.sleep(delay)

    # Si no se pudo después de varios intentos, ya sí lanzamos el error
    raise last_error
