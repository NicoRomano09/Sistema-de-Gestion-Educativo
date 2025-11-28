import __future__
from typing import List
from src.domain.curso import Curso
from src.domain.division import Division

class Establecimiento:
    """
    Esta entidad representa el establecimiento, escuela o instituto donde realizan actividades 
    docentes y alumnos.
    """
    def __init__(
        self, 
        id_establecimiento: int | None, 
        nombre_establecimiento: str, 
        nivel_educativo: str, 
        gestion: str, 
        ):
        self.__id_establecimiento = id_establecimiento
        self.__nombre_establecimiento = nombre_establecimiento
        self.__nivel_educativo = nivel_educativo
        self.__gestion = gestion
        
        self.cursos = []
        self.divisiones = []
        
    @property
    def id_establecimiento(self) -> int:
        return self.__id_establecimiento
    
    @property
    def nombre_establecimiento(self) -> str:
        return self.__nombre_establecimiento
    
    @nombre_establecimiento.setter
    def nombre_establecimiento(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nuevo nombre para el establecimiento debe ser ingresado en un string/cadena de texto para ser válido.")
        self.__nombre_establecimiento = nuevo_nombre
    
    @property
    def nivel_educativo(self) -> str:
        return self.__nivel_educativo
    
    @nivel_educativo.setter
    def nivel_educativo(self, nuevo_nivel: str):
        if not isinstance(nuevo_nivel, str):
            raise TypeError("El nuevo nivel educativo para el establecimiento debe ser ingresado en un string/cadena de texto para ser válido.")
        self.__nivel_educativo = nuevo_nivel
        
    @property
    def gestion(self) -> str:
        return self.__gestion
    
    @gestion.setter
    def gestion(self, nueva_gestion: str):
        if not isinstance(nueva_gestion, str):
            raise TypeError("La nueva gestion debe ser ingresada en un string/cadena de texto para ser válido.")
        self.__gestion = nueva_gestion
    
    def agregar_cursos(self, nuevo_curso: Curso):
        if not isinstance(nuevo_curso, Curso):
            raise TypeError("El nuevo curso debe ser una instancia de clase Curso para ser válido.")
        self.cursos.append(nuevo_curso)
    
    def agregar_divisiones(self, nueva_division: Division):
        if not isinstance(nueva_division, Division):
            raise TypeError("La nueva division debe ser una instancia de clase Division para ser válida.")
        self.divisiones.append(nueva_division)
        
    def mostrar_datos_establecimiento(self) -> str:
        return (
            f"DATOS DEL ESTABLECIMIENTO\n"
            f"{self.nombre_establecimiento}\n"
            f"ID Escuela: {self.id_establecimiento}\n"
            f"Nivel: {self.nivel_educativo}\n"
            f"Gestion: {self.gestion}\n"
            f"Cursos: {self.cursos}\n"
            f"Divisiones: {self.divisiones}\n"
            )
