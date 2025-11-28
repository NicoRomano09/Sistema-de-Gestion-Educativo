import __future__
from typing import List
from src.dao.calificacion_dao import CalificacionDAO
from src.domain.calificacion import Calificacion

class GestorCalificaciones:
    """
    Este gestor se encarga de gestionar la lógica de negocio para la clase Calificacion.
    """
    def __init__(self, dao: CalificacionDAO):
        self.dao = dao
    
    def asignar_calificacion(self, calificacion: Calificacion) -> int:
        if not isinstance(calificacion, Calificacion):
            raise TypeError("La calificación ingresada debe ser una instancia de Calificacion.")

        return self.dao.asignar_calificacion(calificacion)
    
    def obtener_calificacion(self, id_calificacion: int) -> Calificacion | None:
        if not isinstance(id_calificacion, int):
            raise TypeError("Debe ingresar un entero para asociar el ID de la calificación.")
        
        if id_calificacion <= 0:
            raise ValueError("Debe ingresar un valor mayor a 0.")
        
        return self.dao.obtener_calificacion(id_calificacion)
        
    def listar_calificaciones_por_id_estudiante(self, id_estudiante: int) -> List[Calificacion]:
        if not isinstance(id_estudiante, int):
            raise TypeError("Debe ingresar un entero para asociar el ID del estudiante.")
        
        if id_estudiante <= 0:
            raise ValueError("Debe ingresar un valor mayor a 0.")

        return self.dao.listar_calificaciones_por_id_estudiante(id_estudiante)
        
    def modificar_calificacion(self, id_calificacion: int, nota = None, descripcion = None) -> int:
        calificacion_actual = self.dao.obtener_calificacion(id_calificacion)
        
        if not calificacion_actual:
            raise ValueError("La calificación no existe.")
        
        if calificacion_actual is not None:
            calificacion_actual.nota = nota
        
        if calificacion_actual is not None:
            calificacion_actual.descripcion = descripcion
        
        return self.dao.modificar_calificacion(calificacion_actual)
    
    def eliminar_calificacion(self, id_calificacion: int):
        if not isinstance(id_calificacion, int):
            raise TypeError("Debe ingresar un entero para asociar el ID de la calificación que desea eliminar")

        if id_calificacion <= 0:
            raise ValueError("Debe ingresar un valor mayor a 0.")
        
        return self.dao.eliminar_calificacion(id_calificacion)

    