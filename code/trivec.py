############################
# class Trivec :
#      A simple three dimensioned vector
############################
from math import asin, sin, acos, cos, sqrt, pi

class Trivec:
    # constructor
    def __init__(self, x, y, z, ra = True):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.ra = ra

    # destructor
    def __del__(self):
        del self.x, self.y, self.z, self.ra
        #del self

    # reload operators
    # vector + vector : simple add in every dimension
    # note: polar can't add directly
    def __add__(self, tv):
        ra = self.ra
        if not self.ra:
            self = self.trans()
        if not tv.ra:
            tv = tv.trans()
        rtn = Trivec(0, 0, 0, True)
        rtn.x = self.x + tv.x
        rtn.y = self.y + tv.y
        rtn.z = self.z + tv.z
        if not ra:
            rtn = rtn.trans()
        return rtn

    # vector - vector : vector + (-vector)
    def __sub__(self, tv):
        ra = self.ra
        if not self.ra:
            self = self.trans()
        if not tv.ra:
            tv = tv.trans()
        if (self.ra != tv.ra):
            tv = tv.trans()
        rtn = Trivec(0, 0, 0, True)
        rtn.x = self.x - tv.x
        rtn.y = self.y - tv.y
        rtn.z = self.z - tv.z
        if not ra:
            rtn = rtn.trans()
        return rtn

    # index * vector : every dimension * index
    # note : only r * index in polar
    def __mul__(self, index):
        ra = self.ra
        if ra:
            self = self.trans()
        rtn = Trivec(0, 0, 0, False)
        rtn.x = self.x * index
        rtn.y = self.y
        rtn.z = self.z
        if ra:
            self = self.trans()
        return rtn

    # both lmul and rmul are ok
    def __rmul__(self, index):
        return self * index

    # determine whether 2 vectors are equal
    # when every dimension are equal, they are equal
    def __eq__(self, tv) :
        if (self.ra != tv.ra):
            tv = tv.trans()
        return self.x == tv.x and self.y == tv.y and self.z == tv.z
    
    def __ne__(self, tv) :
        if (self.ra != tv.ra):
            tv = tv.trans()
        return not (self == tv)

    # test func, to print out the numbers
    def __repr__(self) :
        s = "(%.4f, %.4f, %.4f) " % (self.x, self.y, self.z)
        if self.ra == True:
            s = s + "in Rectangular"
        else:
            s = s + "in Polar"
        return s

    # make it to string
    def toString(self):
        s = "(%.4f, %.4f, %.4f) " % (self.x, self.y, self.z)
        if self.ra == True:
            s = s + "in Rectangular"
        else:
            s = s + "in Polar"
        return s

    # rec -> polar
    def rtop(self):
        r = sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        # cos(theta) = x / rxy, if rxy == 0 then theta can have all values
        # theta in [0, 2pi)
        if self.y > 0 or (self.y == 0 and self.x != 0):
            theta = acos(self.x / sqrt(self.x ** 2 + self.y ** 2))
        elif self.y < 0:
            theta = 2 * pi - acos(self.x / sqrt(self.x ** 2 + self.y ** 2))
        else :
            theta = 0
        # cos(fi) = z / r , if r == 0 then fi can have all values
        # fi in [0, pi]
        if r != 0:
            fi = acos(self.z / r)
        else:
            fi = 0
        return Trivec(r, theta, fi, False)

    # polar -> rec
    def ptor(self):
        x = self.x * sin(self.z) * cos(self.y)
        y = self.x * sin(self.z) * sin(self.y)
        z = self.x * cos(self.z)
        return Trivec(x, y, z, True)
    
    # trans rec -> polar or polar -> rec
    def trans(self):
        if self.ra == True:
            rtn = self.rtop()            
        else:
            rtn = self.ptor()
        return rtn

    # to clear a data from a 3dvector
    def clear(self):
        self.x = 0
        self.y = 0
        self.z = 0

    # L2 view position
    def getL2Pos(self, basex, basey):
        ra = self.ra
        if not ra:
            self.trans()
        temp = (0.5 ** 0.5) * self.x
        y = basey - (self.z - temp)
        x = basex + (self.y - temp)
        if not ra:
            self.trans()
        return x, y

    # three view drawing - Main View
    def getMainPos(self, basex, basey):
        ra = self.ra
        if not ra:
            self.trans()
        x = basex + self.y
        y = basey - self.z
        if not ra:
            self.trans()
        return x, y

    # three view drawing - Top View
    def getTopPos(self, basex, basey):
        ra = self.ra
        if not ra:
            self.trans()
        x = basex + self.y
        y = basey + self.x
        if not ra:
            self.trans()
        return x, y

    # three view drawing - Side View
    def getLeftPos(self, basex, basey):
        ra = self.ra
        if not ra:
            self.trans()
        x = basex + self.x
        y = basey - self.z
        if not ra:
            self.trans()
        return x, y

'''
def main():
    t1 = Trivec(1, 1, 1, True)
    t2 = Trivec(-1, -1, -1, True)
    t3 = Trivec(1, 0, 1, True)
    print t1 == t3
    t4 = t1
    print t1 == t4
    print (t1 + t2)
    print (t2 - t3)
    t1 = t1.trans()
    t2 = t2.trans()
    print (t1 + t2)
    print (t1 - t3)
    print t1
    t1 = t1.trans()
    print t1
    t1 = t1.trans()
    print t1
    return

main()
'''
