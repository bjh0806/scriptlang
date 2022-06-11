from http.client import HTTPSConnection
from xml.dom.minidom import Element
from project import *

conn = None
server = "openapi.gg.go.kr"

class Internet:
    def connectOpenAPIServer(self):
        global conn, server
        conn = HTTPSConnection(server)

    def userURIBuilder(self, uri, position):
        if "시" not in position:
            position += "시"
        str = uri + quote(position)
        return str

    def getHospitalDataFromXml(self):
        global server, conn
        if conn == None:
            self.connectOpenAPIServer()
        if SearchComboBox.get() == '동물약국':
            uri = self.userURIBuilder("/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=", InputLabel.get())
        elif SearchComboBox.get() == '유기동물 보호시설':
            uri = self.userURIBuilder("/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=", InputLabel.get())
        elif SearchComboBox.get() == '동물 장묘 허가업체':
            uri = self.userURIBuilder("/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=", InputLabel.get())
        elif SearchComboBox.get() == '동물용 의료용구 판매업체':
            uri = self.userURIBuilder("/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=", InputLabel.get())
        else:
            uri = self.userURIBuilder("/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=", InputLabel.get())
        conn.request("GET", uri)
        req = conn.getresponse()
        if int(req.status) == 200:
            return SearchHospital(req.read())

    def getData(self):
        global server, conn
        GraphData = []
        Data = [0, 0, 0, 0, 0]
        if conn == None:
            self.connectOpenAPIServer()
        for i in range(5):
            if i == 1:
                uri = self.userURIBuilder("/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=", InputLabel.get())
            elif i == 2:
                uri = self.userURIBuilder("/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=", InputLabel.get())
            elif i == 3:
                uri = self.userURIBuilder("/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=", InputLabel.get())
            elif i == 4:
                uri = self.userURIBuilder("/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=", InputLabel.get())
            else:
                uri = self.userURIBuilder("/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=", InputLabel.get())
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

        drawGraph(GraphBox, GraphData, 255, 200)