import __future__
from config.db_conn import DBConn
from src.dao.estudiante_dao import EstudianteDAO
from src.services.gestor_estudiantes import GestorEstudiantes

def menu_estudiantes(session):
    print("\nMenú Estudiantes")
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
                if estudiante:
                    print(estudiante.mostrar_datos_estudiante())
                else:
                    print("No se recupero ningún dato.")
            except TypeError:
                print("El ID ingresado es inválido. Intentelo nuevamente.")
            
        elif subopcion == "2":
            try:
                id_curso = int(input("Ingrese el ID del curso: "))
                estudiantes = gestor_estudiantes.listar_estudiantes_por_curso(id_curso)
                if estudiante:
                    print("Lista de estudiantes:")
                    for e in estudiantes:
                        print(e.mostrar_datos_estudiante())  
                else:
                    print("No se recupero ningún dato.")
            except TypeError:
                print("El ID ingresado es inválido. Intentelo nuevamente")
        elif subopcion == "3":
            break
        
        else:
            print('La opción ingresada es inválida.')
