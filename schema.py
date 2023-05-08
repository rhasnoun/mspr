from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    id_user: int
    nom: str
    prenom: str
    email: str
    mot_de_passe: str
    class Config:
        orm_mode= True

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "email": "joe@xyz.com",
                "password": "any"
            }
        }

class Plante(BaseModel):
    id_plante: int
    nom_plante: str
    type: str
    image: str
    class Config:
        orm_mode= True
class Garde(BaseModel):
    id_garde: int
    id_user: int
    id_plante: int
    date_garde: str
    user: str
    plante: str
    class Config:
        orm_mode= True

class Conseil(BaseModel):
    id_conseil: int
    id_botaniste: int
    id_plante: int
    date_conseil: str
    texte_conseil: str
    botaniste: str
    plante: str
    class Config:
        orm_mode= True

class Contact(BaseModel):
    id_contact: int
    id_user1: int
    id_user2: int
    user1: str
    user2: str
    class Config:
        orm_mode= True