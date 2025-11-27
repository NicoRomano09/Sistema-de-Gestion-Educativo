from __future__ import annotations
from services.gestor_docente import GestorDocente
from config.db_conn import DBConn
from dao.docente_dao import DocenteDAO
from domain.docente import Docente
from ui.menu_principal import menu_principal
from ui.func_validar_formato import validar_email


def main():
    db_conn = DBConn(config_file='config.ini')
    dao = DocenteDAO(db_conn)
    gestor_docente = GestorDocente(dao)
    while True:
        print("\nSistema de Gestión Educativo")
        print("1) Registrarse")
        print("2) Iniciar sesión")
        print("0) Salir")
        op = input("> ").strip()

        if op == "1":
            try:
                nombre_docente = input("Ingrese su nombre: ")
                apellido_docente = input("Ingrese su apellido: ")
                email = input("Ingrese su email: ")
                contrasena = input("Ingrese una contraseña: ")
                
                validar_email(email)
                existente = gestor_docente.obtener_docente_por_email(email)
                if existente:
                    raise ValueError("Ya existe un docente con el mail ingresado.")
                
                if contrasena < 8:
                    raise ValueError("Contraseña invalida: Debe contener al menos 8 carácteres.")
                
                docente = Docente(
                    id_docente=None,
                    nombre_docente=nombre_docente,
                    apellido_docente=apellido_docente,
                    email=email,
                    contrasena_hash=contrasena
                )
                
                resultado = gestor_docente.registrar_docente(docente)
                
                if resultado:
                    print("Docente registrado exitosamente.")
                else:
                    print("Operación sin éxito.")

            except Exception as e:
                print(f"Error al registrar el docente: {e}")

        elif op == "2":
            email = input("Email: ").strip()
            contrasena = input("Contraseña: ").strip()
            session = gestor_docente.login(email, contrasena)
            if session:
                menu_principal(session)
            else:
                print("Credenciales inválidas.")

        elif op == "0":
            print("Gracias por utilizar nuestro sistema SmartHome. Hasta pronto.")
            break

        else:
            print("❌ Opción no válida.")

if __name__ == "__main__":
    main()