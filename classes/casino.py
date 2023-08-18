import random

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def show(self):
        print(f"{self.rank} of {self.suit}")


class Deck():
    def __init__(self):
        self.cards = []
        self.new_deck()
        self.shuffle()

    def new_deck(self):
        suits = ['♥', '♣', '♦', '♠']
        ranks = ['A', '2', '3', '4', '5', '6',
                 '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def get_card(self):
        return self.cards.pop()


class Player():
    def __init__(self, name, chips=100):
        self.name = name
        self.chips = chips

    def __repr__(self):
        return self.name
