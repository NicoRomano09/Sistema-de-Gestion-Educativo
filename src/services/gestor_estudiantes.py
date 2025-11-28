import __future__
from typing import List
from src.dao.estudiante_dao import EstudianteDAO
from src.domain.estudiante import Estudiante

class GestorEstudiantes:
    """
    Este gestor se encarga de gestionar la lógica de negocio para la clase Estudiante.
    """
    def __init__(self, dao: EstudianteDAO):
        self.dao = dao
    
    def listar_estudiantes_por_curso(self, id_curso: int) -> List[Estudiante]:
        if not isinstance(id_curso, int):
            raise TypeError("El ID del curso debe ser ingresado como entero.")
        
        if id_curso <= 0:
            raise ValueError("El valor ingresado debe ser mayor a 0.")
        
        return self.dao.listar_estudiantes_por_curso(id_curso) 
    
    def obtener_estudiante(self, id_estudiante: int) -> Estudiante | None:
        if not isinstance(id_estudiante, int):
            raise TypeError("El ID del estudiante debe ser ingresado como entero.")
        
        if id_estudiante <= 0:
            raise ValueError("El valor ingresado para el ID estudiante debe ser mayor a 0.")
        
        return self.dao.obtener_estudiante(id_estudiante)
 