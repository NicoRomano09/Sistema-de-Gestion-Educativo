import __future__
import re
import bcrypt

class Docente:
    """
    Esta entidad representa a un docente, maestro o profesor que imparte clases de una especialidad o
    asignatura en un curso para un grupo de estudiantes.
    """
    def __init__(
        self, 
        id_docente: int | None, 
        nombre_docente: str, 
        apellido_docente: str,
        email: str,
        contrasena: str
        ):
        self.__id_docente = id_docente
        self.__nombre_docente = nombre_docente
        self.__apellido_docente = apellido_docente
        self.__email = email
        self.__contrasena_hash = contrasena
        
        self.id_asignaturas = []
        self.id_cursos = []
        self.id_divisiones = []
        
    @property
    def id_docente(self) -> int:
        return self.__id_docente
    
    @property
    def nombre_docente(self) -> str:
        return self.__nombre_docente
    
    @nombre_docente.setter
    def nombre_docente(self, nuevo_nombre: str):
        if not isinstance(nuevo_nombre, str):
            raise TypeError("El nuevo nombre del docente debe ser ingresado en string/cadena de texto para ser válido.")
        self.__nombre_docente = nuevo_nombre
                
    @property
    def apellido_docente(self) -> str:
        return self.__apellido_docente
    
    @apellido_docente.setter
    def apellido_docente(self, nuevo_apellido: str):
        if not isinstance(nuevo_apellido, str):
            raise TypeError("El nuevo apellido del docente debe ser ingresado en string/cadena de texto para ser válido.")
        self.__apellido_docente = nuevo_apellido
        
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, nuevo_email: str):
        regex = r'^[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}$'
        if not re.match(regex, nuevo_email):
            raise ValueError("El nuevo email ingresado no es válido.")
        self.__email = nuevo_email
    
    @property
    def contrasena_hash(self) -> str:
        return self.__contrasena_hash
    
    @contrasena_hash.setter
    def contrasena_hash(self, nueva_contrasena):
        if len(nueva_contrasena) < 8:
            raise ValueError("La contraseña ingresada debe contener 8 carácteres o mas.")
        if not any(c.isdigit() for c in nueva_contrasena):
            raise ValueError("La contraseña debe incluir un número.")
        
        # Encriptar y guardar
        hashed = bcrypt.hashpw(nueva_contrasena.encode("utf-8"), bcrypt.gensalt())
        self.__contrasena_hash = hashed.decode("utf-8")
        
    def verificar_contrasena(self, contrasena_plana: str):
        return bcrypt.checkpw(
            contrasena_plana.encode("utf-8"),
            self.__contrasena_hash.encode("utf-8")
        )
    
    def agregar_id_asignaturas(self, id_nueva_asignatura: int):
        if not isinstance(id_nueva_asignatura, int):
            raise TypeError("El ID de la nueva asignatura debe ser ingresado como int/entero para ser válido.")
        self.id_asignaturas.append(id_nueva_asignatura)

    def agregar_id_cursos(self, id_nuevo_curso: int):
        if not isinstance(id_nuevo_curso, int):
            raise TypeError("El ID del nuevo curso debe ser ingresado como int/entero para ser válido.")
        self.id_cursos.append(id_nuevo_curso)
        
    def agregar_id_divisiones(self, id_nueva_division: int):
        if not isinstance(id_nueva_division, int):
            raise TypeError("El ID de la nueva división debe ser ingresado como int/entero para ser válido.")
        self.id_divisiones.append(id_nueva_division)
        
    def mostrar_datos_docente(self) -> str:
        return (
            f"DATOS DEL DOCENTE\n"
            f"ID: {self.id_docente}\n"
            f"Nombre y Apellido: {self.nombre_docente} {self.apellido_docente}\n"
        )
