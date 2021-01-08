from math import pow, floor


def is_prime(n):
    flag = True
    try:
        for i in range(2, n-1):
            if n % i == 0:
                flag = False
    except NameError:
        print("传入的值不正确")
    return flag


def main():
    print(is_prime(eval(input("请输入一个整数:"))))


main()
