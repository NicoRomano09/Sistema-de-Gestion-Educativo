import __future__

class Asignatura:
    """
    Esta entidad representa a la asignatura, matería o especialidad que es impartida por un docente
    en un curso para un grupo de estudiantes.
    """
    def __init__(self, id_asignatura: int, nombre_asignatura: str):
        self.__id_asignatura = id_asignatura
        self.__nombre_asignatura = nombre_asignatura
        
    @property
    def id_asignatura(self) -> int:
        return self.__id_asignatura
    
    @property
    def nombre_asignatura(self) -> str:
        return self.__nombre_asignatura
    
    def mostrar_datos_asignatura(self) -> str:
        return f"Asignatura: {self.nombre_asignatura}"
