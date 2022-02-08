from card_pull import Card
cards = Card()
class Director:
    #when the program starts set the game as playing and set a starting score
    def __init__(self):
        self.is_playing = 'true'
        self.total_score = 300
    
    #This is the beginning of the game after the initial setup.
    def start_game(self):
        print("Welcome to Hilo game!")# The welcome message, it will be display at the begining of the game
        print()
        # this is the game loop that will keep the game running until the player looses or quits
        while self.is_playing == 'true':
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    #this is where the users inputs are registered       
    def get_inputs(self):
        if self.is_playing == 'false':
            return
        # the player may choose to draw a card
        draw_card = input("Draw Card? [y/n] ")
        if draw_card == 'n':
            self.is_playing = 'false'
            return
        #this references a method in the Cards class
        #it allows them to guess higher or lower
        cards.get_user_input()    
    
    #this is where the game updates the required variables and runs comparisons
    def do_updates(self):
        if self.is_playing == 'false':
            return 
        #this is a Cards method that draws a new current card
        cards.draw_new_card()
        #this is a Cards method that compares the new and old card to see if the user guessed correctly
        cards.guess()
        #change the points depending on a correct or incorrect guess
        self.total_score += cards.points
        print(f"Next card was: {cards.next_card}")

    #this is where the game produces outputs for the user to see
    def do_outputs(self):
        if self.is_playing == 'false':
            return
        #show the score and the current card for the player
        print(f"Your score is: {self.total_score}\n")
        print(f"The card is: {cards.next_card}")
        if self.total_score <= 0:
            self.is_playing = 'false'