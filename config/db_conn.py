import __future__
import mysql.connector
import logging
import configparser
import pathlib
from mysql.connector import errorcode

class DBConn:
    def __init__(self, config_file):
        self.config_file = config_file
        self.logger = logging.getLogger("DBConn")
        
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)
        
        if (self.config_file != ""):
            config = configparser.ConfigParser()
            config_path = pathlib.Path(__file__).parent.absolute()
            config.read(config_path)
            self.db_config = config['database']
        else:
            self.db_config = None
    
    def obtener_nombre_db(self):
        return self.db_config.get('database')
            
    def conectar_a_mysql(self):
        try:
            return mysql.connector.connect(
                user = self.db_config.get('user'),
                password = self.db_config.get('password'),
                host = self.db_config.get('host'),
                port = self.db_config.get('port')
            )
        except mysql.connector.Error as err:
            self.logger.error(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise 'Usuario o Contraseña inválidos.'
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise 'La base de datos no existe.'
            else:
                raise 'Ocurrió un error inesperado. Contacte al Administrador.'
    