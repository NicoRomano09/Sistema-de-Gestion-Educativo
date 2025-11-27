import __future__
from config.db_conn import DBConn
from dao.estudiante_dao import EstudianteDAO
from services.gestor_estudiantes import GestorEstudiantes

def menu_estudiantes():
    print("Menú Estudiantes")
    db_conn = DBConn(config_file='config.ini')
    dao = EstudianteDAO(db_conn)
    gestor_estudiantes = GestorEstudiantes(dao)
    while True:
        print("1. Obtener estudiante")
        print("2. Listar estudiantes por curso")
        print("3. Volver al menú anterior")
        subopcion = input(">")
        
        if subopcion == "1":
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                estudiante = gestor_estudiantes.obtener_estudiante(id_estudiante)
                return (
                    "DATOS DEL ESTUDIANTE"
                    f'ID Estudiante: {estudiante.id_estudiante}'
                    f'Nombre y Apellido: {estudiante.nombre_estudiante} {estudiante.apellido_estudiante}'
                    f'Estado Estudiante: {estudiante.estado_estudiante}'
                    f'ID Curso: {estudiante.id_curso}'
                    f'ID División: {estudiante.id_division}'
                )
            except TypeError:
                return "El ID ingresado es inválido. Intentelo nuevamente."
            
        elif subopcion == "2":
            try:
                id_curso = int(input("Ingrese el ID del curso: "))
                estudiantes = gestor_estudiantes.listar_estudiantes_por_curso(id_curso)
                return (
                    'ESTUDIANTES: \n'
                    f'{estudiantes}'
                    )
            except TypeError:
                return "El ID ingresado es inválido. Intentelo nuevamente"
        
        else:
            return 'La opción ingresada es inválida.'
