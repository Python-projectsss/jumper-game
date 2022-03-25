
# This class will draw the parachuse and will make the update in the draw 
# Will see if the person is still alive or not and if not will draw it 
# Everytime that the user guess wrong will cut a line from the list 


class Console:
    # ********************** Will initialize the list ***********************
    def __init__(self):
       """
       This method will inizialied the list to draw the parachuse 
       """
       self.parachuse = []
       self.position = 0

    pass


    # ********************************** PARACHUSE POSITION ***********************************

    def parachuse_position(self, tries):
        """
        This will update the  parachuse list if the user guessed wrong and will update it
        cutting one line of the parachuse
        """

        stages = [  
    
"""     ___
    /___\\
    \\   /
     \\ /
      0
     /|\\
     / \\
    """,
    """
    /___\\
    \\   /
     \\ /
      0
     /|\\
     / \\
    """,
    """
    \\   /
     \\ /
      0
     /|\\
     / \\
    """,
    """
     \\ /
      0
     /|\\
     / \\
    """,
    """
      x
     /|\\
     / \\
    """,
    
]

        return stages[tries]


