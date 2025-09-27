from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    role: str

    class Config:
        orm_mode = True
