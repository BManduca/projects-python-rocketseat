# from sqlalchemy.ext.declarative import declarative_base (old) -> versões mais antigas do sqlalchemy
from sqlalchemy.orm import declarative_base

# criando uma base declarativa para repassar para o sqlalchemy,
# quem são os elementos de armazenamento

Base = declarative_base()
