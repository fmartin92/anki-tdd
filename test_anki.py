import anki
import pytest
from datetime import datetime

@pytest.fixture
def card():
    return anki.Card(front='life', back='42')


@pytest.fixture
def card_2():
    return anki.Card(front='death', back='43')


@pytest.fixture
def deck(card):
    return anki.Deck(cards=set([card]))

@pytest.fixture
def timestamp():
    return datetime(2022, 1, 1)


def test_Card__constructor__success(card):
    assert card.front == 'life'
    assert card.back == '42'


def test_Deck__constructor__success(card, deck):
    assert deck.cards == set([card])


def test_Deck__get_history_for_empty_history__success(deck, card):
    assert deck.get_history(card) == []


def test_Deck__get_history_for_unknown_card__key_error(deck, card_2):
    with pytest.raises(KeyError):
        deck.get_history(card_2)


def test_Deck__mark_recall__reflected_in_history(deck, card):
    deck.mark_recall(card, True)
    history = deck.get_history(card)
    assert(len(history) == 1)
    recall_event = history[0]
    assert isinstance(recall_event.timestamp, datetime)
    assert recall_event.was_recalled


def test_RecallEvent__constructor__success(timestamp):
    recall_event = anki.RecallEvent(timestamp, True)
    assert recall_event.timestamp == timestamp
    assert recall_event.was_recalled