import sys
import telepot
from urllib.request import urlopen
import traceback
from xml.etree import ElementTree
from urllib.parse import quote

TOKEN = '5553940355:AAHQN9hpjXh_uHdeZnA14R_xWYiEf5MFONs'
MAX_MSG_LENGTH = 300
bot = telepot.Bot(TOKEN)

def getStr(s):
    return '' if not s else s

def getData(loc_param, category_param):
    res_list = []
    if category_param == '약국':
        url = 'https://openapi.gg.go.kr/AnimalPharmacy?KEY=80e0c92a5694415ea393e4481125d632&SIGUN_NM=' + quote(loc_param)
    elif category_param == '보호':
        url = 'https://openapi.gg.go.kr/OrganicAnimalProtectionFacilit?KEY=855ef34a84c84c44a4226774f236406a&SIGUN_NM=' + quote(loc_param)
    elif category_param == '장묘':
        url = 'https://openapi.gg.go.kr/DoanmalfunrlPrmisnentrp?KEY=0e630d78165442a59187a6de5fb0e55f&SIGUN_NM=' + quote(loc_param)
    elif category_param == '의료용구':
        url = 'https://openapi.gg.go.kr/AnimalMedicalCareThing?KEY=2fd131ecbf784976954fc6678468c173&SIGUN_NM=' + quote(loc_param)
    else:
        url = 'https://openapi.gg.go.kr/Animalhosptl?KEY=cbd2ad3e942d4831a1c412193d392e96&SIGUN_NM=' + quote(loc_param)
    res_body = urlopen(url).read()
    strXml = res_body.decode('utf-8')
    tree = ElementTree.fromstring(strXml)

    items = tree.iter("row")

    for item in items:
        if category_param == '보호':
            row = getStr(item.find('ENTRPS_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('ENTRPS_TELNO').text)
            res_list.append(row)
        elif category_param == '장묘':
            row = getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('TELNO').text)
            res_list.append(row)
        elif getStr(item.find('BSN_STATE_NM').text) != '폐업' and getStr(item.find('BSN_STATE_NM').text) != '말소':
            row = getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('LOCPLC_FACLT_TELNO').text)
            res_list.append(row)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)