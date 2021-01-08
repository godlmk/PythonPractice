def han_nuo(n, str1, str2, str3):
    if n == 1:
        print("将圆盘{}从{}移到{}".format(n, str1, str3))
        '''递归终止条件，第一个盘子上面没有盘子，所以不需要像前面的盘子那样先把它上面的盘子移到B在将自己移到C，
        最后将上面的盘子从B移到C那样操作，直接将它移到C柱子上即可'''
    else:
        han_nuo(n - 1, str1, str3, str2)  # 将第n个盘子之上的所有盘子（n-1个）从A柱子移到B柱子上
        print("将圆盘{}从{}移到{}".format(n, str1, str3))  # 将第n个盘子从A柱子移到C柱子上
        han_nuo(n - 1, str2, str1, str3)  # 将前面从A移到B柱子的n-1个盘子移到C柱子上


def main():
    han_nuo(3, 'A', 'B', 'C')


main()
