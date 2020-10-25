weekstr = "一月二月三月四月五月六月七月八月九月十月十一月十二月"
weekid = eval(input("请输入月份数字（1~12）:"))
if weekid < 11:
    pos = (weekid-1)*2
    print(weekstr[pos:pos+2])
else:
    pos = 20+(weekid % 10)*3
    print(weekstr[pos-3:pos])
print("哎\t生活\t爱\tPython\v")