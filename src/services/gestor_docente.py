import __future__
import bcrypt
from typing import Optional
from dao.docente_dao import DocenteDAO
from domain.docente import Docente

class GestorDocente:
    """
    Este gestor se encarga de gestionar la lógica de negocio para la clase Docente.
    """
    def __init__(self, dao: DocenteDAO):
        self.dao = dao
        
    def registrar_docente(self, docente: Docente) -> int:
        if not isinstance(docente, Docente):
            raise TypeError("El docente ingresado debe ser una instancia de Docente.")
        
        return self.dao.registrar_docente(docente)
    
    def login(self, email: str, contrasena_plana: str) -> Optional[dict]:
        docente = self.dao.obtener_docente_por_email(email)
        if not docente:
            return None
        hashed = docente.pop("contrasena", None)
        
        if not hashed:
            return None
        ok = bcrypt.checkpw(contrasena_plana.encode("utf-8"), hashed.encode("utf-8"))
        return docente if ok else None
    
    def obtener_docente(self, id_docente: int) -> Docente | None:
        if not isinstance(id_docente, int):
            raise TypeError("El valor ingresado para asociar el ID docente debe ser un entero.")
        
        if id_docente <= 0:
            raise ValueError("El valor ingresado debe ser mayor a 0.")
        
        return self.dao.obtener_docente(id_docente)
    
    def obtener_docente_por_email(self, email: str) -> Docente | None:
        if not isinstance(email, str):
            return TypeError("El email ingresado debe ser un string/cadena de texto para ser válido.")
        
        return self.dao.obtener_docente_por_email(email)
    