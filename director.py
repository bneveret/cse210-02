from card_pull import Card
cards = Card()
class Director:

    def __init__(self):
        self.is_playing = 'true'
        self.total_score = 300
        
    def start_game(self):
        print("Welcome to Hilo game!")# The welcome message, it will be display at the begining of the game
        print()
        while self.is_playing == 'true':
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
                   
    def get_inputs(self):
        if self.is_playing == 'false':
            return
        draw_card = input("Draw Card? [y/n] ")
        if draw_card == 'n':
            self.is_playing = 'false'
            return
        cards.get_user_input()    
    
    def do_updates(self):
        if self.is_playing == 'false':
            return 
        
        cards.draw_new_card()
        cards.guess()
        self.total_score += cards.points
        print(f"Next card was: {cards.next_card}")

    def do_outputs(self):
        if self.is_playing == 'false':
            return
        
        print(f"Your score is: {self.total_score}\n")
        print(f"The card is: {cards.next_card}")
        if self.total_score <= 0:
            self.is_playing = 'false'