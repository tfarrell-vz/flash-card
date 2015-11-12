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
