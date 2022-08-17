from pydantic import BaseModel


class Pet(BaseModel):

    id: int
    category: dict
    name: str
    photoUrls: list[str]
    tags: list[dict]
    status: str
