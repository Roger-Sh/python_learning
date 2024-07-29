import os
import time


def main():
    content = '北京第三区交通委提醒您：道路千万条，安全第一条；行车不规范，亲人两行泪。'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()