from tkinter import *
from tkinter import font

def InitScreen():
    fontTitle = font.Font(g_Tk, size=14, weight='bold')
    frameTitle = Frame(g_Tk, padx=10, pady=10)
    frameTitle.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, padx=10, pady=10)
    frameEntry.pack(side="top", fill="x")
    frameCheck = Frame(g_Tk, padx=10, pady=10, bg='orange')
    frameCheck.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10, bg='green')
    frameList.pack(side="bottom", fill="both", expand=True)

    MainText = Label(frameTitle, font=fontTitle, text="경기도 동물 시설 검색 APP")
    MainText.pack(anchor="center", fill="both")
    
    global InputLabel
    InputLabel = Entry(frameEntry, width=40, borderwidth=12, relief='ridge')
    InputLabel.pack(side="left", expand=True)

    SearchButton = Button(frameEntry, text="검색")
    SearchButton.pack(side="right", expand=True, fill="both")

    # global SearchListBox
    # LBScrollbar = Scrollbar(frameCombo)
    # SearchListBox = Listbox(frameCombo, activestyle='none', width=10, height=1, borderwidth=10, relief='ridge', yscrollcommand=LBScrollbar.set)
    # slist = ["동물 병원", "동물 약국", "유기 동물 보호소"]
    # for i, s in enumerate(slist):
    #     SearchListBox.insert(i,s)
    # SearchListBox.pack(side='left', padx=10, expand=True, fill='both')
    # LBScrollbar.pack(side="left")
    # LBScrollbar.config(command=SearchListBox.yview)
    # sendEmailButton = Button(frameCombo, text='이메일')
    # sendEmailButton.pack(side='right', padx=10, fill='y')

    chkValue = []
    strCheck = ['약국', '유기 동물 보호소', '장묘 업체', '기타']
    for i, s in enumerate(strCheck):
        chkValue.append(IntVar())
        Checkbutton(frameCheck, text=s, variable=chkValue[i]).pack(side="left")

    SubText3 = Label(frameList, text="test4")
    SubText3.pack(anchor="center", fill="both")

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

InitScreen()
g_Tk.mainloop()