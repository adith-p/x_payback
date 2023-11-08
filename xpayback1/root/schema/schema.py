from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):

    fullname: str
    email: EmailStr
    password: str
    Phone: int


class User_response_schema(BaseModel):
    fullname: str
    email: EmailStr
    phone: int

    class Config:
        orm_mode = True


class full_user_response(BaseModel):
    profile_pic: str | None
    user: User_response_schema

    class Config:
        orm_mode = True
