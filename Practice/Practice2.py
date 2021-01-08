from random import randint


def product_info():
    info = {}
    for i in range(1, 31):
        name = ("std" + str(i), i)
        sore = randint(55, 100)
        info[name] = sore
    return info


def calculation(info):
    s = 0
    for key in info:
        s += info.get(key)
    avr = s / len(info)
    print("平均值是:{}".format(avr))
    sores = info.values()
    sdev = sum([(x - avr) ** 2 for x in sores])
    sdev = sdev / (len(sores))
    print("最大值是{}".format(max(sores)))
    print("最小值是{}".format(min(sores)))
    print("方差是{}".format(sdev))


def main():
    info = product_info()
    items = list(info.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(items)):
        print(items[i])
    print(info)
    calculation(info)


main()
