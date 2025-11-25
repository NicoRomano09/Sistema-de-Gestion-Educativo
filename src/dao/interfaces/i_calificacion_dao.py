import __future__
from abc import ABC, abstractmethod
from typing import Optional, Any, List

class ICalificacionDAO(ABC):
    """
    Interfaz con métodos sin implementar para el DAO de Calificacion.
    """
    @abstractmethod
    def asignar_calificacion() -> int:
        pass
    
    @abstractmethod
    def obtener_calificacion() -> Optional[Any]:
        pass
    
    @abstractmethod
    def listar_calificaciones() -> List[Any]:
        pass
    
    @abstractmethod
    def modificar_calificacion() -> int:
        pass
    
    @abstractmethod
    def eliminar_calificacion():
        pass