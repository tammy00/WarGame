class Card:
    def __init__(self, suit, value):
        list_value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        suit_number = ['Diamond', 'Spade', 'Heart', 'Club']
        if value in list_value:
            self.value = list_value.index(value) + 2
        else:
            raise IndexError("value not in range")
        if suit in suit_number:
            self.suit = suit_number.index(suit) + 1
        else:
            raise IndexError("suit must one of the following:", suit_number)

    def __gt__(self, other):
        if other.suit < self.suit or (other.suit == self.suit and other.value < self.value):
            return True
        else:
            return False

    def __str__(self):
        return self.suit, self.value
