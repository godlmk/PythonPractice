def multi(*num):
    product = 1
    count = 0
    for i in num:
        if type(i) is int or isinstance(i, float):
            product *= i
        else:
            print("存在不能相乘的数字:{}".format(num[count]))
            return
        count += 1
    return product


def main():
    print(multi(1, 2, 3, 4, ))


main()
