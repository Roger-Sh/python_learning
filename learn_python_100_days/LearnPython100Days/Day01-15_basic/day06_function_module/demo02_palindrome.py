def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10      # 余数 相加
        temp //= 10                         # 去掉余数保留侍卫及以上
    return total == num                     # 判断原数与其反写的数是否相同


print(is_palindrome(10101))