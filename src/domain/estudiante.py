import __future__

class Estudiante:
    """
    Esta entidad representa a un estudiante, alumno o aprendiz que asiste a clases en un 
    establecimiento para adquirir conocimientos.
    """
    def __init__(
        self,
        id_estudiante: int | None,
        nombre_estudiante: str,
        apellido_estudiante: str,
        id_curso: int,
        id_division: int,
        estado_estudiante: bool
        ):
        self.__id_estudiante = id_estudiante
        self.__nombre_estudiante = nombre_estudiante
        self.__apellido_estudiante = apellido_estudiante
        self.__id_curso = id_curso
        self.__id_division = id_division
        self.__estado_estudiante = estado_estudiante
        
    @property
    def id_estudiante(self) -> int:
        return self.__id_estudiante
    
    @property
    def nombre_estudiante(self) -> str:
        return self.__nombre_estudiante
    
    @nombre_estudiante.setter
    def nombre_estudiante(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nuevo nombre para el estudiante debe ser ingresado en string/cadena de texto para ser válido.")
        self.__nombre_estudiante = nuevo_nombre
        
    @property
    def apellido_estudiante(self) -> str:
        return self.__apellido_estudiante
    
    @apellido_estudiante.setter
    def apellido_estudiante(self, nuevo_apellido: str):
        if not isinstance(nuevo_apellido, str):
            raise TypeError("El nuevo apellido para el estudiante debe ser ingresado en string/cadena de texto para ser válido.")

    @property
    def id_curso(self) -> int:
        return self.__id_curso
    
    @id_curso.setter
    def id_curso(self, nuevo_id_curso: int):
        if not isinstance(nuevo_id_curso, int):
            raise TypeError("El nuevo ID de curso para el estudiante debe ser ingresado en int/entero para ser válido.")

    @property
    def id_division(self) -> int:
        return self.__id_division
    
    @id_division.setter
    def id_division(self, nuevo_id_division: int):
        if not isinstance(nuevo_id_division, int):
            raise TypeError("El nuevo ID de la divisón para el estudiante debe ser ingresado en int/entero para ser válido.")
        
    @property
    def estado_estudiante(self) -> bool:
        return self.__estado_estudiante
    
    @estado_estudiante.setter
    def estado_estudiante(self, nuevo_estado: bool):
        if not isinstance(nuevo_estado, bool):
            raise TypeError("El estado del estudiante debe ser ingresado como True/False para ser válido.")
    
    def mostrar_datos_estudiante(self) -> str:
        return (
            "DATOS DEL ESTUDIANTE\n"
            f"ID Estudiante: {self.id_estudiante}\n"
            f"Nombre y Apellido: {self.nombre_estudiante} {self.apellido_estudiante}\n"
            f"ID Curso: {self.id_curso}\n"
            f"ID Division: {self.id_division}\n"
            f"Asistencia: {self.asistencia}%\n"
            f"Estado Estudiante: {self.estado_estudiante}"
        )
    