import random
class Card:
 # 1) Add the class declaration. 
    """The responsibility of class Card is to keep track of the guesses input by the user and calculate the points.
   
    Attributes:
        value (int): Represent the random card.
        points (int): The number of points the player won.
    """
    

        # 2) Create the class constructor.
    def __init__(self):
        """Constructs a new instance of card with a value and points attribute.

        Args:
            self (Card): An instance of card.
        """
        self.value = 0
        self.points = 300

    #dont need this either as its in director.py    
    #def card(self):
        #""" card Generates a new random card from 1 to 13. and calculates the points. The number represent a card."""
        
        #self.current_card = random.randint(1, 13)
        
        #return self.current_card
    
    #Dont think we need this its in director.py
    #def get_user_input(self):
        #self.user_guess = input("higher or lower,[h/l]? ")
        #return self.user_guess
            
    def guess_low(self):
        """ if user's guesses is correct, than 100 point are won, Otherwise, they lose 75 points"""
        if self.user_guess.lower() == "lower" or self.user_guess.lower() == "l":
            self.current_card < self.next_card
            score = self.points + 100
            return score
        else: 
            score = self.points -75
            return score

    def guess_high(self):
        """if user's guesses is higher, meant if user's guesses is correct, 100 points are won. Otherwise they lose 75 points."""
        if self.user_guess.lower() == "higher" or self.user_guess.lower() == "h":
            self.current_card > self.next_card
            score = self.points + 100
            return score
        else: 
            score = self.points -75
            return score

