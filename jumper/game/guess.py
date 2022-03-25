
# This function will take the word from the class word and will compare with the user guess
# if it Guess it will return it as it failed 
#  if it Guess it will call the methon  word from word and will update the word and add the word in the place it has to be 

from game.word import Word

class Guess:    


    # ********************************** INIZIALITED ***********************************
    def __init__(self):
        """
        This method will inizialied the two list the one for the gues and the one with the word
        """
        self.word = Word()
        self.random_word = []
        self.guessed_letters = []
        self.tries = 0
        self.random_word = self.word.get_word()
        self.word_completion = "_" * len(self.random_word)
        self.play = True

    # ********************************** COMPUTE GUESS ***********************************

    def can_play(self):

        if self.tries == 5:
            self.play = False
        
        return self.play


    # ********************************** COMPUTE GUESS ***********************************


    def compute_guess(self,guess):
        """
        This Method will return the progress that the user have made so far
        """

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in self.random_word:
                print(guess, "is not in the word.")
                self.tries += 1
                self.guessed_letters.append(guess)

            else:
                print("Good job, ", guess, " is in the word!.")
                self.guessed_letters.append(guess)
                word_as_list = list(self.word_completion)
                indices = [i for i, letter in enumerate(self.random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                self.word_completion = "".join(word_as_list)
                if "_" not in self.word_completion:
                    print("Congreatulations You guessed the word! " + self.random_word)
                    print("The Jumper is still alive Good Job! \n")
                    self.play =  False

        elif len(guess) == len(self.random_word) and guess.isalpha():
            if guess in self.guessed_letters:
                print("You already guessed the word", guess)
            elif guess != self.random_word:
                print(guess, " Is not not the word.")
                self.tries +=1
                self.guessed_letters.append(guess)
            else:
                self.play = False
                self.word_completion = guess
                print("Congreatulations You guessed the word! " + self.random_word)
                print("The Jumper is still alive Good Job! \n")
            
        else:
            print("Not a valid guess")

    pass


   # ********************************** USER PROGRESS ***********************************

    def user_progress(self):
        """
        This will return the progress of the user how far is he with the word
        """
        return self.word_completion

    # ********************************** MYSTERIOUS WORD ***********************************

    def mysterious_word(self):
        """
        This funcgtion will return the random word
        """
        return self.random_word

    # ********************************** NUMBER OF TRIES ***********************************

    def number_of_tries(self):
        """
        This function will return the random word
        """
        return self.tries
    




