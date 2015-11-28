##########################
# Class Datapack:
#     To check out if the data is correct.
##########################

from trivec import *

# define error numbers
SAFE = -1 # if the data is safe
ERR_NUM = 0 # if input is not a number
ERR_INV = 1 # if the number is invalid 
ERR_COL = 2 # if the planets are going to collapse

class Datapack:
    # constructor
    def __init__(self, data):
        self.d = data

    # check if the data is a number
    def checkNum(self, index):
        try:
            self.d[index] = float(self.d[index])
            return True
        except ValueError:
            return False

    # the check function
    def check(self):
        L = len(self.d)
        for i in range(L):
            if not self.checkNum(i):
                return ERR_NUM
        for i in range(0, L, 7):
            if self.d[i] < 0:
                return ERR_INV
        newd = [0] * 9
        ite = 0
        # this is to generate the data into proper form
        for i in range(9):
            if ite % 7 == 0:
                newd[i] = self.d[ite]
                ite = ite + 1
            else:
                newd[i] = Trivec(self.d[ite], self.d[ite + 1], self.d[ite + 2])
                ite = ite + 3
        if newd[1] == newd[4] or newd[1] == newd[7] or newd[4] == newd[7]:
            return ERR_COL
        self.d = newd
        return SAFE
            
