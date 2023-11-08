from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import models


def validate_email(email, db: Session):
    if db.query(models.Users).filter(models.Users.email == email).first():
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail='Email already exist')
    return True


def validate_phone(phone, db: Session):
    if db.query(models.Users).filter(models.Users.phone == str(phone)).first():
        raise HTTPException(status.HTTP_403_FORBIDDEN,
                            detail='phone number already exist')

    return True
