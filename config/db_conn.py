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

        if self.config_file:
            config = configparser.ConfigParser()
            config_path = pathlib.Path(self.config_file)

            if not config_path.is_absolute():
                config_path = pathlib.Path.cwd() / self.config_file

            config.read(config_path)

            if 'database' not in config:
                raise FileNotFoundError(
                    f"No se encontró la sección [database] en {config_path}. "
                    f"Contenido leído: {config.sections()}"
                )

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
                database = self.db_config.get('database'),
                port = self.db_config.get('port')
            )
        except mysql.connector.Error as err:
            self.logger.error(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception('Usuario o Contraseña inválidos.')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception('La base de datos no existe.')
            else:
                raise Exception('Ocurrió un error inesperado. Contacte al Administrador.')
    