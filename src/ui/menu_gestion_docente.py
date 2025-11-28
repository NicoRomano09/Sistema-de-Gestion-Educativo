import __future__
from src.services.gestor_docente import GestorDocente
from src.dao.docente_dao import DocenteDAO
from config.db_conn import DBConn

def menu_docente(id_docente: int):
    db_conn = DBConn(config_file='config.ini')
    dao = DocenteDAO(db_conn)
    gestor_docente = GestorDocente(dao)
    
    docente = gestor_docente.obtener_docente(id_docente)
    if docente:
        print(docente.mostrar_datos_docente())
    else:
        print("No se recuperaron datos.")
    