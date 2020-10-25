def isNum(s):
    value = False
    if type(s) == int or float or complex or s[-1] == 'j':
        value = True
    return value


def main():
    s = eval(input("请输入一个字符串："))
    print(isNum(s))


main()
