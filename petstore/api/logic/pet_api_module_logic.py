import allure
from pydantic import ValidationError
from petstore.api.validator.pet_module_validator import Pet
from petstore.api.api_methods.pet_api_module import PetApiModule


class PetApiLogic:

    @allure.step('Validate response body and get ID')
    def __get_id_from_the_post_pet_method(self, url: str) -> int:
        response = PetApiModule.post_pet_request(url)

        try:
            post_pet = Pet.parse_raw(response)
            return post_pet.id
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @allure.step('GET pet by id and validate response body')
    def get_pet_by_id_and_validate_id(self, url: str) -> None:
        pet_id: int = self.__get_id_from_the_post_pet_method(url)
        response: str = PetApiModule.get_pet_request(url, pet_id)

        try:
            post_pet = Pet.parse_raw(response)
            assert post_pet.id == pet_id
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @allure.step('Delete created pet by id')
    def delete_pet_by_id(self, url: str) -> None:
        pet_id: int = self.__get_id_from_the_post_pet_method(url)
        PetApiModule.delete_pet_request(url, pet_id)
