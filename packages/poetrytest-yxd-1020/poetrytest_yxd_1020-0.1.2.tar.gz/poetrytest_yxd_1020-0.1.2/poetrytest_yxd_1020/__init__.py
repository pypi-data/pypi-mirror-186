
from pydantic import BaseModel, Field

class Person(BaseModel):
    name: str = Field(alias='Name')
    age: int = Field(alias='Age')
    

