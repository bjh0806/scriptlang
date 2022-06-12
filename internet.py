from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree import ElementTree

conn = None
server = "openapi.gg.go.kr"

def getStr(s):
    return '' if not s else s

def connectOpenAPIServer():
    global server
    return HTTPSConnection(server)

def userURIBuilder(uri, position):
    if position.endswith("시") != True:
        position += "시"
    str = uri + quote(position)
    return str

def getHospitalDataFromXml(category, position):
    global conn
    if conn == None:
        conn = connectOpenAPIServer()
    if category == '동물약국':
        uri = userURIBuilder("/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=", position)
    elif category == '유기동물 보호시설':
        uri = userURIBuilder("/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=", position)
    elif category == '동물 장묘 허가업체':
        uri = userURIBuilder("/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=", position)
    elif category == '동물용 의료용구 판매업체':
        uri = userURIBuilder("/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=", position)
    else:
        uri = userURIBuilder("/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=", position)
    conn.request("GET", uri)
    req = conn.getresponse()
    if int(req.status) == 200:
        return req.read()

def getData(position):
    global server, conn
    GraphData = []
    Data = [0, 0, 0, 0, 0]
    if conn == None:
        connectOpenAPIServer()
    for i in range(5):
        if i == 1:
            uri = userURIBuilder("/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=", position)
        elif i == 2:
            uri = userURIBuilder("/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=", position)
        elif i == 3:
            uri = userURIBuilder("/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=", position)
        elif i == 4:
            uri = userURIBuilder("/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=", position)
        else:
            uri = userURIBuilder("/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=", position)
        conn.request("GET", uri)
        req = conn.getresponse()
        if int(req.status) == 200:
            parseData = ElementTree.fromstring(req.read())
            itemElements = parseData.iter("row")
            j = 1

            for item in itemElements:
                if i == 2:
                    j = j + 1
                elif i == 3:
                    j = j + 1
                elif getStr(item.find('BSN_STATE_NM').text) != '폐업' and getStr(item.find('BSN_STATE_NM').text) != '말소':
                    j = j + 1
        Data[i] = j - 1

    for i in range(5):
        GraphData.append(Data[i])

    return GraphData