from msilib.schema import ListBox
from tkinter import *
from tkinter import font

def event_for_listbox(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

def onSearch():
    global SearchListBox
    sels = SearchListBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        SearchHospital()
    elif iSearchIndex == 1:
        pass
    elif iSearchIndex == 2:
        pass
    elif iSearchIndex == 3:
        pass

def getStr(s):
    return '' if not s else S

def SearchHospital():
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())

    with open('xml 파일명', 'rb') as f:
        strXml = f.read().decode('utf-8')
    parseData = ElementTree.fromstring(strXml)

    elements = parseData.iter('row')

    i = 1

    for item in elements:
        part_el = item.find('CODE_VALUE')

        if InputLabel.get() not in part_el.text:
            continue

        _text = '[' + str(i) + ']' + getStr(item.find('이름').text) + ':' + getStr(item.find('주소').text) + ':' + getStr(item.find('전화번호').text)
        listBox.insert(i - 1, _text)
        i = i + 1

def InitScreen():
    fontTitle = font.Font(g_Tk, size=14, weight='bold')
    frameTitle = Frame(g_Tk, padx=10, pady=10)
    frameTitle.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, padx=10, pady=10)
    frameEntry.pack(side="top", fill="x")
    frameCheck = Frame(g_Tk, padx=10, pady=10)
    frameCheck.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10, pady=10)
    frameList.pack(side="top", fill="x")
    frameGraph = Frame(g_Tk, padx=10, pady=10)
    frameGraph.pack(side="bottom", fill="both", expand=True)

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
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    listBox.pack(side='left', anchor='nw', fill='x')
    LBScrollbar.pack(side="right", anchor='ne', fill='y')
    LBScrollbar.config(comman=listBox.yview)

    global GraphBox
    GraphBox = Listbox(frameGraph, selectmode='extended', width=35, borderwidth=12, relief='ridge')
    GraphBox.pack(side='right', fill='y')

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

InitScreen()
g_Tk.mainloop()