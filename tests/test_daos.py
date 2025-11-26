import pytest 
import mysql.connector
from config.db_conn import DBConn
from mysql.connector import errorcode
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dao.docente_dao import DocenteDAO
from src.domain.docente import Docente
from dao.estudiante_dao import EstudianteDAO
from dao.calificacion_dao import CalificacionDAO
from src.domain.calificacion import Calificacion


@pytest.fixture(scope="module")
def conn():
    db_conn = DBConn("test_config.ini")
    conn = db_conn.conectar_a_mysql()
    try:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_sistema_gestion_educativo")
            cursor.execute("USE test_sistema_gestion_educativo")
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS Docente(
                               id_docente INT AUTO_INCREMENT, 
                               nombre_docente VARCHAR(60) NOT NULL, 
                               apellido_docente VARCHAR(60) NOT NULL, 
                               email VARCHAR(60) NOT NULL UNIQUE, 
                               contrasena_hash VARCHAR(60) NOT NULL, 
                               PRIMARY KEY (id_docente))
                            """)
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS Estudiante(
                            id_estudiante INT AUTO_INCREMENT,
                            nombre_estudiante VARCHAR(60) NOT NULL,
                            apellido_estudiante VARCHAR(60) NOT NULL,
                            id_curso INT NOT NULL,
                            id_division INT NOT NULL,
                            estado_estudiante BOOLEAN NOT NULL,
                            PRIMARY KEY (id_estudiante)
                            )
                           """)
            cursor.execute("""
                           CREATE TABLE IF NOT EXISTS Calificacion(
                            id_calificacion INT AUTO_INCREMENT,
                            id_estudiante INT NOT NULL,
                            id_asignatura INT NOT NULL,
                            nota INT NOT NULL,
                            fecha DATE NOT NULL,
                            descripcion VARCHAR(60),
                            PRIMARY KEY (id_calificacion)
                            )
                           """)
            cursor.execute("DELETE FROM test_sistema_gestion_educativo.Docente")
            cursor.execute("DELETE FROM test_sistema_gestion_educativo.Estudiante")
            cursor.execute("DELETE FROM test_sistema_gestion_educativo.Calificacion")
            
        yield conn
            
        with conn.cursor() as cursor:
            cursor.execute("DROP DATABASE test_sistema_gestion_educativo")
            conn.close()
            
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise("Usuario o Contraseña inválidos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise("La Base de Datos no existe.")
        else:
            raise("Ha ocurrido un error inesperado. Contacte al Administrador.")
    return None

class TestDocenteDAO:
    def test_registrar_docente(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Docente 
                    (nombre_docente, apellido_docente, email, contrasena_hash) 
                    VALUES ('Nico', 'Romano', 'nico@gmail.com', 'nico1234')
                """)
            conn.commit()
            id_generado = cursor.lastrowid
            
        db_conn = DBConn("test_config.ini")
        dao = DocenteDAO(db_conn)
        result = dao.obtener_docente(id_generado)
            
        assert result is not None
        assert isinstance(result, Docente)
        assert result.id_docente == id_generado
        assert result.nombre_docente == "Nico"
        assert result.apellido_docente == "Romano"
        assert result.email == "nico@gmail.com"
    
    def test_obtener_por_email(self, conn):
        db_conn = DBConn("test_config.ini")
        dao = DocenteDAO(db_conn)
        result = dao.obtener_docente_por_email("nico@gmail.com")
        
        assert result is not None
        assert result.id_docente == 1
        assert result.nombre_docente == "Nico"
        assert result.apellido_docente == "Romano"
        assert result.email == "nico@gmail.com"
        assert result.contrasena_hash == "nico1234"
        
class TestEstudianteDAO:
    def test_obtener_estudiante(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Estudiante 
                    (nombre_estudiante, apellido_estudiante, id_curso, id_division, estado_estudiante)
                    VALUES ('Juan', 'Fernandez', 1, 1, True)
                """)
            conn.commit()
            id_generado = cursor.lastrowid
            
        db_conn = DBConn("test_config.ini")
        dao = EstudianteDAO(db_conn)
        result = dao.obtener_estudiante(id_generado)
        
        assert result is not None
        assert result.nombre_estudiante == "Juan"
        assert result.apellido_estudiante == "Fernandez"
        assert result.id_curso == 1
        assert result.id_division == 1
        assert result.estado_estudiante == True
        
    def test_listar_estudiantes_por_curso(self, conn):
        db_conn = DBConn("test_config.ini")
        dao = EstudianteDAO(db_conn)
        result = dao.listar_estudiantes_por_curso(1)
        estudiantes = list(result)
        
        assert len(estudiantes) > 0
        primer_estudiante = estudiantes[0]
        assert primer_estudiante is not None
        assert primer_estudiante.nombre_estudiante == "Juan"
        assert primer_estudiante.apellido_estudiante == "Fernandez"
        assert primer_estudiante.id_curso == 1
        assert primer_estudiante.id_division == 1
        assert primer_estudiante.estado_estudiante == True

class TestCalificacionDAO():
    def test_asignar_calificacion(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Calificacion 
                    (id_estudiante, id_asignatura, nota, fecha, descripcion)
                    VALUES (1, 1, 10, '2025-11-10', 'Nota parcial')
                """)
            conn.commit()
            id_generada = cursor.lastrowid
        
        db_conn = DBConn("test_config.ini")
        dao = CalificacionDAO(db_conn)
        result = dao.obtener_calificacion(id_generada)
        
        assert result is not None
        assert isinstance(result, Calificacion)
        assert result.id_calificacion == id_generada
        assert result.id_asignatura == 1
        assert result.id_estudiante == 1
        assert result.nota == 10
        assert result.fecha == "2025-11-10"
        assert result.descripcion == "Nota parcial"
    
    def test_listar_calificaciones_por_id_estudiante(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Calificacion 
                    (id_estudiante, id_asignatura, nota, fecha, descripcion)
                    VALUES (1, 1, 8, '2025-11-15', 'Nota final')
                """)
            conn.commit()
            id_generado = cursor.lastrowid
            
        db_conn = DBConn("test_config.ini")
        dao = CalificacionDAO(db_conn)
        result = dao.listar_calificaciones_por_id_estudiante(1)
        calificaciones = list(result)
        
        assert len(calificaciones) > 0
        primer_calificacion = calificaciones[0]
        assert primer_calificacion is not None
        assert primer_calificacion.id_calificacion == id_generado
        assert primer_calificacion.id_asignatura == 1
        assert primer_calificacion.id_estudiante == 1
        assert primer_calificacion.nota == 8
        assert primer_calificacion.descripcion == "Nota final"
    
    def test_modificar_calificacion(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Calificacion 
                    (id_estudiante, id_asignatura, nota, fecha, descripcion)
                    VALUES (1, 1, 7, '2025-11-26', 'Prueba')
                """)
            conn.commit()
            id_generado = cursor.lastrowid
            
        with conn.cursor() as cursor:
            cursor.execute("UPDATE test_sistema_gestion_educativo.Calificacion SET nota = 9 WHERE id_calificacion = %s", (id_generado,))
            conn.commit()
        
        db_conn = DBConn("test_config.ini")
        dao = CalificacionDAO(db_conn)
        result = dao.obtener_calificacion(id_generado)
        
        assert result is not None
        assert result.nota == 9
        
    def test_eliminar_calificacion(self, conn):
        with conn.cursor() as cursor:
            cursor.execute("""
                    INSERT INTO test_sistema_gestion_educativo.Calificacion 
                    (id_estudiante, id_asignatura, nota, fecha, descripcion)
                    VALUES (1, 1, 6, '2025-11-26', 'Examen parcial')
                """)
            conn.commit()
            id_generado = cursor.lastrowid
            
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM test_sistema_gestion_educativo.Calificacion WHERE id_calificacion = %s", (id_generado,))
            conn.commit()
        
        db_conn = DBConn("test_config.ini")
        dao = CalificacionDAO(db_conn)
        result = dao.obtener_calificacion(id_generado)
        
        assert result is None
        