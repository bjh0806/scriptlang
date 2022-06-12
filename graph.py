from tkinter import font

def drawGraph(g_Tk, category, canvas, data, canvasWidth, canvasHeight):
    fontText = font.Font(g_Tk, size=12, family='배달의민족 한나체 Air')
    canvas.delete("grim")

    if not len(data):
        canvas.create_text(canvasWidth/2, (canvasHeight/2), font=fontText, text="검색 시 그래프 출력", tags="grim")
        return

    nData = len(data)
    nMax = max(data)

    canvas.create_rectangle(0, 0, canvasWidth, canvasHeight, fill='white', tag="grim")

    if nMax == 0:
        nMax = 1

    rectWidth = (canvasWidth // nData)
    bottom = canvasHeight - 20
    maxheight = canvasHeight - 40
    for i in range(nData):
        if category == '동물약국' and i == 1:
            color="orange"
        elif category == '유기동물 보호시설' and i == 2:
            color="yellow"
        elif category == '동물 장묘 허가업체' and i == 3:
            color="green"
        elif category == '동물용 의료용구 판매업체' and i == 4:
            color="blue"
        elif (category == '동물병원' or category == '검색 옵션 설정') and i == 0:
            color="red"
        else:
            color="grey"

        curHeight = maxheight * data[i] / nMax
        top = bottom - curHeight
        left = i * rectWidth
        right = (i + 1) * rectWidth
        canvas.create_rectangle(left, top, right, bottom, fill=color, tag="grim", activefill='navy')
        canvas.create_text((left+right)//2, top-10, text=data[i], tags="grim")
        if i == 0:
            canvas.create_text((left+right)//2, bottom+10, font=fontText, text='병원', tags="grim")
        elif i == 1:
            canvas.create_text((left+right)//2, bottom+10, font=fontText, text='약국', tags="grim")
        elif i == 2:
            canvas.create_text((left+right)//2, bottom+10, font=fontText, text='보호', tags="grim")
        elif i == 3:
            canvas.create_text((left+right)//2, bottom+10, font=fontText, text='장묘', tags="grim")
        else:
            canvas.create_text((left+right)//2, bottom+10, font=fontText, text='의료용구', tags="grim")