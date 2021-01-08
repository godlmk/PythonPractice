def is_repeat(ls):
    flag = True
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i] == ls[j]:
                flag = False
    return flag


ls = [1, 2, 34, 4, 42, 3, 4]
print(is_repeat(ls))
print(ls)