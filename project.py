from msilib.schema import ListBox
from tkinter import *
from tkinter import font

def InitScreen():
    fontTitle = font.Font(g_Tk, size=14, weight='bold')
    frameTitle = Frame(g_Tk, padx=10, pady=10)
    frameTitle.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, padx=10, pady=10)
    frameEntry.pack(side="top", fill="x")
    frameCheck = Frame(g_Tk, padx=10, pady=10)
    frameCheck.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10)
    frameList.pack(side="bottom", fill="both", expand=True)

    MainText = Label(frameTitle, font=fontTitle, text="경기도 동물 시설 검색 APP")
    MainText.pack(anchor="center", fill="both")
    
    global InputLabel
    InputLabel = Entry(frameEntry, width=40, borderwidth=12, relief='ridge')
    InputLabel.pack(side="left", expand=True)

    SearchButton = Button(frameEntry, text="검색")
    SearchButton.pack(side="right", expand=True, fill="both")

    chkValue = []
    strCheck = ['약국', '보호소', '장묘', '기타']
    for i, s in enumerate(strCheck):
        chkValue.append(IntVar())
        Checkbutton(frameCheck, text=s, borderwidth=10, variable=chkValue[i]).pack(side="left", expand=True)

    sendEmailButton = Button(frameCheck, text='이메일')
    sendEmailButton.pack(side='right', expand=True, fill="both")

    global ListBox
    LBScrollbar = Scrollbar(frameList)
    listBox = Listbox(frameList, selectmode='extended', width=47, height=12, borderwidth=12, relief='ridge', yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>')
    listBox.pack(side='left', anchor='n', fill='x')
    LBScrollbar.pack(side="right", anchor='n', fill='y')
    LBScrollbar.config(comman=listBox.yview)

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

InitScreen()
g_Tk.mainloop()