from tkinter import *
from tkinter.tix import CELL

class Cell(Canvas):
    def __init__(self, parent, row, col, width=20, height=20):
        Canvas.__init__(self, parent, width=width, height=height, bg="blue", borderwidth=2)
        self.color = "white"
        self.row = row
        self.col = col
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)
    
    def clicked(self, event):
        nextcolor = "red" if Turn != "red" else "yellow"
        self.setColor(nextcolor)

    def setColor(self, color):
        global Turn
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")
        Turn = color

def start():
    global Turn
    for i in range(_MAXROW):
        for j in range(_MAXCOL):
            cell = Cell(frame1, i, j, width=20, height=20)
            cell.grid(row=i, column=j)
    Turn = None

window = Tk()
window.title("Connect Four")

_MAXROW = 6
_MAXCOL = 7

restart_text = "새로 시작"

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()

start()

process_button = Button(frame2, text=restart_text)
process_button.pack()

process_button.config(command=start)

window.mainloop()