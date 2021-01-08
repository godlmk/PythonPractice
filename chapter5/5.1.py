def drawtianzige(n):
    lines = 5 * n + 1
    for i in range(1, lines + 1):
        if i % 5 == 1:
            print("+----" * n, end='')
            print("+")
        else:
            print("|    " * n, end='')
            print("|")


def main():
    n = eval(input("请输入田字格的阶数："))
    drawtianzige(n)


main()
