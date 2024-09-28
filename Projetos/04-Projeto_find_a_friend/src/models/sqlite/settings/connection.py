from sqlalchemy import create_engine

# função que auxilia na criação de sessões
from sqlalchemy.orm import sessionmaker


class DBConnectionhandler:
    def __init__(self) -> None:
        #  string connection
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        # criando uma string de conexão apartir da connection_string
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = DBConnectionhandler()
