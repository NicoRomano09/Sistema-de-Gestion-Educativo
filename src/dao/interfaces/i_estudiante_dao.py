import __future__
from abc import ABC
from typing import Optional, Any

class IEstudianteDao(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Estudiante.
    """
    @staticmethod
    def listar_estudiantes() -> Optional[Any]:
        pass
    
    @staticmethod
    def obtener_estudiante(id_estudiante: int) -> Optional[Any]:
        pass
    
