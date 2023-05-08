from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class user(Base):
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
    image = Column(String(100))

class Garde(Base):
    __tablename__  = 'garde'
    id_garde = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_garde = Column(Date)
    user = relationship(user)
    plante = relationship(Plante)

class Conseil(Base):
    __tablename__  = 'conseil'
    id_conseil = Column(Integer, primary_key=True)
    id_botaniste = Column(Integer, ForeignKey('user.id_user'))
    id_plante = Column(Integer, ForeignKey('plante.id_plante'))
    date_conseil = Column(Date)
    texte_conseil = Column(Text)
    botaniste = relationship(user)
    plante = relationship(Plante)

class Contact(Base):
    __tablename__  = 'contact'
    id_contact = Column(Integer, primary_key=True)
    id_user1 = Column(Integer, ForeignKey('user.id_user'))
    id_user2 = Column(Integer, ForeignKey('user.id_user'))
    user1 = relationship(user, foreign_keys=[id_user1])
    user2 = relationship(user, foreign_keys=[id_user2])