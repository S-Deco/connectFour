# Problems set 9 problem 1
# Connect 4


class Board:

    def __init__(self, height, width):
        """ constructs a new board object with height: number of rows
            and width: number of colums in each row
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        # Add code here for the hyphens at the bottom of the board
        # and the numbers underneath it.
        for c in range(self.width * 2 + 1):
            s += '-'
        s += '\n'
        for c in range(self.width):
            s += ' ' + str(c) 
        return s

    def add_checker(self, checker, col):
        """ adds a checker of type checker to column col of the board
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        for c in range(self.height):
            if self.slots[c][col] != ' ':  
                self.slots[c - 1][col] = checker
                break
            elif c == self.height - 1:
                self.slots[c][col] = checker
                break
            
    def reset(self):
        """ resets the board object on which its called
        """
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self,col):
        """ returns True if its valid to put a checker in column col in the
            board object and False otherwise
        """
        if col not in range(self.width):
            return False
        if self.slots[0][col] == ' ':
            return True
        else:
            return False

    def is_full(self):
        """ returns True if the board object is completely full of checkers
            otherwise returns False
        """
        checker = True
        for c in range(self.width):
            if self.can_add_to(c):
                checker = False
        return checker

    def remove_checker(self,col):
        """ removes the top checker from column col of the board object
        """
        checker = 0
        for c in range(self.height):
            if self.slots[c][col] != ' ' and checker == 0:
                self.slots[c][col] = ' '
                checker = 1
                
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self,checker):
        """ Checks for a vertical win for the specified checker
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                 if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row  + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
        return False
    
    def is_diagonal_win(self,checker):
        """ Checks for a diagonal win for the specified checker
        """
        for row in range(self.height - 3, self.height):
            for col in range(self.width - 3):
                 if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                 if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        
        return False

    def is_win_for(self, checker):
        """ accepts a parameter checker that is either 'X' or 'O' and returns
            True if there are 4 consecutive slots containing checker on the
            board
        """
        if self.is_vertical_win(checker) or self.is_horizontal_win(checker) or self.is_diagonal_win(checker):
            return True
        else:
            return False
    

def test():
    b = Board(6, 7)
    print(b)
