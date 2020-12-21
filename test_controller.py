from test_model import TradingCard
from test import write_to_json, card_getter
import json
from flask import request

card = card_getter(987, 1)
print(dir(card))
write_to_json(card[0])