import matplotlib.pyplot as plt
import numpy as np
# matplotlib.rcParams['font.family'] = 'STSong'
# matplotlib.rcParams['font.size'] = 20
# a = np.arange(0.0, 5.0, 0.02)
# plt.plot(a, np.cos(2*np.pi*a), 'r--')
# plt.ylabel("振幅", fontproperties='SimHei', fontsize=20, color="green")
# plt.xlabel("时间", fontproperties='SimHei', fontsize=20)
# plt.title(r'正弦波实例$y=cos(2\pi x)$', fontproperties='SimHei', fontsize=35)
# plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
a = np.arange(100).reshape(5, 20)
np.savetxt('D:/PythonProject\Practice\第0门成绩.csv', a,fmt='%d', delimiter=',')
# # plt.text(2, 1, r'$\mu=100$', fontsize=15)
# plt.axis([-1, 6, -2, 2])
# plt.grid(True)
# plt.subplot(211)
# plt.plot(a, a*1.5, 'go-', a, a*2.5, 'rx', a, a*3.5, 'b^:', a, a*4.5, 'b-.')
# plt.subplot(212)
# plt.plot(a, a*1.5, 'go-', a, a*2.5, 'x', a, a*3.5, 'b^:', a, a*4.5, 'b-.')


'''饼图'''
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1ff%%',
#         shadow=False, startangle=90)
# plt.axis('equal')


'''直方图'''
# np.random.seed(0)
# mu, sigma = 100, 20
# a = np.random.normal(mu, sigma, size=100)
# print(a)
# plt.hist(a, 20, density=False, histtype='stepfilled', facecolor='b', alpha=0.75)
# plt.title('Histogram')
# a = np.arange(24).reshape((2, 3, 4))
# print(a)
# b = np.sqrt(a)
# print(b)
# print(np.maximum(a, b))
# print(a > b)


'''散点图'''
# fig, ax = plt.subplots()
# ax.plot(10*np.random.randn(100), 10*np.random.randn(100), 'o')
# ax.set_title('Simple Scatter')

# plt.show()

