import __future__

class Division:
    """
    Esta entidad representa a la división (Ej: "A" o "B") de un curso al que asiste un estudiante.
    """
    def __init__(self, id_division: int, nombre_division: str):
        self.__id_division = id_division
        self.__nombre_division = nombre_division
        
    @property
    def id_division(self) -> int:
        return self.__id_division
    
    @property
    def nombre_division(self) -> str:
        return self.__nombre_division
    
    def mostrar_datos_division(self) -> str:
        return f"División: {self.nombre_division}"
