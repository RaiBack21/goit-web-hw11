from datetime import date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

class ContactModel(BaseModel):
    first_name: str = Field(min_length=3, max_length=150)
    last_name: str = Field(min_length=3, max_length=150)
    email: EmailStr
    phone_number: str = Field(pattern=r"^\+380\d{9}$")
    birthday: date
    additional_info: Optional[str]

class ContactResponse(ContactModel):
    id: int

    