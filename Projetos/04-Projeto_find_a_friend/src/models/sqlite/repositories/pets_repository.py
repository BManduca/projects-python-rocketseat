from typing import List  # python 3.8
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection):
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                # retornando uma listagem de Pets
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session.query(PetsTable)
                    .filter(PetsTable.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                # caso ocorra qualquer exceção(de maneira geral),
                # será aplicado um rollback, ou seja, voltará ao estado anterior
                database.session.rollback()
                # será levantada a exceção
                raise exception
