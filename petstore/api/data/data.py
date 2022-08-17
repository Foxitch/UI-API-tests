from dataclasses import dataclass


@dataclass
class User:

    user_name: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    password: any = None
    phone: str = None

