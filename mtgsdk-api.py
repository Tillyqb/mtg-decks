from mtgsdk import Card

def get_cards(num_cards):
  cards = Card.where(supertypes='legendary') \
            .where(types='creature') \
            .where(colors='red,white') \
            .limit(num_cards)
  return cards

def get_cards_in_pages():
  cards = Card.where(page=50).where(pageSize=50).all()

  return cards

with open ("card_return.txt", 'w'):
  card = get_cards(1)
  print(card) > 'card_return.txt'