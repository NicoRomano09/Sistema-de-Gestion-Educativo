import __future__

class Curso:
    """
    Esta entidad representa a un curso, grado o año al que asiste un estudiante de acuerdo a su nivel 
    educativo, saberes y edad.
    """
    def __init__(self, id_curso: int | None, nombre_curso: str, id_establecimiento: int):
        self.__id_curso = id_curso
        self.__nombre_curso = nombre_curso
        self.__id_establecimiento = id_establecimiento
    
    @property
    def id_curso(self) -> int:
        return self.__id_curso
    
    @property
    def nombre_curso(self) -> str:
        return self.__nombre_curso
    
    @property
    def id_establecimiento(self) -> int:
        return self.__id_establecimiento
    
    def mostrar_datos_curso(self) -> str:
        return f"Curso: {self.nombre_curso}"
