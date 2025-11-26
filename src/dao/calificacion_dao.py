import __future__
import mysql.connector
from typing import List
from config.db_conn import DBConn
from dao.interfaces.i_calificacion_dao import ICalificacionDAO
from domain.calificacion import Calificacion

class CalificacionDAO(ICalificacionDAO):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia de objetos Calificacion.
    """
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.obtener_nombre_db()
        
    def asignar_calificacion(self, calificacion: Calificacion) -> int:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    INSERT INTO Calificacion (id_estudiante, id_asignatura, nota, fecha, descripcion)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query, (calificacion.id_estudiante, calificacion.id_asignatura, calificacion.nota, calificacion.fecha, calificacion.descripcion))
                conn.commit()
                id_generada = cursor.lastrowid
                return id_generada
            except mysql.connector.Error as err:
                raise err
            
    def obtener_calificacion(self, id_calificacion: int) -> Calificacion | None:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_calificacion, id_estudiante, id_asignatura, nota, fecha, descripcion
                    FROM Calificacion
                    WHERE id_calificacion = %s
                """
                cursor.execute(query, (id_calificacion,))
                row = cursor.fetchone()
                if row is None:
                    return None
                return Calificacion(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                )
            except mysql.connector.Error as err:
                raise err
    
    def listar_calificaciones_por_id_estudiante(self, id_estudiante: int) -> List[Calificacion]:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    SELECT id_calificacion, id_estudiante, id_asignatura, nota, fecha, descripcion
                    FROM Calificacion
                    WHERE id_estudiante = %s
                """
                cursor.execute(query, (id_estudiante,))
                rows = cursor.fetchall()
                if rows is None:
                    return []
                return [Calificacion(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
            except mysql.connector.Error as err:
                raise err
            
    def modificar_calificacion(self, calificacion: Calificacion) -> int:
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    UPDATE Calificacion 
                    SET id_estudiante = %s, id_asignatura = %s, nota = %s, fecha = %s, descripcion = %s
                    WHERE id_calificacion = %s
                """
                cursor.execute(query, (calificacion.id_estudiante, calificacion.id_asignatura, calificacion.nota, calificacion.fecha, calificacion.descripcion, calificacion.id_calificacion))
                conn.commit()
                return cursor.rowcount > 0 
            except mysql.connector.Error as err:
                raise err
            
    def eliminar_calificacion(self, id_calificacion: int):
        with self.db_conn.conectar_a_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = """
                    DELETE FROM Calificacion WHERE id_calificacion = %s
                """
                cursor.execute(query, (id_calificacion,))
                conn.commit()
                return cursor.rowcount > 0
            except mysql.connector.Error as err:
                raise err