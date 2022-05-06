from tkinter import *

def InitScreen():
    frameTitle = Frame(g_Tk, padx=10, pady=10, bg='red')
    frameTitle.pack(side="top", fill="x")
    frameCombo = Frame(g_Tk, padx=10, pady=10, bg='orange')
    frameCombo.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, padx=10, pady=10, bg='yellow')
    frameEntry.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='green')
    frameList.pack(side="bottom", fill="both", expand=True)

    MainText = Label(frameTitle, text="test")
    MainText.pack(anchor="center", fill="both")
    SubText = Label(frameCombo, text="test2")
    SubText.pack(anchor="center", fill="both")
    SubText2 = Label(frameEntry, text="test3")
    SubText2.pack(anchor="center", fill="both")
    SubText3 = Label(frameList, text="test4")
    SubText3.pack(anchor="center", fill="both")

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

InitScreen()
g_Tk.mainloop()