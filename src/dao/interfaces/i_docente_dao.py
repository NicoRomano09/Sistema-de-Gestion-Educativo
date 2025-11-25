import __future__
from abc import ABC, abstractmethod
from typing import Optional, Any

class IDocenteDao(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Docente.
    """
    @abstractmethod
    def registrar_docente(nombre_docente: str, apellido_docente: str) -> int:
        pass
    
    @abstractmethod
    def obtener_docente(id_docente: int) -> Optional[Any]:
        pass