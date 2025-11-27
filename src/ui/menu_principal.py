import __future__
from ui.menu_gestion_estudiantes import menu_estudiantes
from ui.menu_gestion_calificaciones import menu_calificaciones
from ui.menu_gestion_docente import menu_docente
from services.gestor_estudiantes import GestorEstudiantes
from services.gestor_calificaciones import GestorCalificaciones
from dao.estudiante_dao import EstudianteDAO
from dao.calificacion_dao import CalificacionDAO

def menu_principal(session):
    print(f"Bienvenido {session} - Sistema de Gestión Educativo\n")
    dao_estudiante = EstudianteDAO()
    dao_calificacion = CalificacionDAO()
    gestor_estudiantes = GestorEstudiantes(dao_estudiante)
    gestor_calificaciones = GestorCalificaciones(dao_calificacion)
    while True:
        print("Menú Principal")
        print("1. Ver Estudiantes")
        print("2. Gestionar Calificaciones")
        print("3. Ver Mis Datos")
        print("4. Salir")
        opcion = input(">: ")
        
        if opcion == "1":
            menu_estudiantes(session, gestor_estudiantes: GestorEstudiantes)
        elif opcion == "2":
            menu_calificaciones(session, gestor_calificaciones: GestorCalificaciones)
        elif opcion == "3":
            menu_docente(session['id_docente'])
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema.\n")
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intentelo de nuevo.")
