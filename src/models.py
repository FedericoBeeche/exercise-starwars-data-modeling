import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), unique=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    population = Column(Integer)
    capital = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    lastname = Column(String(250))
    age = Column(Integer)
    ship = Column(Integer , ForeignKey('ship.id'))

class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer , ForeignKey('character.id'), primary_key = True)
    name = Column(String(250))
    ship = relationship(Character)

class PlanetFavorite(Base):
    __tablename__ = 'favoritePlanet'
    user_id = Column(Integer , ForeignKey('user.id'), primary_key = True)
    planet_id = Column(Integer , ForeignKey('planet.id'), primary_key = True)
    user = relationship(User)
    planet = relationship(Planet)

class CharacterFavorite(Base):
    __tablename__ = 'favoriteCharacter'
    user_id = Column(Integer , ForeignKey('user.id'), primary_key = True)
    character_id = Column(Integer , ForeignKey('character.id'), primary_key = True)
    user = relationship(User)
    character = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')