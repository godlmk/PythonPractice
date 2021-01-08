import numpy as np
import matplotlib.pyplot as plt
from random import randint
import math

'''初始化数据'''


def init_data():
    data_init = {}
    for k in range(1, 61):
        line = []
        name = ("std" + str(k), k + 4202000)
        for j in range(7):
            line.append(randint(55, 95))
        sore = np.array([x for x in line])
        data_init[name] = sore
    return data_init


def write_document(d):
    """输出每科成绩的csv文件"""

    ls_of_major = []
    for j in range(7):
        for key in d:
            ls_of_major.append(d[key][j])
    a = np.array(ls_of_major).reshape(7, 60)
    for j in range(7):
        a[j] = sorted(a[j], reverse=True)
    for j in range(7):
        np.savetxt("D:/PythonProject/Practice/第{}科成绩.csv".format(j + 1), a[j], fmt='%d', delimiter=',')
    """总成绩输出"""

    s = []
    for key in d:
        s.append(sum(x for x in d.get(key)))

    s = np.array(s)
    title = ['Python程序设计基础', '计算机导论', '离散数学', '数据结构', 'C语言程序设计', 'java语言程序设计', '算法导论', '总分']
    ls = list(d.values())
    ls = np.array(ls)
    ls = np.column_stack((ls, s))
    ds = np.row_stack((title, ls))
    sorted(ds, key=lambda x: x[7], reverse=True)
    np.savetxt("D:/PythonProject/Practice/各个学生成绩.csv", ds, fmt='%s', delimiter=',')
    return ls


def read_document(path):
    ls = []
    f = open(path)
    for line in f:
        line = line.replace('\n', '')
        ls.append(line)
    plt.hist(ls, 60)
    plt.show()
    f.close()


def compute(path):
    f = open(path)
    ds = []
    tot = []
    for line in f:
        line = line.replace("\n", '')
        ds.append(line.split(','))
    f.close()
    print(ds)
    for l in range(1, len(ds)):
        tot.append(int(ds[l][7]))
    print("最大值为{}，最小值为{}，平均数是{}，方差是{}".format(max(tot), min(tot), np.mean(tot), np.var(tot)))


def distance(d1, d2):
    return math.fabs(d1[7] - d2[7])


if __name__ == '__main__':
    data = init_data()
    lt = []
    li = write_document(data)
    compute("D:/PythonProject/Practice/各个学生成绩.csv")
    for i in range(7):
        read_document("D:/PythonProject/Practice/第{}科成绩.csv".format(i + 1))
    num = 0
    for i in range(1, len(li)):
        for j in range(1, len(li)):
            if num == 10:
                break
            if distance(li[i], li[j]) == 0 and i != j:
                print(li[i], li[j])
                lt.append(li[i][7])
                lt.append(li[j][7])
                num += 1
    plt.plot(lt, 'o')
    plt.show()
