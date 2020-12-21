from test_model import TradingCard
import json
from mtgsdk import Card

def card_getter(page_number, page_size):
  cards = Card.where(language='english').where(page=page_number).where(pageSize=page_size).all()
  return cards

def write_to_json(data): 
  with open ('json.txt', 'w') as j:
    json.dump(data, j)
