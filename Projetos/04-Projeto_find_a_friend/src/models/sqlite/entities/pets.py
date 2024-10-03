from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base


class PetsTable(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)

    """ 
        método especial, para que se ocorra em algum momento
        o print em tela de um elemento da tabela pets, virá da forma definida em repr
    """

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"
