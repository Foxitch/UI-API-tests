import allure
import requests
from petstore.api.generator.generator import generated_user_data


class UserApiModule:

    @staticmethod
    @allure.step('Generate users information')
    def __generate_user_info() -> dict:
        user_info = next(generated_user_data())

        user_data: dict = {
            'user_name': f'{user_info.user_name}',
            'first_name': f'{user_info.first_name}',
            'last_name': f'{user_info.last_name}',
            'email': f'{user_info.email}',
            'password': f'{user_info.password}',
            'phone': f'{user_info.phone}',
        }
        return user_data

    @staticmethod
    @allure.step('POST user request')
    def post_user_request(proto: str, url: str) -> str:
        user_info: dict = UserApiModule.__generate_user_info()

        r = requests.post(
            url='{}://{}/v2/user'.format(proto, url),
            headers={'Content-Type': 'application/json'},
            json={
                "id": 0,
                "username": f"{user_info['user_name']}",
                "firstName": f"{user_info['first_name']}",
                "lastName": f"{user_info['last_name']}",
                "email": f"{user_info['email']}",
                "password": f"{user_info['password']}",
                "phone": f"{user_info['phone']}",
                "userStatus": 0
            }
        )

        if r.status_code == 200:
            return user_info['user_name']

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')

    @staticmethod
    @allure.step('GET user request')
    def get_user_request(proto: str, url: str, user_name: str) -> str:
        r = requests.get(
            url='{}://{}/v2/user/{}'.format(proto, url, user_name),
        )

        if r.status_code == 200:
            return r.text

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')

    @staticmethod
    @allure.step('PUT user request')
    def put_user_request(proto: str, url: str, user_name: str) -> str:
        user_info: dict = UserApiModule.__generate_user_info()
        new_user_name: str = next(generated_user_data()).user_name

        r = requests.put(
            url='{}://{}/v2/user/{}'.format(proto, url, user_name),
            headers={'Content-Type': 'application/json'},
            json={
                "id": 0,
                "username": f"{new_user_name}",
                "firstName": f"{user_info['first_name']}",
                "lastName": f"{user_info['last_name']}",
                "email": f"{user_info['email']}",
                "password": f"{user_info['password']}",
                "phone": f"{user_info['phone']}",
                "userStatus": 0
            }
        )

        if r.status_code == 200:
            return new_user_name

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')
