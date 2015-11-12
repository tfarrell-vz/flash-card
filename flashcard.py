class FlashCard:
    """
    A flash card is an abstraction of the physical flash cards we are familiar
    with. It contains text on the front that quizzes our memory, with the answer
    contained on the back.
    """
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back
