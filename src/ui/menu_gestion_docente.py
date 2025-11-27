import __future__
from services.gestor_docente import GestorDocente
from dao.docente_dao import DocenteDAO
from config.db_conn import DBConn

def menu_docente(id_docente: int):
    db_conn = DBConn(config_file='config.ini')
    dao = DocenteDAO(db_conn)
    gestor_docente = GestorDocente(dao)
    
    docente = gestor_docente.obtener_docente(id_docente)
    if docente:
        return (
            "MIS DATOS"
            f'ID Docente: {docente.id_docente}'
            f'Nombre: {docente.nombre_docente}'
            f'Apellido: {docente.apellido_docente}'
            f'email: {docente.email}'
        )
    
    else:
        return 'No se pudo acceder a la información.'
    