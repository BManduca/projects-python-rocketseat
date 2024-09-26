import pytest
from sqlalchemy.engine import Engine
from .connection import db_connection_handler

# intuito de conhecimento(educativo)
@pytest.mark.skip(reason="interação com o banco de dados.")
# test integration with DB
def test_connect_to_db():
    # verificando engine é None
    assert db_connection_handler.get_engine() is None

    # estabelencendo conexao com o DB
    db_connection_handler.connect_to_db()
    #  atualizando e armazenando o valor da engine
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
