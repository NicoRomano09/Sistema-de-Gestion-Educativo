import __future__
from abc import ABC, abstractmethod
from typing import Optional, Any
from domain.docente import Docente

class IDocenteDAO(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Docente.
    """
    @abstractmethod
    def registrar_docente(docente: Docente) -> int:
        pass
    
    @abstractmethod
    def obtener_docente(id_docente: int) -> Optional[Any]:
        pass
    
    @abstractmethod
    def obtener_docente_por_email(email: str) -> Optional[Any]:
        pass