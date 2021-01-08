from random import randint


def birthday_paradox(num):
    birthday_dict = {}
    index = 0
    for i in range(num):
        birthday_dict[i] = randint(1, 365)
    for i in range(num):
        for j in range(num) and not i:
            if birthday_dict[j] == birthday_dict[i]:
                index += 1
                break
    print("The possible is {:.2%}".format(index/num))


def main():
    birthday_paradox(eval(input("请输入人数:")))


main()
