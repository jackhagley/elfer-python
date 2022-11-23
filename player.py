#Player Class
class Player:
    def __init__(self, name_):
        """
        Init the Player by calling the Player’s name
        """
        self.name = name_
        self.hand = set()        # empty the hand
        self.pickup_counter = 3
        self.matrix = []

    def empty_hand(self):
        """
        Empties the Player’s hand of cards
        """
        self.hand = set()

    def show_hand(self):
        """
        DEBUG function that prints the Player’s cards
        'Lay your hand on the table'
        """
        print(f"{self.name}’s hand: {self.hand}")

    def take_card(self,card):
        """
        The Player takes a card from the Deck
        This is used to deal, but the Players take turns to take cards to make their hands
        """
        if (DEBUG):
            print(f"{self.name} gets {card}")
        self.hand.add(card)

    def _print(self):
        """
        DEBUG function in case you need to know the Player name
        """
        print( str(self.name) )
        pass

    def has_card(self,test_card):
        """
        Does the Player have this card?
        Returns a boolean value from a card input
        """
        return test_card in self.hand

    def plays_card(self, game, card):
        """
        Mechanism for a Player removing a card from their hand
        """
        if self.has_card(card): # Players can only play cards they are holding
            game.player_plays_card(self.name,card)
            self.hand.remove(card)
            self.pickup_counter = 0 # Players cannot pick up on turns they play

            #if they play their last card they win
            if (DEBUG):
                print(f"{self.name} has {len(self.hand)} cards left")
            if len(self.hand)==0:
                if (DEBUG):
                    print("game_over")
                game.end_game(self)
        else:
            if (DEBUG):
                # if you ever see this, something has gone badly wrong
                print(f"{self.name} is trying to play {card} (not in hand) ")

    def reset_pickup_counter(self):
        """
        The number of cards they can pick up from the deck if they cannot go
        They must pick them up one by one
        """
        self.pickup_counter = 3

    def take_a_turn(self, game, board_state):
        """
        Used when it becomes the Player’s turn

        possible_moves = a set of the option space
        """

        #Find posible moves with a simple set intersection
        possible_moves = board_state.intersection(self.hand)

        if len(possible_moves)==1:
            #if they have just one option then play that
            self.plays_card(game, str(list(possible_moves)[0]) )
            #nothing else we can do
            game.next_turn()
            return

        if len(possible_moves)>1:

            if (DEBUG):
                print(f"{self.name} has these moves: {possible_moves}")

            """
            At this point the Player must make a decision about which card
            to play. This is the only part of the game that the Player can influence
            The Player can play as many cards as they want,
            but if they can go, they must play at least one

            There are three things to consider:
            - The cards that the player has
            - The cards that have already been played (game picture)
            - The Players that are unable to play (what do people not have)

            This knowledge of the game can be mapped onto a 4x20x(n) matrix
            Each cell can be marked as
            - Unknown (not in play)
            - In this Players Hand
            - Not in another Players hand (they skipped a turn when a card was playable)
                this is important as it may be needed to block another Player

            The Player needs to make it easy for other Players to play the cards that they need
            The Player can force other Players to do this by restricting their moves in the right way




            """

            #choose a card at random
            self.plays_card(game, str(list(possible_moves)[0]) )
            self.take_a_turn(game, game.moves )
        pass

        #if player cannot play then they take a card from the deck
        if len(possible_moves)==0 :

                #no moves left and cannot pickup
            if self.pickup_counter==0 and game.game_is_active:
                game.next_turn()
                return

             # pick up 3 or less cards
            if self.pickup_counter>0 and game.still_has_cards():
                self.take_card( game.deck.deal() )
                self.pickup_counter-=1
                #if they can play it then they play it and their turns ends
                self.take_a_turn (game, board_state)#so just run this function again

            #no cards left to pick up in the deck
            if not game.still_has_cards():
                if (DEBUG):
                    print("no cards left")
                game.next_turn()#can only pass
            pass
#Player Class
