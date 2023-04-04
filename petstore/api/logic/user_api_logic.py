import allure
from pydantic import ValidationError
from petstore.api.validator.user_module_validator import User
from petstore.api.api_methods.user_api_module import UserApiModule


class UserApiLogic:

    @staticmethod
    @allure.step('Validate response status code and get username')
    def __get_user_name_from_the_post_user_method(url: str) -> str:
        user_name: str = UserApiModule.post_user_request(url)
        return user_name

    @allure.step('GET user by username and validate response body')
    def get_user_by_username_and_validate_response(self, url: str) -> None:
        user_name: str = self.__get_user_name_from_the_post_user_method(url)
        response: str = UserApiModule.get_user_request(url, user_name)

        try:
            user_info = User.parse_raw(response)
            assert user_info.username == user_name, f'Response body does not contain information about {user_name}'
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @allure.step('Change username and validate it')
    def user_api_flow(self, url: str) -> None:
        user_name: str = self.__get_user_name_from_the_post_user_method(url)
        UserApiModule.put_user_request(url, user_name)




