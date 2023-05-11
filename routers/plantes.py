from fastapi import APIRouter
from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from auth.auth_bearer import JWTBearer
from models import Plante as ModelPlante
from schema import Plante as SchemaPlante
router = APIRouter()


router = APIRouter(
    prefix="/plante",
    tags = ["plante"],
    dependencies=[Depends(JWTBearer())],
)

@router.post("/add",response_model=bool)
def add_plante(plante: SchemaPlante, id_owner: int):
    try:
        db_plante = ModelPlante(nom_plante=plante.nom_plante, type=plante.type, image=plante.image_url, id_owner=id_owner)
        db.session.add(db_plante)
        db.session.commit()
        return True
    except:
        return False

@router.get("/all")
def get_all_plant():
    try:
        db_all_plants =  db.session.query(ModelPlante).all()
        return db_all_plants
    except:
        return {
        "error": "Wrong details!"
    }