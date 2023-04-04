import allure
import pytest
from petstore.api.logic.pet_api_module_logic import PetApiLogic


@allure.suite('Pet API Module')
class TestPetModule:

    @pytest.mark.api
    @allure.title('Test pet api flow')
    def test_pet_api_flow(self, options):
        PetApiLogic.get_pet_by_id_and_validate_id(url=options['url'])
        PetApiLogic.delete_pet_by_id(url=options['url'])
