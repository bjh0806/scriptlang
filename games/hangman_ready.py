import math
import random
from tkinter import * # Import tkinter
    
class Hangman:
    def __init__(self):
        self.nCorrectChar = 0
        self.nMissChar = 0
        self.nMissedLetters = []
        self.finished = 0
        self.draw()
        self.setWord()
        self.print()

    def setWord(self):
        self.hiddenWord = [i for i in random.choice(words)]
        self.guessWord = ['*' for i in self.hiddenWord]

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        if self.nMissChar >= 0:
            canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
            canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
            canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        radius = 20 # 반지름

        if self.nMissChar >= 1:
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        # Draw the circle
        if self.nMissChar >= 2:
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger

        # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
        if self.nMissChar >= 3:
            x1 = 160 - radius * math.cos(math.radians(45))
            y1 = 60 + radius * math.sin(math.radians(45))
            x2 = 160 - (radius+60) * math.cos(math.radians(45))
            y2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.nMissChar >= 4:
            x1 = 160 - radius * math.cos(math.radians(135))
            y1 = 60 + radius * math.sin(math.radians(135))
            x2 = 160 - (radius+60) * math.cos(math.radians(135))
            y2 = 60 + (radius+60) * math.sin(math.radians(135))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.nMissChar >= 5:
            canvas.create_line(160, 80, 160, 140, tags = "hangman")

        x1 = 160
        y1 = 140

        if self.nMissChar >= 6:
            x2 = 160 - 60 * math.cos(math.radians(45))
            y2 = 140 + 60 * math.sin(math.radians(45))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

        if self.nMissChar >= 7:
            x2 = 160 - 60 * math.cos(math.radians(135))
            y2 = 140 + 60 * math.sin(math.radians(135))

            canvas.create_line(x1, y1, x2, y2, tags = "hangman")

    def guess(self, letter):
        self.count = 0
        if letter not in self.hiddenWord and letter not in self.nMissedLetters:
            self.nMissChar += 1
            self.draw()
            self.nMissedLetters.append(letter)
        else:
            for i in self.hiddenWord:
                if i == letter:
                    if self.guessWord[self.count] == '*':
                        self.guessWord[self.count] = letter
                        self.nCorrectChar += 1
                self.count += 1
        if self.nCorrectChar == len(self.hiddenWord):
            self.finished = 1
        if self.nMissChar == 7:
            self.finished = 2
        self.print()

    def print(self):
        canvas.delete("word")
        if self.finished == 0:
            canvas.create_text(200, 190, text="단어 추측: {}".format(''.join(self.guessWord)), tags = "word")
            if self.nMissChar > 0:
                canvas.create_text(200, 210, text="틀린 글자: {}".format(''.join(self.nMissedLetters)), tags = "word")
        elif self.finished == 1:
            canvas.create_text(200, 190, text="{} 맞았습니다".format(''.join(self.hiddenWord)), tags = "word")
        elif self.finished == 2:
            canvas.create_text(200, 190, text="정답: {}".format(''.join(self.hiddenWord)), tags = "word")
        if self.finished > 0:
            canvas.create_text(200, 210, text="게임을 계속하려면 ENTER를 누르세요", tags = "word")
        
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    if event.char >= 'a' and event.char <= 'z':
        hangman.guess(event.char)
    elif event.keycode == 13:
        if hangman.finished > 0:
            hangman.__init__()
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop