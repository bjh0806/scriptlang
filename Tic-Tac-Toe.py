from tkinter import *

def onClick(event):
    global currentToken
    if currentToken % 2 == 0:
        i = int((event.x_root - 10) / 35)
        j = int((event.y_root - 30) / 40)
        images[j][i].config(file=x_file)
        frameText.config(text=text2)
    else:
        i = int((event.x_root - 10) / 35)
        j = int((event.y_root - 30) / 40)
        images[j][i].config(file=o_file)
        frameText.config(text=text1)
    currentToken += 1
    print(event.x_root, event.y_root)
    print(i, j)

g_Tk = Tk()
g_Tk.geometry("105x160+0+0")

e_file = "empty.gif"
x_file = "x.gif"
o_file = "o.gif"

images = [[PhotoImage(file = e_file) for i in range(3)] for j in range(3)]
cells = [[Label(g_Tk, image=images[i][j]) for i in range(3)] for j in range(3)]

# for i in range(3):
#     for j in range(3):
#         cells[i][j].place(x=j*40, y=i*45)

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

text1 = "x 차례"
text2 = "o 차례"

frameText = Label(frame, text=text1)
frameText.pack(anchor="center", fill="both")

g_Tk.mainloop()