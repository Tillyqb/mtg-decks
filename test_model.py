from pydantic import BaseModel
import dataclasses
from pydantic.dataclasses import dataclass
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import (
    Deque, Dict, FrozenSet, List, Optional, Sequence, Set, Tuple, Union
)
import os

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  db.init_app(app)
  return app

app = create_app()

db = SQLAlchemy()

os.system('dropdb cards')
os.system('createdb cards')
db.create_all(app=create_app())

class TradingCard(BaseModel):
  name: str
  colors: List[str]
  colorIdentity: List[str]
  manaCost: str
  cmc: int
  rarity: str
  types: List[str]
  supertypes: List[str] = None
  subtypes: List[str] = None
  set: List[str]
  setName: str
  text: str
  flavor: str
  power: str
  toughness: str
  layout: str
  imageUrl: str
  printings: List[str]
  legalities: dict

def connect_to_db(flask_app=app, echo=True, db_uri='postgresql:///cards'):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = False
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = flask_app
    db.init_app(flask_app)
    print('Connected to the db!')

if __name__ == "__main__":
    connect_to_db()