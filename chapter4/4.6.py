from random import randint

times = eval(input("请输入想玩的次数："))
pick_change_times = 0
pick_first_times = 0
for i in range(times):
    car = randint(0, 2)
    pick_first = randint(0, 2)
    if pick_first == car:
        pick_first_times += 1
    else:
        pick_change_times += 1
pick_first_percent = pick_first_times / times
pick_change_percent = pick_change_times / times
print("坚持选择猜对的概率为{:.2f}%，改变选择猜对的概率为{:.2f}%".format(pick_first_percent * 100,\
                                                   pick_change_percent * 100))
