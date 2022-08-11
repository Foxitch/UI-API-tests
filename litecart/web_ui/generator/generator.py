import random
from faker import Faker
from litecart.web_ui.data.data import User


faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_user_data():
    yield User(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        address_1=faker_en.address(),
        postcode=random.randint(111111, 999999),
        city=faker_en.city(),
        email=faker_en.email(),
        phone=faker_en.msisdn(),
        password=str(random.randint(0000, 9999)) + faker_en.word()
    )
