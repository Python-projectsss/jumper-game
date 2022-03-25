from game.guess import Guess
from game.word import Word
from game.console import Console

class Director:

     # ******************************************** Will inizialite the game ********************************************
    def __init__(self):

        """"Class Constructor: will inizialite a list and get the word to be guess"""

        self.keep_playing = True
        self.guess = Guess()
        self.console = Console()
        self.word = Word()
        #  This will draw the parachuse just one time
        self.tries = 0
        self.user_letter = ""

    # ******************************************** Start Game ********************************************
    def start_game(self):
        """Starts the game loop to control the sequence of play.

        """
        print("\n")
        while self.keep_playing:
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
           

    # ******************************************** Get imputs ********************************************
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
            it will prompt to the user for the word to guess and will save it in a varible  
        """

        self.user_letter = ""
        self.user_letter = input ("Guess a letter from [a-z] : ")


        
    # ******************************************** do outputs ********************************************
    def do_outputs(self):
        """Outputs the important game information for each round of play. It will draw the paracuse 
        and the list of letter including if he had guess any or not.
        """

        print("   " + self.guess.user_progress())
        # print("   " + self.guess.mysterious_word())
        print(self.console.parachuse_position(self.tries))
        


    # ******************************************** Do updates ********************************************

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, it will compare the information if the user guess right or not 
        """
        

        self.guess.compute_guess(self.user_letter)
        self.keep_playing = self.guess.can_play()
        self.tries = self.guess.number_of_tries()
        
        if self.tries ==  4:
            print("Sorry Buddy you just killed the jumper")
            print(self.console.parachuse_position(4))
            print("The word was ", self.guess.mysterious_word(), " Good luck next time \n")
            self.keep_playing = False

  







       
    




