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
        self.current_card = 0
        self.next_card = random.randint(1, 13)
        self.points = 0
        self.user_guess = ""
    
    #this method will save the current card to a variable and select the next card
    def draw_new_card(self):
        self.current_card = self.next_card
        self.next_card = random.randint(1, 13)

    #this method manages the users guess of higher or lower and saves it
    def get_user_input(self):
        self.user_guess = input("Higher or lower? [h/l] ").lower()
        while self.user_guess != "h" and self.user_guess != "l":
            print("\nPlease Type h for Higher or l for Lower")
            self.user_guess = input("Higher or lower? [h/l] ").lower()
        return self.user_guess
            
    #this method compares the users guess with the current and next card and changes the point value accordingly
    def guess(self):
        """ if user's guesses is correct, than 100 point are won, Otherwise, they lose 75 points"""
        #the first 2 check if the user was right
        if self.user_guess.lower() == "l" and self.current_card > self.next_card:
            self.points = 100

        elif self.user_guess.lower() == "h" and self.current_card < self.next_card: 
            self.points = 100

        #this will check for a tie
        elif self.current_card == self.next_card:
            pass
        
        #this is if they were wrong
        else:
            self.points = -75
