#Deck Class
class Deck:
    def __init__(self):
        """
        Makes a new deck ready to play
        """
        #Storage for the cards
        self.cards = list()
        for suit in SUITS:
            for value in range(1,21):
                self.cards.append(f"{suit}{value}")
        random.shuffle(self.cards)

    def __len__(self):
        """
        Returns how many cards are left to play
        """
        return len(self.cards)

    def deal(self):
        """
        Deals out one card at a time with no replacement
        But only if there are cards left!
        """
        if len(self.cards)>0:
            return self.cards.pop()

    def _print(self):
        """
        DEBUG function
        """
        print(f"There are {len(self.cards)} cards left")
        pass
#Deck Class
