from typing import Dict, List
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_lister_controller import PetListerControllerInterface

class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_reponse(pets)

        return response

    # listagem total pets -> não possui attr
    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets
    
    def __format_reponse(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({ 
                'name': pet.name, 
                'type': pet.type, 
                'id': pet.id 
            })

        return {
            'data': {
                'type': 'Pets',
                'count': len(formatted_pets),
                'attributes': formatted_pets
            }
        }