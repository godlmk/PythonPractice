import numpy as np
import random as rand
import matplotlib.pyplot as plt


def main():
    # Variables
    n = 40  # 粒子个数
    num_variables = 2  # 变量个数
    # Crear allegros
    a = np.empty((num_variables, n))  # 位置信息
    v = np.empty((num_variables, n))  # 速度信息
    Pbest = np.empty((num_variables, n))  # 局部最优
    Gbest = np.empty((1, 2))  # 全局最优
    r = np.empty((n))
    # Llenar arreglos
    for i in range(0, num_variables):  # 2*40的矩阵
        for j in range(0, n):
            Pbest[i][j] = rand.randint(-20, 20)
            a[i][j] = Pbest[i][j]
            v[i][j] = 0
    # Llenar r
    for i in range(0, n):  # 每个粒子的适应度值
        r[i] = fitness(a[0][i], a[1][i])
    # Ordenar elementos de Pbest
    Ordenamiento_Burbuja(Pbest, r, n)
    Gbest[0][0] = Pbest[0][0]
    Gbest[0][1] = Pbest[1][0]
    generation = 0
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)

    while generation < 300:  # generation迭代次数最大值为1000
        for i in range(n):  # 粒子群的粒子个数40
            # 当前粒子与局部粒子比较，通过适应度函数计算
            if fitness(a[0][i], a[1][i]) < fitness(Pbest[0][i], Pbest[1][i]):
                Pbest[0][i] = a[0][i]
                Pbest[1][i] = a[1][i]
            # 当前位置与全局最优粒子比较，通过适应度函数计算
            if fitness(Pbest[0][i], Pbest[1][i]) < fitness(Gbest[0][0], Gbest[0][1]):
                Gbest[0][0] = Pbest[0][i]
                Gbest[0][1] = Pbest[1][i]
            # 从新计算每个粒子的速度和位置
            Vector_Velocidad(n, a, Pbest, Gbest, v)
        generation = generation + 1
        print('Generacion: ' + str(generation) + ' - - - Gbest: ' + str(Gbest))
        line1 = ax.plot(a[0], a[1], 'r+')
        line2 = ax.plot(Gbest[0][0], Gbest[0][1], 'g*')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        fig.canvas.draw()
        ax.clear()
        ax.grid(True)
    print('Gbest: ')
    print(Gbest)


def Vector_Velocidad(n, a, Pbest, Gbest, v):
    """
    计算每个粒子的位置、速度
    :param n: 粒子的个数
    :param a:
    :param Pbest:个体极值
    :param Gbest:全局极值
    :param v:每个粒子的速度
    :return:
    """
    for i in range(n):
        # Velocidad en X
        v[0][i] = 0.7 * v[0][i] + (Pbest[0][i] - a[0][i]) * rand.random() * 1.47 + (
                Gbest[0][0] - a[0][i]) * rand.random() * 1.47
        a[0][i] = a[0][i] + v[0][i]
        # Velocidad en Y
        v[1][i] = 0.7 * v[1][i] + (Pbest[1][i] - a[1][i]) * rand.random() * 1.47 + (
                Gbest[0][1] - a[1][i]) * rand.random() * 1.47
        a[1][i] = a[1][i] + v[1][i]


def fitness(x, y):
    """
    适应度函数  f(x,y)=100 * ((y - (x ** 2)) ** 2) + ((1 - (x ** 2)) ** 2)
    :param x:
    :param y:
    :return:
    """
    return 100 * ((y - (x ** 2)) ** 2) + ((1 - (x ** 2)) ** 2)
    # 100 * ((y - (x**2))**2) + ((1 - (x**2))**2)


def Ordenamiento_Burbuja(Pbest, r, n):
    # Ordenamiento burbuja
    for i in range(1, n):
        for j in range(0, n - 1):
            if r[j] > r[j + 1]:
                # Ordenar el fitness
                tempRes = r[j]
                r[j] = r[j + 1]
                r[j + 1] = tempRes

                # Ordenar las X, Y
                tempX = Pbest[0][j]
                Pbest[0][j] = Pbest[0][j + 1]
                Pbest[0][j + 1] = tempX

                tempY = Pbest[1][j]
                Pbest[1][j] = Pbest[1][j + 1]
                Pbest[1][j + 1] = tempY


if '__main__' == main():
    main()
