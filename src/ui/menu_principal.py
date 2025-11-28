import __future__
from src.ui.menu_gestion_estudiantes import menu_estudiantes
from src.ui.menu_gestion_calificaciones import menu_calificaciones
from src.ui.menu_gestion_docente import menu_docente

def menu_principal(session):
    print(f"\nBienvenido - Sistema de Gestión Educativo\n")
    while True:
        print("\nMenú Principal")
        print("1. Ver Estudiantes")
        print("2. Gestionar Calificaciones")
        print("3. Ver Mis Datos")
        print("4. Salir\n")
        opcion = input(">: ")
        
        if opcion == "1":
            menu_estudiantes(session["id_docente"])
        elif opcion == "2":
            menu_calificaciones(session["id_docente"])
        elif opcion == "3":
            menu_docente(session["id_docente"])
        elif opcion == "4":
            print("Gracias por utilizar nuestro sistema.\n")
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intentelo de nuevo.")
