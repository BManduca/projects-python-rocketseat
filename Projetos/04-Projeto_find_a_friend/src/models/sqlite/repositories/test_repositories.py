import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interação com banco de dados.")
def test_list_pets():
    # instancia do pets_repository com injeção de dependencia do db_connection_handler
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)


@pytest.mark.skip(reason="interação com banco de dados.")
def test_delete_pet():
    name_pet = "belinha"
    repo = PetsRepository(db_connection_handler)
    # delete um pet
    repo.delete_pets(name_pet)


@pytest.mark.skip(reason="interação com banco de dados.")
def test_insert_person():
    first_name = "test first name"
    last_name = "test last name"
    age = 25
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason="interação com banco de dados.")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
