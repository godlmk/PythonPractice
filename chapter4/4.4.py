from random import randint
i = randint(0, 100)
n = 0
j = eval(input("请输入一个0到100的整数:"))
while i != j:
    if j < i:
        print("遗憾，太小了")
    elif j > i:
        print("遗憾，太大了")
    n = n + 1
    j = eval(input("再输一个："))
else:
    print("预测{}次，你猜中了".format(n))
