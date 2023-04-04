import allure
import requests


class PetApiModule:

    @staticmethod
    @allure.step('POST pet request')
    def post_pet_request(url: str) -> str:
        r = requests.post(
            url=f'{url}/v2/pet',
            headers={'Content-Type': 'application/json'},
            json={
                'id': 0,
                'category': {
                    'id': 0,
                    'name': 'string'
                },
                'name': 'doggie',
                'photoUrls': [
                    'string'
                ],
                'tags': [
                    {
                        'id': 0,
                        'name': 'string'
                    }
                ],
                'status': 'available'
            }
        )

        assert r.status_code == 200, f'Expected status code is 200, actual is {r.status_code}'
        return r.text

    @staticmethod
    @allure.step('GET pet request')
    def get_pet_request(url: str, pet_id: int) -> str:
        r = requests.get(
            url=f'{url}/v2/pet/{pet_id}',
        )

        assert r.status_code == 200, f'Expected status code is 200, actual is {r.status_code}'
        return r.text

    @staticmethod
    @allure.step('DELETE pet request')
    def delete_pet_request(url: str, pet_id: int) -> int:
        r = requests.delete(
            url=f'{url}/v2/pet/{pet_id}',
        )

        assert r.status_code == 200, f'Expected status code is 200, actual is {r.status_code}'
        return r.status_code
