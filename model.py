from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Column, Numeric, Text
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    user_f_name = db.Column(db.String)
    user_l_name = db.Column(db.String)
    user_name = db.Column(db.String, unique=True)
    user_password = db.Column(db.String)
    user_email = db.Column(db.String)


class Card(db.Model):
    __tablename__ = 'cards'

    card_id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    card_name = db.Column(db.String)
    card_cost = db.Column(db.String)
    card_series = db.Column(db.Integer, ForeignKey("series.serise_id"))
    card_rules = db.Column(db.Text)
    card_fl_text = db.Column(db.Text)
    card_img = db.Column(db.String)  # this will be a link to an image

    series = relationship("Series", primaryjoin="Series.series_id==Card.card_series")


class CardsOwned(db.Model):
    """A joining table between users and cards"""
    __tablename__ = 'cards_owned'

    co_id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    user_id = db.Column(db.Integer, ForeignKey("users.user_id"))
    card_id = db.Column(db.Integer, ForeignKey("cards.card_id"))

    cards = relationship("Card", primaryjoin="Card.card_id==CardsOwned.card_id")
    users = relationship("User", primaryjoin="User.user_id==CardsOwned.user_id")


class Deck(db.Model):
    __tablename__ = 'decks'

    deck_id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    deck_owner = db.Column(db.Integer, ForeignKey("users.user_id"))
    deck_name = db.Column(db.String)

    users = relationship("User", primaryjoin="User.user_id==Deck.deck_owner")


class DeckCard(db.Model):
    """A joining table between cards and decks"""
    __tablename__ = 'deck_cards'

    dc_id = db.Column(db.Integer, primary_key=True, autoincriment=True)
    deck_id = db.Column(db.Integer, ForeignKey("decks.deck_id"))
    card_id = db.Column(db.Integer, ForeignKey("cards.card_id"))

    decks = relationship("Deck", primaryjoin="DeckCard.deck_id==Deck.deck_id")
    cards = relationship("Card", primaryjoin="Card.card_id==DeckCard.card_id")


def connect_to_db(flask_app=app, echo=True, db_uri='postgresql:///cards'):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = flask_app
    db.init_app(flask_app)
    print('Connected to the db!')


if __name__ == "__main__":
    from app import app

    connect_to_db()
