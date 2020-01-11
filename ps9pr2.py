#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player:

    def __init__(self, checker):
        """ constructs a new player object with attribute checker
        """
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a player object
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one character string representing the checker of the
            Players opponent
        """
        if self.checker  == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self,b):
        """ accepts board object b as a parameter and returns the column where
            the player wants to make the next move
        """
        column = int(input('Enter a column: '))
        while b.can_add_to(column) == False:
            print('Try again!')
            column = int(input('Enter a column: '))
        self.num_moves += 1
        return column

