from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from models import models
from database.database import engine

from routers import users


app = FastAPI()


models.Base.metadata.create_all(engine)
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(users.router)


# @app.post('/register', response_model=User_response_schema)
# async def register_user(request: UserSchema, db: Session = Depends(get_db)):
#     """
#     Register Users
#     """
#     if validate_data.validate_email(db=db, email=request.email):
#         hash_password = hash_pwd.Hasher().get_password_hash(request.password)

#         user_instance = models.Users(
#             fullname=request.fullname, email=request.email, phone=request.Phone, password=hash_password)

#     db.add(user_instance)
#     db.commit()
#     db.refresh(user_instance)

#     return user_instance


# @app.post('/user/{user_id}')
# async def add_users_profile(user_id, image: UploadFile = File(...)):

#     if image:
#         image_url = save_image.save_image(image)

#         collection = m_db.profile
#         document = {'user_id': user_id, 'image_url': image_url}
#         collection.insert_one(document)

#         return {'s': status.HTTP_200_OK}


# @app.get('/user/{user_id}', response_model=full_user_response)
# async def get_users(user_id: int, db: Session = Depends(get_db)):

#     collection = m_db.profile
#     doc = collection.find_one({'user_id': str(user_id)})

#     user = db.query(models.Users).get(user_id)
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail='requested data does not exist')

#     response = {
#         "profile_pic": doc.get('image_url') if doc else None,
#         "user": User_response_schema(fullname=user.fullname, email=user.email, phone=user.phone)
#     }

#     return response
