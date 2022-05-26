from ast import parse
from tkinter import *
from tkinter import font
from http.client import HTTPSConnection
from turtle import bgcolor
from xml.dom.minidom import Element
from urllib.parse import quote
import tkinter.ttk as ttk

conn = None
server = "openapi.gg.go.kr"

def connectOpenAPIServer():
    global conn, server
    conn = HTTPSConnection(server)

def userURIBuilder(uri, position):
    if "시" not in position:
        position += "시"
    str = uri + quote(position)
    return str

def getHospitalDataFromXml():
    global server, conn
    if conn == None:
        connectOpenAPIServer()
    if SearchComboBox.get() == '동물약국':
        uri = userURIBuilder("/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=", InputLabel.get())
    if SearchComboBox.get() == '유기동물 보호시설':
        uri = userURIBuilder("/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=", InputLabel.get())
    if SearchComboBox.get() == '동물 장묘 허가업체':
        uri = userURIBuilder("/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=", InputLabel.get())
    if SearchComboBox.get() == '동물용 의료용구 판매업체':
        uri = userURIBuilder("/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=", InputLabel.get())
    else:
        uri = userURIBuilder("/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=", InputLabel.get())
    conn.request("GET", uri)
    req = conn.getresponse()
    if int(req.status) == 200:
        return SearchHospital(req.read())

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
        if SearchComboBox.get() == '유기동물 보호시설':
            _text = str(i) + '. ' + getStr(item.find('ENTRPS_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('ENTRPS_TELNO').text)
            listBox.insert(i - 1, _text)
            i = i + 1
        if SearchComboBox.get() == '동물 장묘 허가업체':
            _text = str(i) + '. ' + getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('TELNO').text)
            listBox.insert(i - 1, _text)
            i = i + 1
        elif getStr(item.find('BSN_STATE_NM').text) != '폐업':
            _text = str(i) + '. ' + getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('LOCPLC_FACLT_TELNO').text)
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
    frameList = Frame(g_Tk, padx=10)
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

    global SearchComboBox
    slist = ['동물병원', '동물약국', '유기동물 보호시설', '동물 장묘 허가업체', '동물용 의료용구 판매업체']
    SearchComboBox = ttk.Combobox(frameCheck, width=37, height=5, values=slist)
    SearchComboBox.set("검색 옵션 설정")
    SearchComboBox.pack(side='left', expand=True)

    # global chkValue
    # chkValue = []
    # strCheck = ['약국', '보호소', '장묘', '기타']
    # for i, s in enumerate(strCheck):
    #     chkValue.append(IntVar())
    #     Checkbutton(frameCheck, text=s, borderwidth=10, variable=chkValue[i]).pack(side="left", expand=True)

    sendEmailButton = Button(frameCheck, text='이메일')
    sendEmailButton.pack(side='right', expand=True, fill="both")

    global listBox
    LBScrollbar = Scrollbar(frameList)
    UBScrollbar = Scrollbar(frameList, orient='horizontal')
    listBox = Listbox(frameList, selectmode='extended', width=50, height=12, borderwidth=12, relief='ridge', xscrollcommand=UBScrollbar.set, yscrollcommand=LBScrollbar.set)
    listBox.bind('<<ListboxSelect>>', event_for_listbox)
    LBScrollbar.pack(side="right", fill='y')
    LBScrollbar.config(command=listBox.yview)
    UBScrollbar.pack(side="bottom", fill='x')
    UBScrollbar.config(command=listBox.xview)
    listBox.pack(side='left', fill='x')

    global GraphBox
    GraphBox = Listbox(frameGraph, selectmode='extended', width=35, borderwidth=12, relief='ridge')
    GraphBox.pack(side='right', fill='y')

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")

InitScreen()
g_Tk.mainloop()