import __future__
from typing import Optional, List
from dao.interfaces.i_calificacion_dao import ICalificacionDAO
from domain.calificacion import Calificacion

class CalificacionDAO(ICalificacionDAO):
    """
    Esta entidad se encarga de interactuar con la Base de Datos, 
    permitiendo la persistencia de objetos Calificacion.
    """
    def asignar_calificacion() -> int:
        pass
    
    def obtener_calificacion() -> Calificacion | None:
        pass
    
    def listar_calificaciones() -> List[Calificacion]:
        pass
    
    def modificar_calificacion() -> int:
        pass
    
    def eliminar_calificacion():
        pass