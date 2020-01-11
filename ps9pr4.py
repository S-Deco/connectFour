#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):

    def __init__(self,checker,tiebreak,lookahead):
        """ constructs a new AIPlayer object using the attributes of player and
            new attributes tiebreak and lookahead.
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string represetnign an AIPlayer object by overriding
            the __repr__ method inherited from the player. Incldes tiebreak and
            lookahead
        """
        checker = super().__repr__()
        return checker + ' (' +  self.tiebreak + ', ' + str(self.lookahead) + ')'

    def max_score_column(self,scores):
        """ takes input scores: a list of scores, and returns the index of
            the column with the max score
        """
        listindeces= []
        currentmax = scores[0]
        for i in range(len(scores)):
            if currentmax == scores[i]:
                listindeces += [i]
            elif currentmax < scores[i]:
                currentmax = scores[i]
                listindeces = [i]
        if self.tiebreak == 'RANDOM':
            return random.choice(listindeces)
        elif self.tiebreak == 'RIGHT':
            return listindeces[-1]
        else:
            return listindeces[0]

    def scores_for(self,b):
        """ takes input b: board object, and determines the called AIPlayer's
            scores for the columns in  b
        """

        listscores = [50] *  b.width
        for c in range(b.width):
            if b.can_add_to(c) == False:
                  listscores[c] = -1
            elif b.is_win_for(self.checker):
                 listscores[c] = 100
            elif b.is_win_for(self.opponent_checker()):
                listscores[c] = 0
            elif self.lookahead == 0:
                if listscores[c] == 50:
                    listscores[c] = 50
            else:
                opponent = AIPlayer(self.opponent_checker(),self.tiebreak, self.lookahead - 1)
                b.add_checker(self.checker,c)
                opp_scores = opponent.scores_for(b)
                if 100 in opp_scores:
                    listscores[c] = 0
                elif 50 in opp_scores:
                    listscores[c] = 50
                elif 0 in opp_scores:
                    listscores[c] = 100

                b.remove_checker(c)
        return listscores

    def next_move(self,b):
        """ overrides next_move of player with AIPlayers best move """
        bestcol = self.max_score_column(self.scores_for(b))
        self.num_moves += 1
        return bestcol
                
