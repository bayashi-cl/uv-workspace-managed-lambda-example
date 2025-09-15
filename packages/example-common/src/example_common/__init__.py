from pydantic import BaseModel


class ExampleDto(BaseModel):
    message: str
