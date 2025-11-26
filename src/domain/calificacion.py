import __future__
from typing import List
from datetime import date

class Calificacion:
    """
    Esta entidad representa calificaciones de los estudiantes en las diferentes
    asignaturas.
    """
    def __init__(
        self, 
        id_calificacion: int | None,
        id_estudiante: int,
        id_asignatura: int,
        nota: int,
        fecha: date,
        descripcion: str
        ):
        self.__id_calificacion = id_calificacion
        self.__id_estudiante = id_estudiante
        self.__id_asignatura = id_asignatura
        self.__nota = nota
        self.__fecha = fecha
        self.__descripcion = descripcion
        
    @property
    def id_calificacion(self) -> int:
        return self.__id_calificacion
    
    @property
    def id_estudiante(self) -> int:
        return self.__id_estudiante
    
    @id_estudiante.setter
    def id_estudiante(self, nuevo_id_estudiante: int):
        if not isinstance(nuevo_id_estudiante, int):
            return TypeError("El nuevo id de estudiante debe ingresarse como int/entero para ser válido.")
        self.__id_estudiante = nuevo_id_estudiante
        
    @property
    def id_asignatura(self) -> int:
        return self.__id_asignatura
    
    @id_asignatura.setter
    def id_asignatura(self, nuevo_id_asignatura: int):
        if not isinstance(nuevo_id_asignatura, int):
            return TypeError("El nuevo id de asignatura debe ingresarse como int/entero para ser válido.")
        self.__id_asignatura = nuevo_id_asignatura
    
    @property
    def nota(self) -> int:
        return self.__nota
    
    @nota.setter
    def nota(self, nueva_nota: int):
        if not isinstance(nueva_nota, int):
            return TypeError("La nueva nota debe ingresarse como int/entero para ser válida.")
        self.__nota = nueva_nota
        
    @property
    def descripcion(self) -> str:
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str):
        if not isinstance(nueva_descripcion, str):
            return TypeError("La nueva descripción debe ingresarse en string/cadena de texto para ser válida.")

    @property
    def fecha(self) -> date:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, nueva_fecha: date):
        if not isinstance(nueva_fecha, date):
            return TypeError("La nueva fecha debe ser un objeto 'datetime.date' para ser válida.")
        self.__fecha = nueva_fecha
        
    def mostrar_datos_calificacion(self):
        return (
            "DATOS DE LA CALIFICACION\n"
            f"ID Calificación: {self.id_calificacion}\n"
            f"ID Estudiante: {self.id_estudiante}\n"
            f"ID Asignatura: {self.id_asignatura}\n"
            f"Nota: {self.nota}"
            f"Fecha: {self.fecha}"
            f"Descripción: {self.descripcion}"
        )