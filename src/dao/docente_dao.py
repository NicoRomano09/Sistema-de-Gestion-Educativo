import __future__
import mysql.connector
from typing import Optional, Any
from src.dao.interfaces.i_docente_dao import IDocenteDAO
from src.domain.docente import Docente
from config.db_conn import DBConn

class DocenteDAO(IDocenteDAO):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia de objetos Docente.
    """
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.obtener_nombre_db()
    
    def registrar_docente(self, docente: Docente) -> int:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO Docente (nombre_docente, apellido_docente, email, contrasena_hash)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(query, (docente.nombre_docente, docente.apellido_docente, docente.email, docente.contrasena_hash))
                conn.commit()
                id_generada = cursor.lastrowid
                return id_generada
            except mysql.connector.Error as err:
                self.db_conn.logger.error(err)
                raise err
            
    def obtener_docente(self, id_docente: int) -> Docente | None:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_docente, nombre_docente, apellido_docente, email, contrasena_hash
                    FROM Docente
                    WHERE id_docente = %s
                """
                cursor.execute(query, (id_docente,))
                row = cursor.fetchone()
                if row is None:
                    return None
                return Docente(
                    row[0], 
                    row[1], 
                    row[2], 
                    row[3], 
                    row[4]
                )
            except mysql.connector.Error as err:
                raise err
            
    def obtener_docente_por_email(self, email: str) -> Docente | None:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_docente, nombre_docente, apellido_docente, email, contrasena_hash
                    FROM Docente
                    WHERE email = %s
                """
                cursor.execute(query, (email,))
                row = cursor.fetchone()
                if row is None:
                    return None
                return Docente(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4]
                )
            except mysql.connector.Error as err:
                raise err
        