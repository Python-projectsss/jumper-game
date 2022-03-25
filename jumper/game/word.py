
# This class will inizialite the list and will get a random word from the a list that we will include

import random

class Word:

     # ********************** Will initialize the list for the word ***********************
    def __init__(self):
        """
        This method will inizialied the list 
        """
        self.list_words = []
        self.empty_array = []

    pass


    # ********************************** LIST OF WORDS ***********************************

    def list_of_words(self):

        """"
        This will have the list of a lot of word that the game randomnly will select and save in the
        word attribute it will not return any value just will contain the list
        """

        self.list_words = ["apple", "banana","cherry","mango", "orange","dog","goat", "pop","mouse","zebra","lion","beer","water", "love"  "hat","lamp", "book","umbrella", "cake", "bottle"]


    # ********************************** GET WORD ***********************************

    def get_word(self):
        """
        Get Word is the only methond that will return a value and is going to be the word that 
        randomly was chose and assign to the attribute word
        """
        self.list_of_words()
        self.word = random.choice(self.list_words)

        return self.word









