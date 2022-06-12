from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from xml.etree import ElementTree
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import folium
import webbrowser
import spam
from image import *
from internet import *
from graph import *

popup = inputEmail = btnEmail = None
addrEmail = None

def onEmailInput():
    global addrEmail
    addrEmail = inputEmail.get()
    msg = MIMEMultipart('alternative')
    if SearchComboBox.get() == '검색 옵션 설정':
        msg['Subject'] = '동물 시설 검색 결과 - {}'.format(InputLabel.get())
    else:
        msg['Subject'] = '동물 시설 검색 결과 - {} / {}'.format(InputLabel.get(), SearchComboBox.get())
    for i in range(100):
        HtmlPart = MIMEText('{}\n'.format(str(listBox.get(i))), 'html', _charset = 'UTF-8')
        msg.attach(HtmlPart)
    sendMail('skscjswoz1@gmail.com', addrEmail, msg)
    popup.destroy()

def onEmailPopup(event):
    global g_Tk, addrEmail, popup
    addrEmail = None
    popup = Toplevel(g_Tk)
    popup.geometry("300x150")
    popup.title("받을 이메일 주소 입력")

    global inputEmail, btnEmail
    inputEmail = Entry(popup, width=200)
    inputEmail.pack(fill='x', padx=10, expand=True)

    btnEmail = Button(popup, text="확인", command=onEmailInput)
    btnEmail.pack(anchor="s", padx=10, pady=10)

def sendMail(fromAddr, toAddr, msg):
    import smtplib
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()

    s.login('skscjswoz1@gmail.com', 'hzyzzjteuahhhlhm')
    s.sendmail(fromAddr, [toAddr], msg.as_string())
    s.close()

def Pressed(event):
    global listBox, parseData

    sels = listBox.curselection()
    iSearchIndex = 0 if len(sels) == 0 else listBox.curselection()[0]

    itemElements = parseData.iter("row")

    i = 0

    for item in itemElements:
        if SearchComboBox.get() == '유기동물 보호시설':
            if i == iSearchIndex:
                locationx = item.find('REFINE_WGS84_LAT').text
                locationy = item.find('REFINE_WGS84_LOGT').text
                name = getStr(item.find('ENTRPS_NM').text)
                map_osm = folium.Map(location=[locationx, locationy], zoom_start=30)
                folium.Marker([locationx, locationy], popup=name).add_to(map_osm)
                map_osm.save('osm.html')
                webbrowser.open_new('osm.html')
            i = i + 1
        elif SearchComboBox.get() == '동물 장묘 허가업체':
            if i == iSearchIndex:
                locationx = item.find('REFINE_WGS84_LAT').text
                locationy = item.find('REFINE_WGS84_LOGT').text
                name = getStr(item.find('BIZPLC_NM').text)
                map_osm = folium.Map(location=[locationx, locationy], zoom_start=30)
                folium.Marker([locationx, locationy], popup=name).add_to(map_osm)
                map_osm.save('osm.html')
                webbrowser.open_new('osm.html')
            i = i + 1
        elif getStr(item.find('BSN_STATE_NM').text) != '폐업' and getStr(item.find('BSN_STATE_NM').text) != '말소':
            if i == iSearchIndex:
                locationx = item.find('REFINE_WGS84_LAT').text
                locationy = item.find('REFINE_WGS84_LOGT').text
                name = getStr(item.find('BIZPLC_NM').text)
                map_osm = folium.Map(location=[locationx, locationy], zoom_start=30)
                folium.Marker([locationx, locationy], popup=name).add_to(map_osm)
                map_osm.save('osm.html')
                webbrowser.open_new('osm.html')
            i = i + 1
        
def onSearch(event):
    global imageLabel
    SearchHospital(getHospitalDataFromXml(SearchComboBox.get(), InputLabel.get()))
    drawGraph(g_Tk, SearchComboBox.get(), GraphBox, getData(InputLabel.get()), 255, 200)
    if SearchComboBox.get() == '동물약국':
        imageLabel.setImage('picture/logo2.png')
    elif SearchComboBox.get() == '유기동물 보호시설':
        imageLabel.setImage('picture/logo3.png')
    elif SearchComboBox.get() == '동물 장묘 허가업체':
        imageLabel.setImage('picture/logo4.png')
    elif SearchComboBox.get() == '동물용 의료용구 판매업체':
        imageLabel.setImage('picture/logo5.png')
    else:
        imageLabel.setImage('picture/logo.png')

def SearchHospital(strXml):
    global listBox, parseData
    listBox.delete(0, listBox.size())
    
    parseData = ElementTree.fromstring(strXml)
    
    itemElements = parseData.iter("row")

    i = 1

    for item in itemElements:
        if SearchComboBox.get() == '유기동물 보호시설':
            _text = str(i) + '. ' + getStr(item.find('ENTRPS_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('ENTRPS_TELNO').text)
            listBox.insert(i - 1, _text)
            i = i + 1
        elif SearchComboBox.get() == '동물 장묘 허가업체':
            _text = str(i) + '. ' + getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('TELNO').text)
            listBox.insert(i - 1, _text)
            i = i + 1
        elif getStr(item.find('BSN_STATE_NM').text) != '폐업' and getStr(item.find('BSN_STATE_NM').text) != '말소':
            _text = str(i) + '. ' + getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('LOCPLC_FACLT_TELNO').text)
            listBox.insert(i - 1, _text)
            i = i + 1
    
    listBox.insert(100, '--------------------------------')
    listBox.insert(100, '{0}{1}개를 확인하였습니다.'.format(spam.result(), spam.num(i)))

def InitScreen():
    global imageLabel, fontText
    fontTitle = font.Font(g_Tk, size=14, family='배달의민족 한나는 열한살')
    fontText = font.Font(g_Tk, size=12, family='배달의민족 한나체 Air')
    frameTitle = Frame(g_Tk, padx=10, pady=10)
    frameTitle.pack(side="top", fill="x")
    frameEntry = Frame(g_Tk, padx=10, pady=5)
    frameEntry.pack(side="top", fill="x")
    frameCheck = Frame(g_Tk, padx=10, pady=5)
    frameCheck.pack(side="top", fill="x")
    frameList = Frame(g_Tk, padx=10)
    frameList.pack(side="top", fill="x")
    frameGraph = Frame(g_Tk, padx=10, pady=10)
    frameGraph.pack(side="bottom", fill="both", expand=True)

    MainText = Label(frameTitle, font=fontTitle, text="경기도 동물 시설 검색 APP")
    MainText.pack(anchor="center", fill="both")
    
    global InputLabel
    InputLabel = Entry(frameEntry, width=32, borderwidth=12, relief='ridge', font=fontText)
    InputLabel.insert(0, '지역명 입력')
    InputLabel.pack(side="left", expand=True)

    SearchButton = ImageButton(frameEntry, width=20, height=20)
    SearchButton.setImage('picture/glass.png')
    SearchButton.bind('<Button-1>', onSearch)
    SearchButton.pack(side="right", expand=True, fill="both")

    global SearchComboBox
    slist = ['동물병원', '동물약국', '유기동물 보호시설', '동물 장묘 허가업체', '동물용 의료용구 판매업체']
    SearchComboBox = ttk.Combobox(frameCheck, width=30, height=5, values=slist, font=fontText)
    SearchComboBox.set("검색 옵션 설정")
    SearchComboBox.pack(side='left', expand=True)

    sendEmailButton = ImageButton(frameCheck, width=35, height=25)
    sendEmailButton.setImage('picture/gmail.png')
    sendEmailButton.bind('<Button-1>', onEmailPopup)
    sendEmailButton.pack(side='right', expand=True, fill="both")

    global listBox
    LBScrollbar = Scrollbar(frameList)
    UBScrollbar = Scrollbar(frameList, orient='horizontal')
    listBox = Listbox(frameList, selectmode='extended', width=50, height=11, borderwidth=12, relief='ridge', font=fontText, xscrollcommand=UBScrollbar.set, yscrollcommand=LBScrollbar.set)
    LBScrollbar.pack(side="right", fill='y')
    LBScrollbar.config(command=listBox.yview)
    UBScrollbar.pack(side="bottom", fill='x')
    UBScrollbar.config(command=listBox.xview)
    listBox.pack(side='left', fill='x')

    global GraphBox, GraphData
    GraphData = []
    GraphBox = Canvas(frameGraph, width=253)
    GraphBox.pack(side='right', fill='y')
    drawGraph(g_Tk, SearchComboBox.get(), GraphBox, GraphData, 255, 200)
    imageLabel = ImageLabel(frameGraph, width=100, height=95)
    imageLabel.setImage('picture/logo.png')
    imageLabel.pack()
    imageButton = ImageButton(frameGraph, width=100, height=100)
    imageButton.setImage('picture/map.png')
    imageButton.bind('<Button-1>', Pressed)
    imageButton.pack(side='bottom')

g_Tk = Tk()
g_Tk.geometry("400x600+450+100")
InitScreen()
g_Tk.mainloop()