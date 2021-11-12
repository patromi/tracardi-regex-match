from pydantic import BaseModel


class Configuration(BaseModel):
    pattern: str
    text: str
    groups_name: list
