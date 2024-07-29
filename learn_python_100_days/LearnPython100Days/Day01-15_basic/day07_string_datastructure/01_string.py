def main():

    s1 = 'hello, world!'
    s2 = "\nhello, world!"

    # 以三个双引号或单引号开头的字符串可以折行
    s3 = """
    hello, 
    world!
    """
    print(s1, s2, s3, end='')

    # 前者是八进制的表示法，后者是十六进制的表示法
    s1 = '\141\142\143\x61\x62\x63'     # abcabc
    s2 = '\u9a86\u660a'                 # 骆昊
    print(s1, s2)

    # 不希望字符串中的\表示转义，我们可以通过在字符串的最前面加上字母r来加以说明
    s1 = r'\'hello, world!\''
    s2 = r'\n\\hello, world!\\\n'
    print(s1, s2, end='')

    # string *
    s1 = 'hello ' * 3
    print(s1)  # hello hello hello

    # string + string
    s2 = 'world'
    s1 += s2
    print(s1)  # hello hello hello world

    # string in
    print('ll' in s1)  # True
    print('good' in s1)  # False

    # 从字符串中取出指定位置的字符(下标运算)
    str2 = 'abc123456'
    print(str2[2])  # c
    print(str2[0])  # a

    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45

    str1 = 'hello, world!'

    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13

    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())  # Hello, world!

    # 获得字符串每个单词首字母大写的拷贝
    print(str1.title())  # Hello, World!

    # 获得字符串变大写后的拷贝
    print(str1.upper())  # HELLO, WORLD!

    # 从字符串中查找子串所在位置
    print(str1.find('or'))  # 8
    print(str1.find('shit'))  # -1

    # 与find类似但找不到子串时会引发异常
    print(str1.index('or'))         # 8
    # print(str1.index('shit'))       # ValueError: substring not found

    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('He'))  # False
    print(str1.startswith('hel'))  # True

    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('!'))  # True

    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))     # ******************hello, world!*******************

    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50, ' '))      # hello, world!
    str2 = 'abc123456'

    # 检查字符串是否由数字构成
    print(str2.isdigit())  # False

    # 检查字符串是否以字母构成
    print(str2.isalpha())  # False

    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())  # True

    str3 = '    jackfrued@126.com   '
    print(str3)

    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())

    # 格式化输出字符串
    a, b = 5, 10
    print('%d * %d = %d' % (a, b, a * b))
    print('{0} * {1} = {2}'.format(a, b, a * b))
    print(f'{a} * {b} = {a * b}')

if __name__ == '__main__':
    main()
