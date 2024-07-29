"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reversed
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: all / any / id / input / open / print / type

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


def myfilter(mystr):
    return len(mystr) == 6


# help()
print(chr(0x9a86))              # 骆
print(hex(ord('骆')))            # 0x9a86

print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))


fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])

# 输出符合myfilter的内容
fruits2 = list(filter(myfilter, fruits))    #定义一个filter, 并用filter()去使用这个filter
print(fruits)
print(fruits2)
