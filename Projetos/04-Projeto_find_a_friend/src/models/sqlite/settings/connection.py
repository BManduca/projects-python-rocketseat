from sqlalchemy import create_engine

class DBConnectionhandler:
    def __init__(self) -> None:
        #  string connection
        self.__connection_string = 'sqlite:///storage.db'
        self.__engine = None

    def connect_to_db(self):
        # criando uma string de conexão apartir da connection_string
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

db_connection_handler = DBConnectionhandler()
