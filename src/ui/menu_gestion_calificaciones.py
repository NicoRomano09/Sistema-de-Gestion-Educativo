import __future__
from services.gestor_calificaciones import GestorCalificaciones
from dao.calificacion_dao import CalificacionDAO
from config.db_conn import DBConn
from domain.calificacion import Calificacion
from datetime import datetime, date

def menu_calificaciones():
    print("Menú Calificaciones")
    db_conn = DBConn(config_file='config.ini')
    dao = CalificacionDAO(db_conn)
    gestor_calificacion = GestorCalificaciones(dao)
    while True:
        print("1. Asignar Calificación")
        print("2. Obtener Calificación")
        print("3. Listar calificaciones por id de estudiante")
        print("4. Modificar Calificación")
        print("5. Eliminar Calificación")
        print("6. Volver al menú anterior")
        subopcion = input(">: ")
        
        if subopcion == "1":
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante: "))
                id_asignatura = int(input("Ingrese el ID de la asignatura: "))
                nota = int(input("Ingrese la nota (1-10): "))
                fecha_str = input("Ingrese la fecha de la calificación (Formato Obligatorio: AAAA-MM-DD): ")
                descripcion = input("Ingrese una breve descripción: ")
                
                fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
                calificacion = Calificacion(
                    id_calificacion=None,
                    id_estudiante=id_estudiante, 
                    id_asignatura=id_asignatura, 
                    nota=nota, 
                    fecha=fecha, 
                    descripcion=descripcion
                    )
                id_generada = gestor_calificacion.asignar_calificacion(calificacion)
                print(f"Calificación registrada con éxito con el ID: {id_generada}")
            except TypeError:
                print("Los valores ingresados son inválidos.")
                
        elif subopcion == "2":
            try:
                id_calificacion = int(input("Ingrese el ID de la calificación a buscar: "))
                calificacion_encontrada = gestor_calificacion.obtener_calificacion(id_calificacion)
                
                if calificacion_encontrada:
                    print("DATOS DE LA CALIFICACIÓN")
                    print(calificacion_encontrada.mostrar_datos_calificacion())
                    
                else:
                    print("No se encontro ningúna calificación registrada con ese ID.")
            except TypeError:
                print("Los datos ingresados son del tipo incorrecto.")
                
        elif subopcion == "3":
            try:
                id_estudiante = int(input("Ingrese el ID del estudiante para ver sus calificaciones: "))
                calificaciones_encontradas = gestor_calificacion.listar_calificaciones_por_id_estudiante(id_estudiante)
                
                if calificaciones_encontradas:
                    print("Calificaciones: ")
                    for c in calificaciones_encontradas:
                        print(c)
                
                else:
                    print("El ID del estudiante no posee calificaciones.")
            except TypeError:
                print("Los valores ingresados son del tipo incorrecto.")
        
        elif subopcion == "4":
            try:
                id_calificacion = int(input("Ingrese el ID de la calificación a modificar: "))
                
                nota = int(input("Ingrese un valor (1-10) para modificar la nota o presione enter para omitir: "))
                descripcion = input("Ingrese una nueva descripción o presione enter para no modificar: ")
                
                resultado = gestor_calificacion.modificar_calificacion(id_calificacion, nota, descripcion)
                if resultado:
                    print("Modificación realizada exitosamente.")
                else:
                    print("No se realizó ninguna modificación.")
            except TypeError:
                print("Los valores ingresados son del tipo incorrecto. Intentelo nuevamente.")
        
        elif subopcion == "5":
            try:
                id_calificacion = int(input("Ingrese el ID de la calificación que desea eliminar: "))
                
                resultado = gestor_calificacion.eliminar_calificacion(id_calificacion)
                if resultado:
                    print("Calificación eliminada exitosamente.")
                    
                else: 
                    print("No se pudo eliminar la calificación.")
            except TypeError:
                print("Los valores ingresados son del tipo incorrecto.")
        
        elif subopcion == "6":
            break
        
        else:
            print("Opción inválida. Intentelo nuevamente.")