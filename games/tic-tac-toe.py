from tkinter import *

class Cell(Label):
    def __init__(self, token):
        self.token = token

def onClick(event):
    global currentToken, xcount, ocount
    if currentToken % 2 == 0 and currentToken != -1:
        i = int((event.x_root - 10) / 40)
        j = int((event.y_root - 30) / 45)
        if 0 <= i < 3 and 0 <= j < 3:
            if cells[j][i].token == ' ':
                images[j][i].config(file=x_file)
                cells[j][i].token = 'X'
                xcount += 1
                statusLabel.config(text=text2)
                currentToken += 1
    elif currentToken % 2 == 1 and currentToken != -1:
        i = int((event.x_root - 10) / 40)
        j = int((event.y_root - 30) / 45)
        if 0 <= i < 3 and 0 <= j < 3:
            if cells[j][i].token == ' ':
                images[j][i].config(file=o_file)
                cells[j][i].token = 'O'
                ocount += 1
                statusLabel.config(text=text1)
                currentToken += 1
    
    flip()

def flip():
    global currentToken
    if xcount + ocount == 9:
        statusLabel.config(text="비김!")

    # 가로 판정
    for i in range(3):
        xcount_g = 0
        ocount_g = 0
        for j in range(3):
            if cells[i][j].token == 'X':
                xcount_g += 1
            elif cells[i][j].token == 'O':
                ocount_g += 1
            if j == 2:
                if xcount_g == 3:
                    statusLabel.config(text="X 승리!")
                    currentToken = -1
                elif ocount_g == 3:
                    statusLabel.config(text="O 승리!")
                    currentToken = -1

    # 세로 판정
    for j in range(3):
        xcount_s = 0
        ocount_s = 0
        for i in range(3):
            if cells[i][j].token == 'X':
                xcount_s += 1
            elif cells[i][j].token == 'O':
                ocount_s += 1
            if i == 2:
                if xcount_s == 3:
                    statusLabel.config(text="X 승리!")
                    currentToken = -1
                elif ocount_s == 3:
                    statusLabel.config(text="O 승리!")
                    currentToken = -1

    # 대각선 판정
    xcount_1 = 0
    ocount_1 = 0
    xcount_2 = 0
    ocount_2 = 0

    for i in range(3):
        for j in range(3):
            if i == j:
                if cells[i][j].token == 'X':
                    xcount_1 += 1
                elif cells[i][j].token == 'O':
                    ocount_1 += 1
            if i == 2 and j == 2:
                if xcount_1 == 3:
                    statusLabel.config(text="X 승리!")
                    currentToken = -1
                elif ocount_1 == 3:
                    statusLabel.config(text="O 승리!")
                    currentToken = -1
            if i + j == 2:
                if cells[i][j].token == 'X':
                    xcount_2 += 1
                elif cells[i][j].token == 'O':
                    ocount_2 += 1
            if (i == 0 and j == 2) or (i == 2 and j == 0):
                if xcount_2 == 3:
                    statusLabel.config(text="X 승리!")
                    currentToken = -1
                elif ocount_2 == 3:
                    statusLabel.config(text="O 승리!")
                    currentToken = -1  

g_Tk = Tk()
g_Tk.geometry("105x160+0+0")

e_file = "games/empty.gif"
x_file = "games/x.gif"
o_file = "games/o.gif"

xcount = 0
ocount = 0

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