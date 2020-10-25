def isOdd(N):
    value = True
    if N % 2 == 0:
        value = False
    return value


def main():
    N = eval(input("请输入一个整数:"))
    print(isOdd(N))


main()
