import os
import uuid
from fastapi import status, HTTPException
from models import models
from schema.schema import User_response_schema
from utils import validate_data, hash_pwd, save_image


def register(request, db):
    if validate_data.validate_email(request.email, db) and validate_data.validate_phone(request.phone, db):

        HASH_PWD = hash_pwd.Hasher().get_password_hash(request.password)
        user_instance = models.Users(
            fullname=request.fullname, email=request.email, phone=str(request.phone), password=HASH_PWD)

        db.add(user_instance)
        db.commit()
        db.refresh(user_instance)

    return user_instance


def upload_photo(image, user_id, db):

    image_url = save_image.save_image(image)

    profile_instance = models.Profile(
        profile_pic=image_url, user_id=user_id)

    db.add(profile_instance)
    db.commit()
    db.refresh(profile_instance)

    db.rollback()
    return {'s': status.HTTP_200_OK}


def return_user(db, user_id):
    if profile := db.query(models.Profile).filter(models.Profile.user_id == user_id).first():
        return profile
    elif user := db.query(models.Users).get(user_id):
        return {
            "profile_pic": None,
            "user": User_response_schema(fullname=user.fullname, email=user.email, phone=user.phone)
        }
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='requested data does not exist')
