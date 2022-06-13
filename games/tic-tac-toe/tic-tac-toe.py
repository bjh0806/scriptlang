from tkinter import *

class Cell(Label):
    def __init__(self, token):
        self.token = token
        self.xcount = 0     # 전체 x 개수
        self.ocount = 0     # 전체 o 개수

    def delete(self, line):     # x, o 개수 초기화
        if line == 'g':         # 가로
            self.xcount_g = 0
            self.ocount_g = 0
        if line == 's':         # 세로
            self.xcount_s = 0
            self.ocount_s = 0
        if line == 'num':       # 대각선
            self.xcount_1 = 0
            self.ocount_1 = 0
            self.xcount_2 = 0
            self.ocount_2 = 0

    def flip(self):
        global currentToken
        if self.xcount + self.ocount == 9:
            statusLabel.config(text="비김!")

        # 가로 판정
        for i in range(3):
            self.delete('g')
            for j in range(3):
                if cells[i][j].token == 'X':
                    self.xcount_g += 1
                elif cells[i][j].token == 'O':
                    self.ocount_g += 1
                if j == 2:
                    if self.xcount_g == 3:
                        statusLabel.config(text="X 승리!")
                        currentToken = -1
                    elif self.ocount_g == 3:
                        statusLabel.config(text="O 승리!")
                        currentToken = -1

        # 세로 판정
        for j in range(3):
            self.delete('s')
            for i in range(3):
                if cells[i][j].token == 'X':
                    self.xcount_s += 1
                elif cells[i][j].token == 'O':
                    self.ocount_s += 1
                if i == 2:
                    if self.xcount_s == 3:
                        statusLabel.config(text="X 승리!")
                        currentToken = -1
                    elif self.ocount_s == 3:
                        statusLabel.config(text="O 승리!")
                        currentToken = -1

        # 대각선 판정
        self.delete('num')
        for i in range(3):
            for j in range(3):
                if i == j:
                    if cells[i][j].token == 'X':
                        self.xcount_1 += 1
                    elif cells[i][j].token == 'O':
                        self.ocount_1 += 1
                if i == 2 and j == 2:
                    if self.xcount_1 == 3:
                        statusLabel.config(text="X 승리!")
                        currentToken = -1
                    elif self.ocount_1 == 3:
                        statusLabel.config(text="O 승리!")
                        currentToken = -1
                if i + j == 2:
                    if cells[i][j].token == 'X':
                        self.xcount_2 += 1
                    elif cells[i][j].token == 'O':
                        self.ocount_2 += 1
                if (i == 0 and j == 2) or (i == 2 and j == 0):
                    if self.xcount_2 == 3:
                        statusLabel.config(text="X 승리!")
                        currentToken = -1
                    elif self.ocount_2 == 3:
                        statusLabel.config(text="O 승리!")
                        currentToken = -1  

def onClick(event):
    global currentToken
    if currentToken % 2 == 0 and currentToken != -1:
        i = int((event.x_root - 10) / 40)
        j = int((event.y_root - 30) / 45)
        if 0 <= i < 3 and 0 <= j < 3:
            if cells[j][i].token == ' ':
                images[j][i].config(file=x_file)
                cells[j][i].token = 'X'
                cell.xcount += 1
                statusLabel.config(text=text2)
                currentToken += 1
    elif currentToken % 2 == 1 and currentToken != -1:
        i = int((event.x_root - 10) / 40)
        j = int((event.y_root - 30) / 45)
        if 0 <= i < 3 and 0 <= j < 3:
            if cells[j][i].token == ' ':
                images[j][i].config(file=o_file)
                cells[j][i].token = 'O'
                cell.ocount += 1
                statusLabel.config(text=text1)
                currentToken += 1

    cell.flip()

g_Tk = Tk()
cell = Cell(' ')
g_Tk.geometry("105x160+0+0")

e_file = "games/empty.gif"
x_file = "games/x.gif"
o_file = "games/o.gif"

images = [[PhotoImage(file = e_file) for i in range(3)] for j in range(3)]
cells = [[Cell(' ') for i in range(3)] for j in range(3)]

frame1 = Frame(g_Tk)
frame1.pack(side="top", fill="x")
frame2 = Frame(g_Tk)
frame2.pack(side="top", fill="x")
frame3 = Frame(g_Tk)
frame3.pack(side="top", fill="x")

for i in range(3):
    frame1Text = Label(frame1, image=images[0][i])
    frame1Text.pack(side='left', fill="both")
    frame2Text = Label(frame2, image=images[1][i])
    frame2Text.pack(side='left', fill="both")
    frame3Text = Label(frame3, image=images[2][i])
    frame3Text.pack(side='left', fill="both")

currentToken = 0

g_Tk.bind("<Button-1>", onClick)

frame = Frame(g_Tk, padx=10, pady=3)
frame.pack(side="bottom", fill="x")

text1 = "X 차례"
text2 = "O 차례"

statusLabel = Label(frame, text=text1)
statusLabel.pack(anchor="center", fill="both")

g_Tk.mainloop()