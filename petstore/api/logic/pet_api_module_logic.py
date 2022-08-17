import allure
from pydantic import ValidationError
from petstore.api.validator.pet_module_validator import Pet
from petstore.api.api_methods.pet_api_module import PetApiModule


class PetApiLogic:

    @staticmethod
    @allure.step('Validate response body and get ID')
    def __get_id_from_the_post_pet_method(proto: str, url: str) -> int:
        response = PetApiModule.post_pet_request(proto, url)

        try:
            post_pet = Pet.parse_raw(response)
            return post_pet.id
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @staticmethod
    @allure.step('GET pet by id and validate response body')
    def get_pet_by_id_and_validate_id(proto: str, url: str) -> None:
        pet_id: int = PetApiLogic.__get_id_from_the_post_pet_method(proto, url)
        response: str = PetApiModule.get_pet_request(proto, url, pet_id)

        try:
            post_pet = Pet.parse_raw(response)
            assert post_pet.id == pet_id
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @staticmethod
    @allure.step('Delete created pet by id')
    def delete_pet_by_id(proto: str, url: str) -> None:
        pet_id: int = PetApiLogic.__get_id_from_the_post_pet_method(proto, url)
        PetApiModule.delete_pet_request(proto, url, pet_id)
