from game.card_pull import Card
cards = Card()
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (Card): Manages current and new cards.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.is_playing = 'true'
        self.total_score = 300
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        print("Welcome to Hilo game!")# The welcome message, it will be display at the begining of the game
        print()
        while self.is_playing == 'true':
            self.do_outputs()
            self.get_inputs()
            self.do_updates()

    def get_inputs(self):
        """Ask the user if they want to draw.
           If they don't want to draw it ends the game.
           Asks the user to guess higher or lower.

        Args:
            self (Director): An instance of Director.
        """

        if self.is_playing == 'false':
            return
        draw_card = input("Draw Card? [y/n] ")
        if draw_card == 'n':
            self.is_playing = 'false'
            return
        cards.get_user_input()    
    
    def do_updates(self):
        """Updates the current and next card.
           Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """

        if self.is_playing == 'false':
            return 
        cards.draw_new_card()
        cards.guess()
        self.total_score += cards.points
        
    def do_outputs(self):
        """Displays the new card and the score. Also ends the game if they lose. 

        Args:
            self (Director): An instance of Director.
        """

        print(f"Next card was: {cards.next_card}")
        if self.is_playing == 'false':
            return
        print(f"Your score is: {self.total_score}\n")
        print(f"The card is: {cards.next_card}")
        if self.total_score <= 0:
            self.is_playing = 'false'