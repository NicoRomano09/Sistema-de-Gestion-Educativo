import __future__
from typing import Optional, Any
from dao.interfaces.i_docente_dao import IDocenteDao
from domain.docente import Docente
from config.db_conn import DBConn

class DocenteDAO(IDocenteDao):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia de objetos Docente.
    """
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.obtener_nombre_db()
    
    def registrar_docente(self, docente: Docente) -> int:
        pass
    
    def obtener_docente(self, id_docente: int) -> Docente | None:
        pass
    