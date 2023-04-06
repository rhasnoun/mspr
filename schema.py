from pydantic import BaseModel 

class Utilisateur(BaseModel):
    id_utilisateur: int
    nom: str
    prenom: str
    email: str
    mot_de_passe: str
    class Config:
        orm_mode= True

class Plante(BaseModel):
    id_plante: int
    nom_plante: str
    type: str
    image: str
    class Config:
        orm_mode= True
class Garde(BaseModel):
    id_garde: int
    id_utilisateur: int
    id_plante: int
    date_garde: str
    utilisateur: str
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
    id_utilisateur1: int
    id_utilisateur2: int
    utilisateur1: str
    utilisateur2: str
    class Config:
        orm_mode= True