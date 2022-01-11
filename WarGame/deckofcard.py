from random import *


class DeckOfCard:

    def __init__(self):
        self.cards = []
        for s in ['Spade', 'Club', 'Diamond', 'Heart']:
            for v in range(2, 11):
                self.cards.append((s, v))
            for v in 'Jack', 'Queen', 'King', 'Ace':
                self.cards.append((s, v))

    def __str__(self):
        return self.cards

    def cards_shuffle(self):
        for i in range(3):
            shuffle(self.cards)

    def deal_one(self):
        e = choice(self.cards)
        self.cards.remove(e)
        return e

# obj = DeckOfCard()
# print(obj.cards)
# print('_____________________')
# obj.cards_shuffle()
# print(obj.cards)
# print(len(obj.cards))
# print(obj.deal_one())
# print(len(obj.cards))
