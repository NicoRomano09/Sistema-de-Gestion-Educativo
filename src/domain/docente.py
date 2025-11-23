import __future__
from typing import List

class Docente:
    """
    Esta entidad representa a un docente, maestro o profesor que imparte clases de una especialidad o
    asignatura en un curso para un grupo de estudiantes.
    """
    def __init__(
        self, 
        id_docente: int, 
        nombre_docente: str, 
        apellido_docente: str, 
        asignaturas: List[int], 
        cursos: List[int], 
        divisiones: List[int]
        ):
        self.__id_docente = id_docente
        self.__nombre_docente = nombre_docente
        self.__apellido_docente = apellido_docente
        self.__id_asignaturas = asignaturas
        self.__id_cursos = cursos
        self.__id_divisiones = divisiones
        
    @property
    def id_docente(self) -> int:
        return self.__id_docente
    
    @property
    def nombre_docente(self) -> str:
        return self.__nombre_docente
    
    @nombre_docente.setter
    def nombre_docente(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str):
            return TypeError("El nuevo nombre del docente debe ser ingresado en string/cadena de texto para ser válido.")
        self.__nombre_docente = nuevo_nombre
                
    @property
    def apellido_docente(self) -> str:
        return self.__apellido_docente
    
    @apellido_docente.setter
    def apellido_docente(self, nuevo_apellido: str):
        if not isinstance(nuevo_apellido, str):
            return TypeError("El nuevo apellido del docente debe ser ingresado en string/cadena de texto para ser válido.")
        self.__apellido_docente = nuevo_apellido
    
    @property
    def id_asignaturas(self) -> List[int]:
        return self.__id_asignaturas
    
    @id_asignaturas.setter
    def id_asignaturas(self, id_nueva_asignatura: int):
        if not isinstance(id_nueva_asignatura, int):
            return TypeError("El ID de la nueva asignatura debe ser ingresado como int/entero para ser válido.")
        self.__id_asignaturas.append(id_nueva_asignatura)
        
    @property
    def id_cursos(self):
        return self.__id_cursos
    
    @id_cursos.setter
    def id_cursos(self, id_nuevo_curso: int):
        if not isinstance(id_nuevo_curso, int):
            return TypeError("El ID del nuevo curso debe ser ingresado como int/entero para ser válido.")
        self.__id_cursos.append(id_nuevo_curso)
        
    @property
    def id_divisiones(self, id_nueva_division: int):
        if not isinstance(id_nueva_division, int):
            return TypeError("El ID de la nueva división debe ser ingresado como int/entero para ser válido.")
        self.__id_divisiones.append(id_nueva_division)
        
    def mostrar_datos_docente(self) -> str:
        return (
            f"DATOS DEL DOCENTE\n"
            f"ID: {self.id_docente}\n"
            f"Nombre y Apellido: {self.nombre_docente} {self.apellido_docente}\n"
            f"ID Asignatura: {self.id_asignaturas}"
        )
