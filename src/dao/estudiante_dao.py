import __future__
import mysql.connector
from typing import Optional, List
from config.db_conn import DBConn
from src.dao.interfaces.i_estudiante_dao import IEstudianteDAO
from src.domain.estudiante import Estudiante

class EstudianteDAO(IEstudianteDAO):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia, actualizacion y eliminación de objetos Estudiante.
    """
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.obtener_nombre_db()
        
    def listar_estudiantes_por_curso(self, id_curso) -> List[Estudiante]:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_estudiante, nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante
                    FROM Estudiante
                    WHERE id_curso = %s
                """
                cursor.execute(query, (id_curso,))
                rows = cursor.fetchall()
                if rows is None:
                    return []
                return [Estudiante(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
            except mysql.connector.Error as err:
                raise err
    
    def obtener_estudiante(self, id_estudiante: int) -> Estudiante | None:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_estudiante, nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante
                    FROM Estudiante
                    WHERE id_estudiante = %s
                """
                cursor.execute(query, (id_estudiante,))
                row = cursor.fetchone()
                if row is None:
                    return None
                return Estudiante(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5]
                )
            except mysql.connector.Error as err:
                raise err
