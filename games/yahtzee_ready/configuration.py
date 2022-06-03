from dice import *

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        # TODO: 구현
        num = 0
        count = [0 for i in range(6)]
        list = []
        ccount = 1
        for i in range(6):
            if i == row:
                for j in range(5):
                    if Dice.getRoll(dices[j]) == row + 1:
                        num += (row + 1)
        if row == 8:
            for i in range(5):
                count[Dice.getRoll(dices[i]) - 1] += 1
            for i in range(6):
                if count[i] >= 3:
                    for j in range(6):
                        num += count[j] * (j + 1)
                        if j == 5:
                            break
        if row == 9:
            for i in range(5):
                count[Dice.getRoll(dices[i]) - 1] += 1
            for i in range(6):
                if count[i] >= 4:
                    for j in range(6):
                        num += count[j] * (j + 1)
                        if j == 5:
                            break
        if row == 10:
            for i in range(5):
                count[Dice.getRoll(dices[i]) - 1] += 1
            if 3 in count and 2 in count:
                num = 25
        if row == 11:
            for i in range(5):
                list.append(Dice.getRoll(dices[i]))
            list.sort()
            for i in range(4):
                if list[i + 1] == list[i]:
                    continue
                elif list[i + 1] == list[i] + 1:
                    ccount += 1
                else:
                    ccount = 1
            if ccount >= 4:
                num = 30
        if row == 12:
            for i in range(5):
                list.append(Dice.getRoll(dices[i]))
            list.sort()
            for i in range(4):
                if list[i + 1] == list[i]:
                    continue
                elif list[i + 1] == list[i] + 1:
                    ccount += 1
                else:
                    ccount = 1
            if ccount >= 5:
                num = 40
        if row == 13:
            first = Dice.getRoll(dices[0])
            for i in range(5):
                if Dice.getRoll(dices[i]) != first:
                    return 0
            num = 50
        if row == 14:
            for i in range(5):
                num += Dice.getRoll(dices[i])
        if 6 <= row <= 7 or 15 <= row <= 16:
            return -1
        else:
            return num

