import random
from faker import Faker
from petstore.api.data.data import User


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_user_data():
    yield User(
        user_name=faker_en.user_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        phone=faker_en.msisdn(),
        password=str(random.randint(0000, 9999)) + faker_en.word()
    )
