def isOdd(N):
    value = True
    if N % 2 == 0 or N == 1:
        value = False
    return value


isodd = lambda n: n + 1


def main():
    N = eval(input("请输入一个整数:"))
    print(isOdd(N))


main()
