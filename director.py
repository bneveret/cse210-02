from card_pull import Card
import random

class Director:

    def __init__(self):
        self.current_card = random.randint(1, 13)
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        
        cards = Card()
        #self.current_card.append(cards)
        
    def start_game(self):
        print("Welcome to Hilo game!")# The welcome message, it will be display at the begining of the game
        print()
        while self.is_playing:
            self.do_outputs()
            self.get_inputs(Card())
            self.do_updates()
            self.__init__()
            
                   
    def get_inputs(self, cards):
        #draw_card = input("Draw Card? [y/n] ")
        #self.is_playing = (draw_card == "y")
        #cards = Card()
        cards.get_user_input()    

    def do_outputs(self):
        if not self.is_playing:
            return
        #value=""
        cards = Card()
        cards = self.current_card
        #value += (f"{cards.value} ")

        print(f"The card is: {cards}")
        #print(f"Your score is: {self.total_score}\n")
        #self.is_playing == (self.score > 0)
    
    def do_updates(self):
        if not self.is_playing:
            return 
        
        # updates go here
        cards = Card()
        cards = self.current_card
        #card_dict2 = { card2.get_value()}
        #self.next_card.update(card_dict2)
        #card_dict2.clear()

        #for key2, value2 in self.next_card.items():
        #    self.card_value2 = value2
        print(f"Next card was: {cards}")