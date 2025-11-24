# app/Mail/controller.py

from fastapi import APIRouter, HTTPException
from app.Mail.model import MailModel
from app.database.core import get_db as get_database
from app.Mail.service import send_email_smtp
from typing import List
from bson import ObjectId

router = APIRouter()

# Create a new mail entry

@router.post("/mails/", response_model=MailModel)
async def create_mail(mail: MailModel):
    db = get_database()
    
    # Convertimos a dict con alias (_id en vez de id)
    mail_dict = mail.model_dump(by_alias=True)

    # ❗ ELIMINAMOS _id si viene como None
    if mail_dict.get("_id") is None:
        mail_dict.pop("_id")

    # Insertamos en Mongo
    result = db.mails.insert_one(mail_dict)

    # Mandar correo
    send_email_smtp(
        recipient=mail.email,
        subject="Mail Received",
        body=f"Hello {mail.name},\n\nWe have received your mail regarding '{mail.description}'. We will get back to you shortly.\n\nBest regards,\nTeam"
    )

    # Asignamos el _id generado a la respuesta
    mail.id = str(result.inserted_id)

    return mail


# Get all mail entries

@router.get("/mails/", response_model=List[MailModel])
async def get_mails():
    db = get_database()
    mails = []
    for mail in db.mails.find():
        mail['id'] = str(mail['_id'])
        mails.append(MailModel.model_validate(mail))
    return mails