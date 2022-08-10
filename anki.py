from datetime import datetime

class Card:
    def __init__(self, front: str, back: str):
        self.front = front
        self.back = back


class Deck:
    def __init__(self, cards: set):
        self.cards = cards
        self.history = {card: [] for card in cards}
    
    def get_history(self, card: Card):
        return self.history[card]
    
    def mark_recall(self, card: Card, was_recalled: bool):
        self.history[card].append(
            RecallEvent(
                datetime.now(),
                was_recalled)
        )


class RecallEvent:
    def __init__(self, timestamp: datetime, was_recalled: bool):
        self.timestamp = timestamp
        self.was_recalled = was_recalled