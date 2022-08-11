from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    address_1: any = None
    postcode: int = None
    city: str = None
    email: str = None
    phone: str = None
    password: any = None

