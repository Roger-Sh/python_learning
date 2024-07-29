"""
井字棋游戏

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])  # top
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])  # middle
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])  # bottom


def main():
    # 初始化井字棋字典
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }

    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'                  # 下棋者
        counter = 0                 # 步数
        os.system('cls')            # linux: clear
        print()
        print_board(curr_board)

        while counter < 9:
            move = input('轮到%s走棋, 请输入位置: ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn

                # 切换下棋者
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'

            os.system('cls')
            print()

            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
