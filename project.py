from ast import parse
from tkinter import *
from tkinter import font
from http.client import HTTPSConnection
from xml.dom.minidom import Element

conn = None
server = "openapi.gg.go.kr"
url = "/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96"

def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)

def getHospitalDataFromXml():
    global server, conn
    if conn == None:
        connectOpenAPIServer()
    conn.request("GET", url)
    req = conn.getresponse()
    if int(req.status) == 200:
        return SearchHospital(req.read().decode('utf-8'))

def event_for_listbox(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        data = event.widget.get(index)
        print(data)

def onSearch():
    getHospitalDataFromXml()

def getStr(s):
    return '' if not s else s

def SearchHospital(strXml):
    from xml.etree import ElementTree

    global listBox
    listBox.delete(0, listBox.size())
    
    parseData = ElementTree.fromstring(strXml)
    
    itemElements = parseData.iter("row")

    i = 1

    for item in itemElements:
        sigun = item.find("SIGUN_NM")

        if InputLabel.get() in sigun.text:
            _text = '[' + str(i) + ']' + getStr(item.find('BIZPLC_NM').text) + ':' + getStr(item.find('SIGUN_NM').text) + ':' + getStr(item.find('LOCPLC_FACLT_TELNO').text)
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

    SearchButton = Button(frameEntry, text="검색", command=onSearch)
    SearchButton.pack(side="right", expand=True, fill="both")

    chkValue = []
    strCheck = ['약국', '보호소', '장묘', '기타']
    for i, s in enumerate(strCheck):
        chkValue.append(IntVar())
        Checkbutton(frameCheck, text=s, borderwidth=10, variable=chkValue[i]).pack(side="left", expand=True)

    sendEmailButton = Button(frameCheck, text='이메일')
    sendEmailButton.pack(side='right', expand=True, fill="both")

    global listBox
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