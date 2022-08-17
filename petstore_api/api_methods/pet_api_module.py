import allure
import requests


class PetApiModule:

    @staticmethod
    @allure.step('POST pet request')
    def post_pet_request(proto: str, url: str) -> str:
        r = requests.post(
            url='{}://{}/v2/pet'.format(proto, url),
            headers={'Content-Type': 'application/json'},
            json={
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            }
        )

        if r.status_code == 200:
            return r.text

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')

    @staticmethod
    @allure.step('GET pet request')
    def get_pet_request(proto: str, url: str, pet_id: int) -> str:
        r = requests.get(
            url='{}://{}/v2/pet/{}'.format(proto, url, pet_id),
        )

        if r.status_code == 200:
            return r.text

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')

    @staticmethod
    @allure.step('DELETE pet request')
    def delete_pet_request(proto: str, url: str, pet_id: int) -> int:
        r = requests.delete(
            url='{}://{}/v2/pet/{}'.format(proto, url, pet_id),
        )

        if r.status_code == 200:
            return r.status_code

        raise AssertionError(f'Expected status code is 200, actual is {r.status_code}')

