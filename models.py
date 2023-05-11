from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__  = 'user'
    id_user = Column(Integer, primary_key=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    email = Column(String(100))
    mot_de_passe = Column(String(50))

class Plante(Base):
    __tablename__  = 'plante'
    id_plante = Column(Integer, primary_key=True)
    nom_plante = Column(String(50))
    type = Column(String(50))
    id_owner = Column(Integer, ForeignKey('user.id_user'))
    owner = relationship('user')
    image_url = Column(String(100))

class Garde(Base):
    __tablename__  = 'garde'
    id_garde = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_debut = Column(Date)
    date_fin = Column(Date)
    user = relationship(User)
    plante = relationship(Plante)

class Conseil(Base):
    __tablename__  = 'conseil'
    id_conseil = Column(Integer, primary_key=True)
    id_botaniste = Column(Integer, ForeignKey('user.id_user'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_conseil = Column(Date)
    texte_conseil = Column(Text)
    botaniste = relationship(User)
    plante = relationship(Plante)
