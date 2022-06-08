import time
import telepot
from pprint import pprint
import noti

def replyData(user, loc_param, category_param='병원'):
    res_list = noti.getData(loc_param, category_param)

    msg = ''
    for r in res_list:
        if len(r + msg) + 1 > noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r + '\n'
        else:
            msg += r + '\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, '%s 지역에 해당하는 데이터가 없습니다.' % loc_param)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '텍스트 이외의 메시지는 처리가 불가능합니다.')
        return
    text = msg['text']
    args = text.split(' ')
    replyData(chat_id, args[1], args[0])

pprint(noti.bot.getMe())

noti.bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)