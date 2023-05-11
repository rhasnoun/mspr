from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from auth.auth_bearer import JWTBearer
from models import Garde as ModelGarde
from schema import Garde as SchemaGarde

router = APIRouter(
    prefix="/garde",
    tags = ["garde"],
    dependencies=[Depends(JWTBearer())],
)


@router.post("/add")
def add_garde(garde: SchemaGarde):
    try:
        db_garde = ModelGarde(id_user=garde.id_user, id_plante=garde.id_plante, date_debut=garde.date_debut,date_fin = garde.date_fin)
        db.session.add(db_garde)
        db.session.commit()
    except:
        raise HTTPException( status_code=403, detail = {'error adding'})