

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])

    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    x = [1, 2, 3, 4, 5, 6]

    m1, m2 = max2(x)
    print(m1, m2)


if __name__ == '__main__':
    main()
