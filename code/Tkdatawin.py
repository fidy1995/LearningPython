#######################
# Class Tkdatawin:
#     A window to generate data.
#######################
from Tkinter import *

class Tkdatawin:
    # the label painter
    def generateLabels(self):
        self.l[0] = Label(self.c, text = "Planet 1 mass: ")
        self.l[1] = Label(self.c, text = "Position X: ")
        self.l[2] = Label(self.c, text = "Position Y: ")
        self.l[3] = Label(self.c, text = "Position Z: ")
        self.l[4] = Label(self.c, text = "Velocity X: ")
        self.l[5] = Label(self.c, text = "Velocity Y: ")
        self.l[6] = Label(self.c, text = "Velocity Z: ")
        self.l[7] = Label(self.c, text = "Planet 2 mass: ")
        self.l[8] = Label(self.c, text = "Position X: ")
        self.l[9] = Label(self.c, text = "Position Y: ")
        self.l[10] = Label(self.c, text = "Position Z: ")
        self.l[11] = Label(self.c, text = "Velocity X: ")
        self.l[12] = Label(self.c, text = "Velocity Y: ")
        self.l[13] = Label(self.c, text = "Velocity Z: ")
        self.l[14] = Label(self.c, text = "Planet 3 mass: ")
        self.l[15] = Label(self.c, text = "Position X: ")
        self.l[16] = Label(self.c, text = "Position Y: ")
        self.l[17] = Label(self.c, text = "Position Z: ")
        self.l[18] = Label(self.c, text = "Velocity X: ")
        self.l[19] = Label(self.c, text = "Velocity Y: ")
        self.l[20] = Label(self.c, text = "Velocity Z: ")
        for i in range(21):
            r = (i + 2 + 2 * (i / 7)) / 3
            if i % 7 != 0:
                col = (i - 1 - i / 7) % 3 * 2
            else:
                col = 0
            self.l[i].grid(row = r, column = col)

    # entry painters, getting data
    def generateEntries(self):
        for i in range(21):
            self.e[i] = Entry(self.c)
            r = (i + 2 + 2 * (i / 7)) / 3
            if i % 7 != 0:
                col = (i - i / 7 - 1) % 3 * 2 + 1
            else:
                col = 1
            self.e[i].grid(row = r, column = col)

    # show this window
    def show(self):
        self.c.pack()

    # hide this window
    def hide(self):
        self.c.destroy()

    # generate data from entries
    def getData(self):
        data = [0] * 21
        for i in range(21):
            data[i] = self.e[i].get()
        return data

    # button drawers, bind in the graphwin
    def generateButtons(self):
        self.b[0] = Button(self.c, text = "OK")
        self.b[1] = Button(self.c, text = "cancel")
        #self.b[0].bind("<Button-1>", self.accept)
        #self.b[1].bind("<Button-1>", self.hide)
        self.b[0].grid(row = 9, column = 2)
        self.b[1].grid(row = 9, column = 3)

    # constructor
    def __init__(self, root):
        self.c = Canvas(root, width = 640, height = 480)
        # debug info
        # self.c.grid()
        # debug info
        self.l = [Label()] * 21
        self.e = [Entry()] * 21
        self.b = [Button()] * 2
        self.generateLabels()
        self.generateEntries()
        self.generateButtons()

    # destructor
    def __del__(self):
        del self.c, self.l, self.e, self.b

'''
root = Tk()

def cb(event):
    root.destroy()    

def main():    
    b = Button(root, text = "ok")
    b.bind("<Button-1>", cb)
    b.grid()
    if Tkdatawin(root):
        0
    root.mainloop()
main()
'''
        
