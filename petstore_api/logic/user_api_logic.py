import allure
from pydantic import ValidationError
from petstore_api.validator.user_module_validator import User
from petstore_api.api_methods.user_api_module import UserApiModule


class UserApiLogic:

    @staticmethod
    @allure.step('Validate response status code and get username')
    def __get_user_name_from_the_post_user_method(proto: str, url: str) -> str:
        user_name: str = UserApiModule.post_user_request(proto, url)
        return user_name

    @staticmethod
    @allure.step('GET user by username and validate response body')
    def get_user_by_username_and_validate_response(proto: str, url: str) -> None:
        user_name: str = UserApiLogic.__get_user_name_from_the_post_user_method(proto, url)
        response: str = UserApiModule.get_user_request(proto, url, user_name)

        try:
            user_info = User.parse_raw(response)
            assert user_info.username == user_name, f'Response body does not contain information about {user_name}'
        except ValidationError as e:
            raise AssertionError('Exception:\n', e.json())

    @staticmethod
    @allure.step('Change username and validate it')
    def user_api_flow(proto: str, url: str) -> None:
        user_name: str = UserApiLogic.__get_user_name_from_the_post_user_method(proto, url)
        UserApiModule.put_user_request(proto, url, user_name)




