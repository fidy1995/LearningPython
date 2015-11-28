####################
# Class Tktribody:
#     The GUI of the tribody.
####################
from Tkinter import *
from tribody import *

# bases
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300
MID_WIDTH = CANVAS_WIDTH / 2
MID_HEIGHT = CANVAS_HEIGHT / 2
START = 0
PLANET_R = 7 # the diametre / 2 of the planets
TEXT = 24 # the font of text
TEXT_BLANK = TEXT + 12 # the place of text

class Tktribody:
    # generate labels
    def generateLabels(self):
        self.label[0] = Label(self.tbc[0], text = "M", fg = "cyan", bg = "black", font = TEXT)
        self.label[1] = Label(self.tbc[1], text = "L", fg = "cyan", bg = "black", font = TEXT)
        self.label[2] = Label(self.tbc[2], text = "T", fg = "cyan", bg = "black", font = TEXT)
        self.label[3] = Label(self.tbc[3], text = "L2", fg = "#9B009B", bg = "black", font = TEXT)
        self.label[0].place(x = CANVAS_WIDTH - TEXT_BLANK, y = CANVAS_HEIGHT - TEXT_BLANK)
        self.label[1].place(x = TEXT_BLANK, y = CANVAS_HEIGHT - TEXT_BLANK)
        self.label[2].place(x = CANVAS_WIDTH - TEXT_BLANK, y = TEXT_BLANK)
        self.label[3].place(x = TEXT_BLANK, y = TEXT_BLANK)
    
    # to generate 4 canvas for 4 views
    def generateCanvas(self):
        for i in range(4):
            self.tbc[i] = Canvas(self.tbf, width = 400, height = 300, bg = "black")
            self.tbc[i].grid(row = i / 2, column = 2 * (i % 2), columnspan = 2)
        self.generateLabels()
    
    # to generate the lines between canvas
    def generateLines(self):
        self.lines[0] = self.tbc[1].create_line(START, START, START, CANVAS_HEIGHT, fill = "white", width = 3)
        self.lines[1] = self.tbc[2].create_line(START, START, CANVAS_WIDTH, START, fill = "white", width = 3)
        self.lines[2] = self.tbc[3].create_line(START, START, START, CANVAS_HEIGHT, fill = "white", width = 3)
        self.lines[3] = self.tbc[3].create_line(START, START, CANVAS_WIDTH, START, fill = "white", width = 3)

    # axis painter
    def generateAxis(self):
        # main view axis: x->y, y->z
        self.axis[0] = self.tbc[0].create_line(MID_WIDTH, MID_HEIGHT, MID_WIDTH, START, fill = "cyan", width = 2, arrow = "last")
        self.axis[1] = self.tbc[0].create_line(MID_WIDTH, MID_HEIGHT, CANVAS_WIDTH, MID_HEIGHT, fill = "cyan", width = 2, arrow = "last")
        # left view axis: x->x, y->z
        self.axis[2] = self.tbc[1].create_line(MID_WIDTH, MID_HEIGHT, MID_WIDTH, START, fill = "cyan", width = 2, arrow = "last")
        self.axis[3] = self.tbc[1].create_line(MID_WIDTH, MID_HEIGHT, CANVAS_WIDTH, MID_HEIGHT, fill = "cyan", width = 2, arrow = "last")
        # top view axis: x->y, y->-x
        self.axis[4] = self.tbc[2].create_line(MID_WIDTH, MID_HEIGHT, MID_WIDTH, CANVAS_HEIGHT, fill = "cyan", width = 2, arrow = "last")
        self.axis[5] = self.tbc[2].create_line(MID_WIDTH, MID_HEIGHT, CANVAS_WIDTH, MID_HEIGHT, fill = "cyan", width = 2, arrow = "last")
        # L-2 view axis: x->y, y->z, (x/2 + y/2)->x
        self.axis[6] = self.tbc[3].create_line(MID_WIDTH, MID_HEIGHT, MID_WIDTH, START, fill = "cyan", width = 2, arrow = "last")
        self.axis[7] = self.tbc[3].create_line(MID_WIDTH, MID_HEIGHT, CANVAS_WIDTH, MID_HEIGHT, fill = "cyan", width = 2, arrow = "last")
        self.axis[8] = self.tbc[3].create_line(MID_WIDTH, MID_HEIGHT, MID_WIDTH - MID_HEIGHT, CANVAS_HEIGHT,
                                               fill = "cyan", width = 2, arrow = "last")

    # to paint the planets
    def generatePlanets(self):
        color = ["red", "green", "blue"]
        for i in range(3):
            pos = self.tb.getPlanetPos(i, MID_WIDTH, MID_HEIGHT)
            for j in range(4):
                self.planets[4 * i + j] = self.tbc[j].create_oval(pos[2 * j] - PLANET_R, pos[2 * j + 1] - PLANET_R,
                                                                  pos[2 * j] + PLANET_R, pos[2 * j + 1] + PLANET_R, fill = color[i])

    # to refresh the position of the planets
    def refreshPlanets(self):
        for i in range(12):
            self.tbc[i/4].delete(self.planets[i])
        self.generatePlanets()

    # to move the planets
    def planetMove(self):        
        self.tb.cal()
        # redraw the canvas every 5 seconds to clear the rubbish
        if self.count == 50:
            for i in range(4):
                self.tbc[i].destroy()
            self.generateCanvas()
            self.count = 0
        self.generateAxis()
        self.refreshPlanets()
        self.count = self.count + 1

    # constructor
    def __init__(self, root, tb):
        self.tbf = Frame(root, width = 800, height = 600)
        self.tb = tb
        self.tbc = [0] * 4
        self.label = [0] * 4
        self.lines = [0] * 4
        self.planets = [0] * 12
        self.axis = [0] * 9
        self.count = 0

    # destructor
    def __del__(self):
        del self.tbf, self.tb, self.tbc, self.label, self.lines, self.planets, self.axis, self.count

    # to show the canvas
    def show(self):
        self.tbf.grid(row = 0, column = 0, rowspan = 2, columnspan = 4)
        self.generateCanvas()
        self.generateLines()
        self.generateAxis()
        self.generatePlanets()

    # hide the canvas
    def hide(self):
        self.tbc.destroy()
