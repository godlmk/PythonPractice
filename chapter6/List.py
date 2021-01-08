def delete_min(ls):
    ls1 = ls.copy()
    for i in range(len(ls)):
        ls[i] = min(ls1)
        ls1.remove(min(ls1))


def delete_max(ls):
    ls1 = ls.copy()
    for i in range(len(ls)):
        ls[i] = max(ls1)
        ls1.remove(max(ls1))


def main():
    delete_max([2, 5, 7, 1, 6])
    ls1 = [30, 1, 2, 0]
    ls2 = [30, 21, 133]
    print(ls1 > ls2)
    ls = [[2, 3, 7], [[3, 5], 3], [0, 9]]
    print(ls)


main()
