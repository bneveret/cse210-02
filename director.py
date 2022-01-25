from card_pull import Card
import random

class Director:

    def __init__(self):
        self.current_card = [random.randint(1, 13)]
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        cards = Card()
        self.current_card.append(cards)
        
    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self, cards):
        draw_card = input("Draw Card? [y/n] ")
        self.is_playing = (draw_card == "y")
        cards.get_user_input()

    def do_updates(self, cards):
        if not self.is_playing:
            return 
        
        # updates go here
        

    def do_outputs(self):
        if not self.is_playing:
            return
        value=""
        cards = self.current_card[0]
        value += f"{cards.value} "

        print(f"You rolled a {value}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)