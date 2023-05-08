import os
import uvicorn
from dotenv import load_dotenv
from fastapi import Body, Depends, FastAPI 
from fastapi_sqlalchemy import DBSessionMiddleware, db
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from models import user as Modeluser, Plante as ModelPlante, Garde as ModelGarde, Conseil as ModelConseil, Contact as ModelContact
from schema import UserLoginSchema, User as SchemaUser, Plante as SchemaPlante, Garde as SchemaGarde, Conseil as SchemaConseil, Contact as SchemaContact

load_dotenv(".env")



app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/user/signup", tags=['user'])
def sign_user(user: SchemaUser):
    db_user = Modeluser(nom=user.nom, prenom=user.prenom, email=user.email, mot_de_passe=user.mot_de_passe)
    db.session.add(db_user)
    db.session.commit()
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    users = db.session.query(Modeluser).all()
    for user in users:
        if user.email == data.email and user.mot_de_passe == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(...)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

@app.get("/get-user/", tags=["user"])
def get_users():
    users = db.session.query(Modeluser).all()
    return users


@app.post("/plante/add",dependencies=[Depends(JWTBearer())],tags=["plante"] ,response_model=bool)
def add_plante(plante: SchemaPlante):
    try:
        db_plante = ModelPlante(nom_plante=plante.nom_plante, type=plante.type, image=plante.image)
        db.session.add(db_plante)
        db.session.commit()
        return True
    except:
        return False

@app.post("/plante/{id}",dependencies=[Depends(JWTBearer())],tags=["plante"] ,response_model=bool)
def get_plante(plante: SchemaPlante):
    try: 
        db_plante = ModelPlante(nom_plante=plante.nom_plante, type=plante.type, image=plante.image)
        db.session.add(db_plante)
        db.session.commit()
        return True 
    except:
        return False

@app.post("/add-garde/", response_model=SchemaGarde)
def add_garde(garde: SchemaGarde):
    db_garde = ModelGarde(id_user=garde.id_user, id_plante=garde.id_plante, date_garde=garde.date_garde)
    db.session.add(db_garde)
    db.session.commit()
    return db_garde

@app.post("/add-conseil/", response_model=SchemaConseil)
def add_conseil(conseil: SchemaConseil):
    db_conseil = ModelConseil(id_botaniste=conseil.id_botaniste, id_plante=conseil.id_plante, date_conseil=conseil.date_conseil, texte_conseil=conseil.texte_conseil)
    db.session.add(db_conseil)
    db.session.commit()
    return db_conseil

@app.post("/add-contact/", response_model=SchemaContact)
def add_contact(contact: SchemaContact):
    db_contact = ModelContact(id_user1=contact.id_user1, id_user2=contact.id_user2)
    db.session.add(db_contact)
    db.session.commit()
    return db_contact




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)