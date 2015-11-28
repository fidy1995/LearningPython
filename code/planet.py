###################################
# class Planet :
#      One single planet of the system
#      Provide several methods to determine position
###################################
from trivec import *
from time import sleep

# G
GRAVITY_CONST = 6.67428 * (10 ** 0)

class Planet:
    # constructor
    def __init__(self, tvp, tvv, mass):
        self.p = tvp
        self.v = tvv
        self.m = float(mass)
        self.a = Trivec(0, 0, 0, True)

    # destructor
    def __del__(self):
        del self.p, self.v, self.m, self.a
        #del self

    # test func, print out the status of the planet
    def __repr__(self):
        s = "Place: " + self.p.toString()
        s = s + "\nVelocity: " + self.v.toString()
        s = s + "\nAccleration: " + self.a.toString()
        s = s + "\nMass: %.4f" % self.m
        return s

    # test func for Tribody
    def toString(self):
        s = "Place: " + self.p.toString()
        s = s + "\nVelocity: " + self.v.toString()
        s = s + "\nAccleration: " + self.a.toString()
        s = s + "\nMass: %.4f" % self.m
        return s

    # get the distance of 2 planets
    def getDistance(self, pl):
        return pl.p - self.p

    # get the distance of 2 planets in polar
    def getPoDistance(self, pl):
        distance = self.getDistance(pl)
        distance = distance.trans()
        return distance

    # get the gravity in 3 dimensions
    def getGravity(self, pl):
        distance = self.getPoDistance(pl)
        absG = GRAVITY_CONST * self.m * pl.m / (distance.x ** 2)
        gravity = Trivec(absG, distance.y, distance.z, False)
        return gravity.trans()

    # update the accleration of the planet
    def updateAcc(self, acc):
        self.a = self.a + acc

    # update the velocity of the planet, and clear the accleration
    # because v(t)(0, t) = adt(0, t), F does not bound to time and so does a
    # but v is time-related so we must clear a after it is added to v
    def updateVelo(self, tdelta):
        #print "for debug %.2f" % tdelta, self.a, self.v
        self.v = self.v + (tdelta * self.a)
        #print "for debug %.2f" % tdelta, self.a, self.v
        self.a.clear()

    # update the position of the planet
    def updatePos(self, tdelta):
        self.p = self.p + (self.v * tdelta)

    def getAcc(self, pl):
        gravity = self.getGravity(pl)
        acc = gravity * (1 / self.m)
        return acc

    # get the change of velocity
    def getDeltaVelo(self, tdelta):
        velocity = tdelta * self.a
        return velocity

    # get the change of position for furthur use (especially for GUI)
    def getDeltaPos(self, tdelta):
        deltapos = tdelta * self.v
        return deltapos

    # get the 2-dimension position: for GUI
    def getL2Pos(self, basex, basey):
        return self.p.getL2Pos(basex, basey)

    # three view drawing - Main View
    def getMainPos(self, basex, basey):
        return self.p.getMainPos(basex, basey)

    # three view drawing - Top View
    def getTopPos(self, basex, basey):
        return self.p.getTopPos(basex, basey)

    # three view drawing - Side View
    def getLeftPos(self, basex, basey):
        return self.p.getLeftPos(basex, basey)

'''
def main():
    pos1 = Trivec(0, 0, 0)
    velo1 = Trivec(0, 0, 0)
    pl1 = Planet(pos1, velo1, 6l* (10 ** 24))
    pos2 = Trivec(2L * (10 ** 11), 0, 0)
    pl2 = Planet(pos2, velo1, 2l * (10 ** 30))
    tdelta = 0.1
    for i in range(3000):
        sleep(tdelta)
        pl1.updateAcc(pl2)
        pl2.updateAcc(pl1)
        pl1.updatePos(tdelta)
        pl2.updatePos(tdelta)
        print pl1
        print pl2
        pl1.updateVelo(tdelta)
        pl2.updateVelo(tdelta)        

main()
'''
        
        
    
