"""
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...


Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    # 输入行数
    num = int(input('Number of rows: '))

    # 初始化二维列表
    yh = [[]] * num

    #对于每一行
    for row in range(len(yh)):
        # 初始化每一列的元素
        yh[row] = [None] * (row + 1)

        # 对于每一行的每一个元素
        for col in range(len(yh[row])):

            # 第一个元素 和 最后一个元素为1
            if col == 0 or col == row:
                yh[row][col] = 1

            # 中间每一个元素为上一行的同一列元素加上上一行的前一列元素
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]

            # 打印
            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    main()
