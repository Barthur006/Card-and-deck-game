from card import Card
from random import shuffle
import random

class Deck(object):
    """Deck class models a standard deck of playing cards containing 52 cards."""

    def __init__(self):
        """
        Initializes a deck with an unshuffled deck of 52 cards.
        
        Instance variables:
            self._cards: a list initialized with 52 Card objects in a standard deck of cards.
        """
        self._cards = []
        for rank in range(1,14):
            for suit in range(1,5):
                self._cards.append(Card(rank,suit))
        

    def size(self):
        """Returns the size (number of cards) of the deck."""
        return len(self._cards)

    def is_empty(self):
        """Returns True if the deck is empty, False otherwise."""
        return (len(self._cards) == 0)
       

    def contains(self, card):
        "Returns True if the specified card is in the deck, False otherwise."
        if card in self._cards:
            return True
        else:
            return False

    def shuffle(self):
        """Shuffle the cards in the deck into a random order."""

        """"
        import random
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        """
        shuffle(self._cards)
              

    def deal(self):
        """If the deck is not empty, pop the card at the end of deck and return it."""

        for x in range (53):  
            if  self.is_empty(): break
            return self._cards.pop()

    """   
        if len(self.cards) == 0:
            return
        return self.cards.pop()

        if len(self._cards) != 0:
            return self._cards.pop()
    """

    def __str__(self):
        """Returns a printable string representation of cards in the deck."""
        return str(self._cards)

    def __repr__(self):
        """Returs a string representation of cards in the deck."""
        return self.__str__()


