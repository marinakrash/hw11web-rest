from typing import List, Optional
from pydantic import BaseModel, Field


class ContactsModel(BaseModel):
    name: str = Field(max_length=25)


class ContactsResponse(ContactsModel):
    id: int

    class Config:
        orm_mode = True
