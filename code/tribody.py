#####################################
# class Tribody :
#      The three body system at back end
#      Provide several methods especially for GUI
#      Calculate the status of every planets in the system
#####################################
from planet import *

class Tribody:
    # constructor
    def __init__(self, pl, tdelta = 0.1):
        self.pl = pl
        self.t = tdelta

    # copy constructor
    def copy(self):
        tb = Tribody(self.pl, self.t)
        return tb

    # destructor
    def __del__(self):
        del self.pl, self.t

    # test func
    def __repr__(self):
        s = ""
        for i in range(3):
            s = s + self.pl[i].toString() + "\n"
        return s

    # calculate every status for one step:
    # the acceleration must be calculated in the same time
    def calAcc(self, i):
        acc = Trivec(0, 0, 0)
        if i != 0:
            acc = acc + self.pl[i].getAcc(self.pl[0])
        if i != 1:
            acc = acc + self.pl[i].getAcc(self.pl[1])
        if i != 2:
            acc = acc + self.pl[i].getAcc(self.pl[2])
        return acc

    # cal other status with acclerations
    def calStatus(self, acc):
        for i in range(3):
            self.pl[i].updateAcc(acc[i])
            self.pl[i].updateVelo(self.t)
            self.pl[i].updatePos(self.t)

    # calculate all status of planets
    def cal(self):
        acc0 = self.calAcc(0)
        acc1 = self.calAcc(1)
        acc2 = self.calAcc(2)
        acc = [acc0, acc1, acc2]
        self.calStatus(acc)

    # get the 4 positions of a planet as a list
    def getPlanetPos(self, index, basex, basey):
        pos = [0] * 8
        pos[0], pos[1] = self.pl[index].getMainPos(basex, basey)
        pos[2], pos[3] = self.pl[index].getLeftPos(basex, basey)
        pos[4], pos[5] = self.pl[index].getTopPos(basex, basey)
        pos[6], pos[7] = self.pl[index].getL2Pos(basex, basey)
        return pos

'''
def main():
    pos1 = Trivec(0, 0, 0)
    pos2 = Trivec(2000, 0, 0)
    pos3 = Trivec(-2000, 0, 0)
    velo1 = Trivec(0, 0, 0)
    velo2 = Trivec(0, 5000, 0)
    velo3 = Trivec(0, -5000, 0)
    pl1 = Planet(pos1, velo1, 1l * 10 ** 20)
    pl2 = Planet(pos2, velo2, 5)
    pl3 = Planet(pos3, velo3, 5)
    pl = [pl1, pl2, pl3]
    tb = Tribody(pl)
    for i in range(3):
        tb.cal()

main()
'''
