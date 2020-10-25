a = eval(input("请输入第一个数：\n"))
b = eval(input("请输入第二个数：\n"))
product = a*b
while b != 0:
    temp = a % b
    a = b
    b = temp
else:print("最大公约数为{}，最小公倍数为：{}".format(a, product/a))
