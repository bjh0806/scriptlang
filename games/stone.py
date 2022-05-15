from tkinter import *

class Cell(Canvas):
    def __init__(self, parent, row, col, width=20, height=20):
        Canvas.__init__(self, parent, width=width, height=height, bg="blue", borderwidth=2)
        self.color = "white"
        self.row = row
        self.col = col
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)
    
    def clicked(self, event):
        if self.color == "white" and end != 1:
            if self.row == 5 or (self.row <= 4 and cell[self.row + 1][self.col].color != "white"):
                nextcolor = "red" if Turn != "red" else "yellow"
                self.setColor(nextcolor)
                self.__checkCount()
                self.__checkVertical()
                self.__checkHorizontal()
                self.__checkDiag1()
                self.__checkDiag2()

    def setColor(self, color):
        global Turn
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill=self.color, tags="oval")
        Turn = color

    def __checkCount(self):
        count = 0
        for i in range(_MAXROW):
            for j in range(_MAXCOL):
                if cell[i][j].color != "white":
                    count += 1
                if count == 42:
                    process_button.config(text="승자 없음!")

    def __checkVertical(self):
        global end
        for j in range(_MAXCOL):
            self.rcount_s = 0
            self.ycount_s = 0
            for i in range(_MAXROW):
                if cell[i][j].color == "red":
                    self.rstarti = i
                    self.rstartj = j
                    self.rcount_s += 1
                    self.ycount_s = 0
                elif cell[i][j].color == "yellow":
                    self.ystarti = i
                    self.ystartj = j
                    self.ycount_s += 1
                    self.rcount_s = 0
                elif cell[i][j].color == "white":
                    self.rcount_s = 0
                    self.ycount_s = 0
                if self.rcount_s == 4:
                    for k in range(4):
                        cell[self.rstarti - k][self.rstartj].config(bg="red")
                    process_button.config(text="red 승리!")
                    end = 1
                elif self.ycount_s == 4:
                    for k in range(4):
                        cell[self.ystarti - k][self.ystartj].config(bg="yellow")
                    process_button.config(text="yellow 승리!")
                    end = 1

    def __checkHorizontal(self):
        global end
        for i in range(_MAXROW):
            self.rcount_g = 0
            self.ycount_g = 0
            for j in range(_MAXCOL):
                if cell[i][j].color == "red":
                    self.rstarti = i
                    self.rstartj = j
                    self.rcount_g += 1
                    self.ycount_g = 0
                elif cell[i][j].color == "yellow":
                    self.ystarti = i
                    self.ystartj = j
                    self.ycount_g += 1
                    self.rcount_g = 0
                elif cell[i][j].color == "white":
                    self.rcount_g = 0
                    self.ycount_g = 0
                if self.rcount_g == 4:
                    for k in range(4):
                        cell[self.rstarti][self.rstartj - k].config(bg="red")
                    process_button.config(text="red 승리!")
                    end = 1
                elif self.ycount_g == 4:
                    for k in range(4):
                        cell[self.ystarti][self.ystartj - k].config(bg="yellow")
                    process_button.config(text="yellow 승리!")
                    end = 1

    def __checkDiag1(self):
        global end
        for i in range(_MAXROW):
            for j in range(_MAXCOL):
                self.rcount_1 = 0
                self.ycount_1 = 0
                for k in range(4):
                    if i - k >= 0 and j + k < _MAXCOL:
                        if cell[i - k][j + k].color == "red":
                            self.rstarti = i
                            self.rstartj = j
                            self.rcount_1 += 1
                            self.ycount_1 = 0
                        elif cell[i - k][j + k].color == "yellow":
                            self.ystarti = i
                            self.ystartj = j
                            self.ycount_1 += 1
                            self.rcount_1 = 0
                        elif cell[i - k][j + k].color == "white":
                            self.rcount_1 = 0
                            self.ycount_1 = 0
                    if self.rcount_1 == 4:
                        for k in range(4):
                            cell[self.rstarti - k][self.rstartj + k].config(bg="red")
                        process_button.config(text="red 승리!")
                        end = 1
                    elif self.ycount_1 == 4:
                        for k in range(4):
                            cell[self.ystarti - k][self.ystartj + k].config(bg="yellow")
                        process_button.config(text="yellow 승리!")
                        end = 1

    def __checkDiag2(self):
        global end
        for i in range(_MAXROW):
            for j in range(_MAXCOL):
                self.rcount_2 = 0
                self.ycount_2 = 0
                for k in range(4):
                    if i - k >= 0 and j - k >= 0:
                        if cell[i - k][j - k].color == "red":
                            self.rstarti = i
                            self.rstartj = j
                            self.rcount_2 += 1
                            self.ycount_2 = 0
                        elif cell[i - k][j - k].color == "yellow":
                            self.ystarti = i
                            self.ystartj = j
                            self.ycount_2 += 1
                            self.rcount_2 = 0
                        elif cell[i - k][j - k].color == "white":
                            self.rcount_2 = 0
                            self.ycount_2 = 0
                    if self.rcount_2 == 4:
                        for k in range(4):
                            cell[self.rstarti - k][self.rstartj - k].config(bg="red")
                        process_button.config(text="red 승리!")
                        end = 1
                    elif self.ycount_2 == 4:
                        for k in range(4):
                            cell[self.ystarti - k][self.ystartj - k].config(bg="yellow")
                        process_button.config(text="yellow 승리!")
                        end = 1

def restart():
    global Turn, end
    for i in range(_MAXROW):
        for j in range(_MAXCOL):
            cell[i][j].delete("oval")
            cell[i][j].color = "white"
            cell[i][j].config(bg="blue")
            cell[i][j].create_oval(4, 4, 20, 20, fill="white", tags="oval")
            process_button.config(text=restart_text)
    Turn = None
    end = 0

window = Tk()
window.title("Connect Four")

_MAXROW = 6
_MAXCOL = 7

Turn = None
end = 0
count = 0
restart_text = "새로 시작"

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()

cell = [[Cell(frame1, i, j, width=20, height=20) for j in range(_MAXCOL)] for i in range(_MAXROW)]

for i in range(_MAXROW):
    for j in range(_MAXCOL):
        cell[i][j].grid(row=i, column=j)

process_button = Button(frame2, text=restart_text)
process_button.pack()

process_button.config(command=restart)

window.mainloop()