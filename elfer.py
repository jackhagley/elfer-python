
import random

import constants as c
import deck
import player



class Elfer:
#     
    def __init__(self):
        self.the_active_player = False;
        self.players = [player.Player(name) for name in c.player_names]
        self.deck = deck.Deck()
        self.board = dict()
        self.moves = set()
        self.starting_cards = [ a+str(11) for a in c.suits ]
        self.game_is_active = True
        
    def still_has_cards(self):
        return len(self.deck)

    def next_turn(self):
        if self.game_is_active:
            self.the_active_player.reset_pickup_counter()
            self.players = self.players[1:] + self.players[:1]
            self.the_active_player = self.players[0]
            if (c.DEBUG):             
                print (f"It is {self.players[0].name}’s turn")
    
    def end_game(self, player):
        print(f"{player.name} wins")
        self.game_is_active = False
    
    def get_available_moves(self):
        #generates a set of strings of possible card plays
        self.moves = set()
        for stack in self.board.items():
            #get colour
            colour = stack[0]
            #get values
            low, high = int(stack[1][0]), int(stack[1][1])
            #make up some 11s if there’s nothing there
            if low==99 and high ==-99:
                self.moves.add(f"{colour}{11}")            
            if 11>=low>1:
                self.moves.add(f"{colour}{low-1}")
            if 11<=high<20:
                self.moves.add(f"{colour}{high+1}")
        if (c.DEBUG):        
            print(f"availiable board moves: {self.moves}")
        pass
    
    def player_plays_card(self, name, card):
        if card in self.moves:
            #do not make an illegal play
            colour = card[0]       
            value = int(card[1:3])
            #is it an 11 play
            if value==11:
                self.board[colour] = [11,11]
            #is it a low play or a high play?
            current_low =  int( self.board[colour][0] ) 
            current_high = int( self.board[colour][1] )       
            if  1 <= value < 11: 
                self.board[colour] = [value,current_high]
            if 20 >= value > 11: 
                self.board[colour] = [current_low, value]       

            if (c.DEBUG):
                print(f"{name} plays {card}")
            self.get_available_moves()#updates the board
        else:
            if (c.DEBUG):
                print(f"{name} plays {card} is not possible (player does not have card)")
        pass
    
    def reset_game(self):
        #SETUP
        #shuffle the player order
        random.shuffle(self.players)
        self.the_active_player = False;
        #clear the board
        self.board = dict.fromkeys(c.suits,[99,-99]) # Colour, Low Value, High Value
        self.get_available_moves()
        #give the cards back
        for player in self.players:
            player.empty_hand()
        #remake the deck
        self.deck = deck.Deck()
        #reset the move
        self.get_available_moves() 
        #deal out   
        for i in range(c.n_starting_hand):
            for player in self.players:
                player.take_card( self.deck.deal() )

        #GAME ON
        self.game_is_active = True
        #Whomstever has the red 11 starts
        #If no-one has the red 11 then Y, G, B are chosen in order    
        for card in self.starting_cards:
            for player in self.players:
                if card in player.hand and not self.the_active_player:#only if there is no active_player
                    if (c.DEBUG):
                        print (f"{player.name} has {card}")
                    self.the_active_player = player
                    if (c.DEBUG):
                        print(f"{self.the_active_player.name} will start the game")
                    #player plays an 11
                    self.the_active_player.plays_card(self, card)#put the game into the player so we can play it back
                    

                    break                    
        #If no one can go then we just take the first person
        #because we shuffle people it’s like they are swapping seats each game
        if not self.the_active_player:
            if (c.DEBUG):
                print ("no one has an 11, picking at random")
            self.the_active_player = self.players[0]
            if (c.DEBUG):
                print(f"{self.the_active_player} will start the game")       
        pass

                
    def play(self, n_plays):
        for n in range(n_plays):
            print("")
            print(f"game {n+1}")
            self.reset_game()      
            while self.game_is_active and self.the_active_player:
                self.the_active_player.take_a_turn(self, self.moves)
            