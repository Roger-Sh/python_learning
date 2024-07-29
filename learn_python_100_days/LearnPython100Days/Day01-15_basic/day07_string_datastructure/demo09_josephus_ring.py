"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""


def main():
    # 初始化30个人
    persons = [True] * 30
    counter, index, number = 0, 0, 0

    while counter < 15:                     # 当扔下去的人数小于15时
        if persons[index]:                  # 若当前的人还未扔下去， 即跳过扔下去的人
            number += 1                     # 当前的人开始报数
            if number == 9:                 # 如果数字为9
                persons[index] = False      # 把此人扔下去
                counter += 1                # 扔下去的人数+1
                number = 0                  # 重新开始计数
        index += 1                          # 开始下一个人
        index %= 30                         # 若人数到达30人，则从头开始
    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()