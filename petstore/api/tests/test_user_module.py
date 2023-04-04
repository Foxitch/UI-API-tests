import allure
import pytest
from petstore.api.logic.user_api_logic import UserApiLogic


@allure.suite('User API Module')
class TestUserModule:

    @pytest.mark.api
    @allure.title('Test user api flow')
    def test_user_api_flow(self, options):
        UserApiLogic.get_user_by_username_and_validate_response(url=options['url'])
        UserApiLogic.user_api_flow(url=options['url'])
