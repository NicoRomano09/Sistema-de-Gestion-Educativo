import __future__
from typing import Optional, List
from config.db_conn import DBConn
from dao.interfaces.i_estudiante_dao import IEstudianteDao
from domain.estudiante import Estudiante

class EstudianteDAO(IEstudianteDao):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia, actualizacion y eliminación de objetos Estudiante.
    """
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.obtener_nombre_db()
        
    def listar_estudiantes(self) -> List[Estudiante]:
        pass
    
    def obtener_estudiante(self, id_estudiante: int) -> Estudiante | None:
        pass    
