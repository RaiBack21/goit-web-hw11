from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas import ContactResponse, ContactModel
from src.database.db import get_db
from src.repository import contacts as rep_contacts

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.get("/", response_model=List[ContactResponse])
async def get_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = await rep_contacts.get_contacts(skip, limit, db)
    return contacts


@router.get("/search", response_model=List[ContactResponse])
async def search_contacts(
    first_name: str = None,
    last_name: str = None,
    email: str = None,
    db: Session = Depends(get_db),
):
    contacts = await rep_contacts.serch_contacts(first_name, last_name, email, db)
    return contacts


@router.get("/upcoming birthdays", response_model=List[ContactResponse])
async def get_upcoming_birthdays(db: Session = Depends(get_db)):
    contacts = await rep_contacts.get_upcoming_birthdys(db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def get_contacts(contact_id: int, db: Session = Depends(get_db)):
    contact = await rep_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db)):
    return await rep_contacts.create_contact(body, db)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    body: ContactModel, contact_id: int, db: Session = Depends(get_db)
):
    contact = await rep_contacts.update_contact(body, contact_id, db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await rep_contacts.remove_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
