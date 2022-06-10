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
    if (text.startswith('병원') or text.startswith('약국') or text.startswith('보호') or text.startswith('장묘') or text.startswith('의료용구')) and len(args) > 1:
        replyData(chat_id, args[1], args[0])
    else:
        noti.sendMessage(chat_id, "- 도움말 -\n\n경기도 동물 시설 검색 봇입니다.\n\n카테고리는 < 동물병원 >, < 동물약국 >, < 유기동물 보호시설 >, < 동물 장묘 허가업체 >, < 동물용 의료용구 판매업체 >로 총 5가지입니다.\n\n검색을 위해서는 < 카테고리 > < 지역명 > 순으로 입력을 해주세요.\n\n카테고리의 경우 < 병원 >, < 약국 >, < 보호 >, < 장묘 >, < 의료용구 > 중 하나를, 지역명의 경우 ~시 형태로 입력해야 합니다. (수원 x, 수원시 o)\n입력 예시) 수원시의 동물병원을 검색하고 싶은 경우: 병원 수원시, 시흥시의 동물약국을 검색하고 싶은 경우: 약국 시흥시\n\n요구 조건에 맞추어 입력을 완료하면 해당 지역의 동물 시설 리스트가 출력됩니다.")

pprint(noti.bot.getMe())

noti.bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)