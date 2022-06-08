import sys
import traceback
from xml.etree import ElementTree
from xml.dom.minidom import parseString
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
import re
from datetime import date, datetime
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

    items = tree.iter("item")
    for item in items:
        if category_param == '보호':
            row = getStr(item.find('ENTRPS_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('ENTRPS_TELNO').text)
        elif category_param == '장묘':
            row = getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('TELNO').text)
        elif getStr(item.find('BSN_STATE_NM').text) != '폐업' and getStr(item.find('BSN_STATE_NM').text) != '말소':
            row = getStr(item.find('BIZPLC_NM').text) + ' : ' + getStr(item.find('REFINE_ROADNM_ADDR').text) + ' / ' + getStr(item.find('LOCPLC_FACLT_TELNO').text)
        res_list.append(row)
    print(res_list)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exception(*sys.exc_info(), file=sys.stdout)

def replyData(user, loc_param, category_param='병원'):
    print(user, loc_param, category_param)
    res_list = getData(loc_param, category_param)

    msg = ''
    for r in res_list:
        print(str(datetime.now()).split('.')[0], r)
        if len(r + msg) + 1 > MAX_MSG_LENGTH:
            sendMessage(user, msg)
            msg = r + '\n'
        else:
            msg += r + '\n'
    if msg:
        sendMessage(user, msg)
    else:
        sendMessage(user, '%s 지역에 해당하는 데이터가 없습니다.' % loc_param)

def save(user, loc_param):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        sendMessage(user, '이미 해당 정보가 저장되어 있습니다.')
        return
    else:
        sendMessage(user, '저장되었습니다.')
        conn.commit()

def check(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, location TEXT, PRIMARY KEY(user, location))')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id: ' + str(data[0]) + ', location: ' + data[1]
        sendMessage(user, row)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        sendMessage(chat_id, '텍스트 이외의 메시지는 처리가 불가능합니다.')
        return
    text = msg['text']
    args = text.split(' ')
    if text.startswith('약국') and len(args) > 1:
        print('try to 약국', args[0])
    elif text.startswith('보호') and len(args) > 1:
        print('try to 보호', args[0])
    elif text.startswith('장묘') and len(args) > 1:
        print('try to 장묘', args[0])
    elif text.startswith('의료용구') and len(args) > 1:
        print('try to 의료용구', args[0])
    elif len(args) > 1:
        print('try to 병원', args[0])
    replyData(chat_id, args[1], args[0])

pprint(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)