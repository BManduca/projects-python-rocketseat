from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
import pytest
from .pets_repository import PetsRepository

# Teste unitário => Para simular uma session e evitar que o programa fique em tempo
# integral batendo no DB para efetuar os devidos testes

# Intuito deste unittest é conseguir colocar um ambiente controlado 'na frente'
# do banco de dados, para assim, não ter o acesso direto do código com o banco de dados


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],  # query
                    [
                        PetsTable(name="Ralf", type="dog"),
                        PetsTable(name="Noah", type="cat"),
                    ],  # result
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        # quando fizermos a query, o efeito secundário vai ser levantar um erro.
        self.session.query.side_effect = self.__raise_no_result_found

    # ao utilizarmos os seguintes params: *args e **kwargs,
    # as propriedades que serão 'enviadas' para self.__raise_no_result_found,
    # serão carregadas diretamente no metodo
    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


# test for listing pets
def test_list_pets():
    # criando mock de conexao
    mock_connection = MockConnection()
    # instanciando repositorio com mock de conexao
    repo = PetsRepository(mock_connection)
    # chamando metodo list_pets e verificando se retorna a lista de pets correta
    response = repo.list_pets()

    # query chamada uma única vez com {nome_da_tabela} que é o comportamento do método list_pets
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "Ralf"


# test for delete pet
def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pets("petName")

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.name == "petName")
    mock_connection.session.delete.assert_called_once()


# test for except in return if the pet list
def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []


def test_delete_pet_error():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pets("petName")

    # verificando se o metodo de rollback foi chamado uma unica vez
    mock_connection.session.rollback.assert_called_once()
