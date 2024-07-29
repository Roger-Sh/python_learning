def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')           # find element reversely
    if 0 < pos < len(filename) - 1:
        if has_dot:
            index = pos
        else:
            index = pos+1

        return filename[index:]
    else:
        return ''


def main():
    file_name = 'file.txt'
    file_extent = get_suffix(file_name, has_dot=True)
    print(file_extent)

    file_name = 'file.txt.exe'
    file_extent = get_suffix(file_name, has_dot=True)
    print(file_extent)

    file_name = 'file.txt...exe'
    file_extent = get_suffix(file_name, has_dot=True)
    print(file_extent)


if __name__ == '__main__':
    main()
