from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
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
