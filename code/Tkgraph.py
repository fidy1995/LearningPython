###################
# Class Tkgraph:
#     The controller of GUI.
###################
from Tkinter import *
from Tktribody import *
from Tkdatawin import *
from datapack import *
from tkMessageBox import *
import thread

class Tkgraph:
    # P/V operations to protect shared data for thread
    def P(self):
        if self.lock <= 0:
            return False
        elif self.lock > 0:
            self.lock = self.lock - 1
            return True

    def V(self):
        self.lock = self.lock + 1
        
    # move one step
    def move(self, event):
        if not self.dwopen:
            self.tb.planetMove()
            if self.lock == 0:
                self.V()

    # run the animation
    def runAnimation(self):
        while not self.stopped:
            self.tb.planetMove()
            sleep(self.tb.tb.t)
            # in order to debug, i made the time faster
            # sleep(self.tb.tb.t)
        self.V()
        thread.exit_thread()

    # doing things to prepare for animation
    def run(self, event):
        # if the datawin is open, then the buttons are not working
        if not self.dwopen and self.P(): # lock the thread
            self.b[1].destroy()
            self.b[3].destroy()
            self.b[2] = Button(self.rt, text = "stop")
            self.b[2].bind("<1>", self.stop)
            self.b[2].grid(row = 2, column = 0)
            self.stopped = False
            # i use multiple thread here in order to receive signals when drawing pictures
            thread.start_new_thread(self.runAnimation, ())

    # stop the animation
    def stop(self, event):
        if not self.dwopen: # same as upper function
            self.b[2].destroy()
            self.stopped = True
            sleep(0.2)
            self.b[1] = Button(self.rt, text = "start")
            self.b[1].bind("<1>", self.run)
            self.b[1].grid(row = 2, column = 0)
            self.b[3] = Button(self.rt, text = "next")
            self.b[3].bind("<1>", self.move)
            self.b[3].grid(row = 2, column = 1)

    # stop and quit the program
    def hide(self, event):
        if not self.stopped:
            self.stop(event)
        if askokcancel("Quit", "Are you sure want to quit?"):
            self.rt.destroy()

    # the wrapper of generateDatawin
    def generateDatawin_w(self, event):
        if not self.stopped:
            self.stop(event)
        self.generateDatawin()

    # the drawer and binder of buttons
    def generateMainButtons(self):
        self.b[1] = Button(self.rt, text = "start")
        #self.b[2] = Button(self.rt, text = "stop")
        self.b[3] = Button(self.rt, text = "next")
        self.b[4] = Button(self.rt, text = "Settings")
        self.b[5] = Button(self.rt, text = "quit")
        self.b[1].bind("<1>", self.run)
        #self.b[2].bind("<1>", self.stop)
        self.b[3].bind("<1>", self.move)
        self.b[4].bind("<1>", self.generateDatawin_w)
        self.b[5].bind("<1>", self.hide)
        self.b[1].grid(row = 2, column = 0)
        self.b[3].grid(row = 2, column = 1)
        self.b[4].grid(row = 2, column = 2)
        self.b[5].grid(row = 2, column = 3)

    # to paint the three-body system
    def showTbwin(self):
        self.tb.show()
        self.generateMainButtons()

    # to generate the data of tribody
    def generateTribody(self, d):
        pl1 = Planet(d[1], d[2], d[0])
        pl2 = Planet(d[4], d[5], d[3])
        pl3 = Planet(d[7], d[8], d[6])
        pl = [pl1, pl2, pl3]
        return Tribody(pl)

    # hide the datawin
    def hideDatawin(self, event):
        self.dw.hide()
        self.tp.destroy()
        self.dwopen = False

    # accept data and hide datawin
    def acceptData(self, event):
        d = self.dw.getData()
        self.dp = Datapack(d)
        errno = self.dp.check()
        if errno == SAFE:
            self.b[0].destroy()
            self.hideDatawin(event)
            self.tb = Tktribody(self.rt, self.generateTribody(self.dp.d))
            self.dwopen = False
            self.showTbwin()
        elif errno == ERR_NUM:
            showwarning("Input error", "Your input is not a number")
        elif errno == ERR_INV:
            showwarning("Input error", "Mass cannot below zero")
        elif errno == ERR_COL:
            showwarning("Input error", "Position cannot be the same")
            
    # to paint the datawin
    def generateDatawin(self):
        if self.dwopen == False:
            self.dwopen = True
            self.tp = Toplevel(self.rt)
            self.tp.title("Settings")
            self.dw = Tkdatawin(self.tp)
            self.dw.b[0].bind("<1>", self.acceptData)
            self.dw.b[1].bind("<1>", self.hideDatawin)
            self.dw.show()

    # when the program starts, it should provide the datawin
    def startProgram(self, event):
        self.generateDatawin()

    # to print a button on the program
    def generateStartButton(self):
        self.b[0] = Button(self.rt, text = "Let's ROCK!!!")
        self.b[0].bind("<1>", self.startProgram)
        self.b[0].pack()
        self.rt.mainloop()

    # constructor
    def __init__(self):
        self.rt = Tk()
        self.tp = 0
        self.tb = 0
        self.dw = 0
        self.b = [0] * 6
        self.dp = 0
        self.dwopen = False
        self.lock = 1
        #self.stopped = True
        self.generateStartButton()

    # destructor
    def __del__(self):
        del self.rt, self.tp, self.tb, self.dw, self.b, self.dp, self.dwopen
