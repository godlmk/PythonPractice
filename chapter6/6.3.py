def is_repeat(ls):
    set_of_list = set(ls)
    if len(ls) == len(set_of_list):
        flag = True
    else:
        flag = False
    return flag


ls = [1, 2, 3, 4]
print(is_repeat(ls))