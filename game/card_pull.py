import random
class Card:
    
    """The responsibility of class Card is to keep track of the guesses input by the user and calculate the points.
   
    Attributes:
        value (int): Represent the random card.
        points (int): The number of points the player won.
    """
    
    def __init__(self):
        """Constructs a new instance of card with a value and points attribute.

        Args:
            self (Card): An instance of card.
        """
        self.current_card = 0
        self.next_card = random.randint(1, 13)
        self.points = 0
        self.user_guess = ""
    
    def draw_new_card(self):
        """Selects a new card and sets the current card.
            
            Args:
                self (Card): An instance of Card.
            """
        self.current_card = self.next_card
        self.next_card = random.randint(1, 13)

    def get_user_input(self):
        """gets the users guess of higher or lower.
            
            Args:
                self (Card): An instance of Card.
            """
        self.user_guess = input("Higher or lower? [h/l] ").lower()
        while self.user_guess != "h" and self.user_guess != "l":
            print("\nPlease Type h for Higher or l for Lower")
            self.user_guess = input("Higher or lower? [h/l] ").lower()
        return self.user_guess
            
    def guess(self):
        """ if user's guesses is correct, than 100 point are won, Otherwise, they lose 75 points
        
            Args:
                self (Card): An instance of Card.
            """
        if self.user_guess.lower() == "l" and self.current_card > self.next_card:
            self.points = 100

        elif self.user_guess.lower() == "h" and self.current_card < self.next_card: 
            self.points = 100

        elif self.current_card == self.next_card:
            pass
        
        else:
            self.points = -75
