from fastapi import APIRouter, Body
from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from schema import UserLoginSchema

from models import User as ModelUser
from schema import User  as SchemaUser

router = APIRouter(
    prefix="/user",
    tags = ["users"],
)


@router.post("/signup")
def sign_user(user: SchemaUser):
    db_user = ModelUser(nom=user.nom, prenom=user.prenom, email=user.email, mot_de_passe=user.mot_de_passe)
    db.session.add(db_user)
    db.session.commit()
    return signJWT(user.email)

@router.post("/login")
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

@router.get("/all")
def get_users():
    users = db.session.query(ModelUser).all()
    return users

@router.get("/{id}")
def get_user(idUser: int):
    users = db.session.query(ModelUser).filter(ModelUser.id == idUser).first()
    return users

def check_user(data: UserLoginSchema):
    users = db.session.query(ModelUser).all()
    for user in users:
        if user.email == data.email and user.mot_de_passe == data.password:
            return True
    return False
