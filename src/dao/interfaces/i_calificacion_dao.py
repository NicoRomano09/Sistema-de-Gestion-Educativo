import __future__
from abc import ABC, abstractmethod
from typing import Optional, Any, List
from domain.calificacion import Calificacion

class ICalificacionDAO(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Calificacion.
    """
    @abstractmethod
    def asignar_calificacion(calificacion: Calificacion) -> int:
        pass
    
    @abstractmethod
    def obtener_calificacion(id_calificacion: int) -> Optional[Any]:
        pass
    
    @abstractmethod
    def listar_calificaciones_por_id_estudiante(id_estudiante: int) -> List[Any]:
        pass
    
    @abstractmethod
    def modificar_calificacion(calificacion: Calificacion) -> int:
        pass
    
    @abstractmethod
    def eliminar_calificacion(id_calificacion: int):
        pass