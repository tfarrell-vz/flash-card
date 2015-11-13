import random


class FlashCard:
    """
    A flash card is an abstraction of the physical flash cards we are familiar
    with. It contains text on the front that quizzes our memory, with the answer
    contained on the back.
    """
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back


class Deck:
    """
    A deck is a container of flash cards.
    """
    def __init__(self, cards=None):
        """
        A deck can be initialized with a list of cards.
        """
        if cards:
            self.cards = cards
        else:
            self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def shuffle(self):
        random.shuffle(self.cards)


class Quiz:
    def __init__(self, deck, position=0):
        self.deck = deck
        self.position = 0
        self.correct = []
        self.incorrect = []
        self.current_card = None

    def start(self):
        self.current_card = self.deck[0]

    def advance(self):
        self.position += 1
        self.current_card = self.deck[self.position]

    def retreat(self):
        self.position -= 1
        self.current_card = self.deck[self.position]

    def mark(self, correct=False):
        if correct:
            self.correct.append(self.current_card)
        else:
            self.incorrect.append(self.current_card)