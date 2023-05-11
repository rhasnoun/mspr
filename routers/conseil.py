from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from auth.auth_bearer import JWTBearer
from models import Conseil as ModelConseil
from schema import Conseil as SchemaConseil
router = APIRouter(
    prefix="/conseil",
    tags = ["conseil"],
    dependencies=[Depends(JWTBearer())],
)

@router.post("/add")
def add_conseil(conseil: SchemaConseil):
    db_conseil = ModelConseil(id_botaniste=conseil.id_botaniste, id_plante=conseil.id_plante, date_conseil=conseil.date_conseil, texte_conseil=conseil.texte_conseil)
    db.session.add(db_conseil)
    db.session.commit()
    return db_conseil
