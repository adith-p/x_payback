from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from database.database import get_db
from schema.schema import User_response_schema, UserSchema, full_user_response
from repository import user


router = APIRouter(prefix='/user', tags=['users'])


@router.post('/register', response_model=User_response_schema)
async def register_user(request: UserSchema, db: Session = Depends(get_db)):
    """
    Register Users
    """
    return user.register(request, db)


@router.post('/{user_id}')
async def add_users_profile(user_id, image: UploadFile = File(...), db: Session = Depends(get_db)):

    return user.upload_photo(image, user_id, db)


@router.get('/{user_id}', response_model=full_user_response)
async def get_users(user_id: int, db: Session = Depends(get_db)):

    return user.return_user(db, user_id)
