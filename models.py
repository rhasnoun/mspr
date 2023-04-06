from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Utilisateur(Base):
    __tablename__  = 'utilisateur'
    id_utilisateur = Column(Integer, primary_key=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    email = Column(String(100))
    mot_de_passe = Column(String(50))

class Plante(Base):
    __tablename__  = 'plante'
    id_plante = Column(Integer, primary_key=True)
    nom_plante = Column(String(50))
    type = Column(String(50))
    image = Column(String(100))

class Garde(Base):
    __tablename__  = 'garde'
    id_garde = Column(Integer, primary_key=True)
    id_utilisateur = Column(Integer, ForeignKey('utilisateur.id_utilisateur'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_garde = Column(Date)
    utilisateur = relationship(Utilisateur)
    plante = relationship(Plante)

class Conseil(Base):
    __tablename__  = 'conseil'
    id_conseil = Column(Integer, primary_key=True)
    id_botaniste = Column(Integer, ForeignKey('utilisateur.id_utilisateur'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_conseil = Column(Date)
    texte_conseil = Column(Text)
    botaniste = relationship(Utilisateur)
    plante = relationship(Plante)

class Contact(Base):
    __tablename__  = 'contact'
    id_contact = Column(Integer, primary_key=True)
    id_utilisateur1 = Column(Integer, ForeignKey('utilisateur.id_utilisateur'))
    id_utilisateur2 = Column(Integer, ForeignKey('utilisateur.id_utilisateur'))
    utilisateur1 = relationship(Utilisateur, foreign_keys=[id_utilisateur1])
    utilisateur2 = relationship(Utilisateur, foreign_keys=[id_utilisateur2])