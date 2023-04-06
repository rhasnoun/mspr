import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI 
from fastapi_sqlalchemy import DBSessionMiddleware, db

from models import Utilisateur as ModelUtilisateur, Plante as ModelPlante, Garde as ModelGarde, Conseil as ModelConseil, Contact as ModelContact
from schema import Utilisateur as SchemaUtilisateur, Plante as SchemaPlante, Garde as SchemaGarde, Conseil as SchemaConseil, Contact as SchemaContact

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-utilisateur/", response_model=SchemaUtilisateur)
def add_utilisateur(utilisateur: SchemaUtilisateur):
    db_utilisateur = ModelUtilisateur(nom=utilisateur.nom, prenom=utilisateur.prenom, email=utilisateur.email, mot_de_passe=utilisateur.mot_de_passe)
    db.session.add(db_utilisateur)
    db.session.commit()
    return db_utilisateur

@app.post("/add-plante/", response_model=SchemaPlante)
def add_plante(plante: SchemaPlante):
    db_plante = ModelPlante(nom_plante=plante.nom_plante, type=plante.type, image=plante.image)
    db.session.add(db_plante)
    db.session.commit()
    return db_plante

@app.post("/add-garde/", response_model=SchemaGarde)
def add_garde(garde: SchemaGarde):
    db_garde = ModelGarde(id_utilisateur=garde.id_utilisateur, id_plante=garde.id_plante, date_garde=garde.date_garde)
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
    db_contact = ModelContact(id_utilisateur1=contact.id_utilisateur1, id_utilisateur2=contact.id_utilisateur2)
    db.session.add(db_contact)
    db.session.commit()
    return db_contact

@app.get("/get-utilisateur/")
def get_utilisateurs():
    utilisateurs = db.session.query(ModelUtilisateur).all()
    return utilisateurs


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)