# connectFour
Python connect 4 where one can play against another person or a brute force AI. 

I designed this as a project during a programming course. To play, run ps9pr3.py with the connect_four function in the syntax

connect_four(Player('X'), AIPlayer('O', 'RANDOM', 4))

where Player('X') is the user

and AIPlayer('O', 'RANDOM', 4) is the AI. With RANDOM being the direction it picks if there are 2 solutions with the same
chance of winning, and 4 being the number of moves it looks ahead. To play against another human switch out AI player with
Player('O'). Since the algorithm used to determine next moves is of time complexity O(n^2), look-ahead of over 5 is not
recommended. 
