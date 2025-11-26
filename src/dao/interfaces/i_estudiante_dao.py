import __future__
from abc import ABC
from typing import Optional, Any

class IEstudianteDAO(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Estudiante.
    """
    @staticmethod
    def listar_estudiantes_por_curso(id_curso: int) -> Optional[Any]:
        pass
    
    @staticmethod
    def obtener_estudiante(id_estudiante: int) -> Optional[Any]:
        pass
    
