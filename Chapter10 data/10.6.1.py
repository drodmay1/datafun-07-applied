# Creating, Shuffling and Dealing the Cards 
from deck import DeckOfCards

deck_of_cards = DeckOfCards()

print(deck_of_cards)

deck_of_cards.shuffle()

print(deck_of_cards)

# Dealing Cards
deck_of_cards.deal_card()

# Class Card’s Other Features
card = deck_of_cards.deal_card()

str(card)

card.image_name

