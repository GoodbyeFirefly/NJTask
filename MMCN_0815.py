import torch
import numpy as np
import math
from torch.autograd import Variable
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from sympy import plot_implicit

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')

# # M/M/C/N排队论模型
R = np.array(range(0, 50, 1))       # λ顾客平均到达率
S = 1 / 3.96             # μ顾客的平均被服务数 1，2，4，8
c = 100   # 中继链数目 1,2,3,4,5,6
load = R / (c * S)                        # ρ系统到达负荷
N = 50000
#
Lq = []
Lq_small = []
Lq_big = []
Ls = []
Wq = []
Ws = []
# sumTem = 0
# for n in range(0, c):
#     sumTem += pow(c * load, n) / math.factorial(n)
# p0 = 1 / (sumTem + pow(c * load, c) * (1 - pow(load, N - c + 1)) / math.factorial(c) / (1 - load))
# pN = pow(c, c) * pow(load, N) * p0 / math.factorial(c)
# tem = p0 * load * pow(c * load, c) / math.factorial(c) / pow(1 - load, 2)
# LqTem = tem * (1 - pow(load, N - c) - (N - c) * pow(load, N - c) * (1 - load))
# Lq.append(LqTem)

#
#
def MMCN():
    for i in np.arange(0.0, 50.0, 0.1):
        load = i / (c * S)
        sumTem = 0
        for n in range(0, c):
            sumTem += pow(i / S, n) / math.factorial(n)

        if (load < 1):
            p0 = 1 / (sumTem + pow(i / S, c) / math.factorial(c) / (1 - load))
            # pN = pow(c, c) * pow(load, N) * p0 / math.factorial(c)
            # tem = p0 * load * pow(c * load, c) / math.factorial(c) / pow(1 - load, 2)
            LqTem = pow(i / S, c + 1) * p0 / (c * math.factorial(c)) / pow(1 - load, 2)
            Lq_small.append(LqTem)
            # Lq_big.append(0)
            # Ls.append(LqTem + c * load * (1 - pN))
            # WqTem = LqTem / (i * (1 - pN))
            # Wq.append(WqTem)
            # Ws.append(WqTem + 1 / S)
        # elif (load > 1):
        #     p0 = 1 / (sumTem + pow(i / S, c) / math.factorial(c) / (1 - load))
        #     pN = pow(c, c) * pow(load, N) * p0 / math.factorial(c)
        #     tem = p0 * load * pow(c * load, c) / math.factorial(c) / pow(1 - load, 2)
        #     LqTem = tem * (1 - pow(load, N - c) - (N - c) * pow(load, N - c) * (1 - load))
        #     # Lq_small.append(0)
        #     Lq_big.append(LqTem)
            # Ls.append(0)
            # Wq.append(0)
            # Ws.append(0)

MMCN()

R1 = np.arange(0, 100 / 3.96, 0.1)       # λ顾客平均到达率
plt.title("平均队列长度")
plt.xlabel("请求到达率λ")
plt.ylabel("平均队列长度Lq")
plt.plot(R1, Lq_small, label = 'ρ < 1')
# R2 = np.arange(100 / 4.24 + 0.1, 430.0, 0.1)       # λ顾客平均到达率
# plt.plot(R2, Lq_big, label = 'ρ > 1')
# plt.legend()
plt.show()


#
# for c in range(1, 7):
#     plt.figure('中继链数目c = ' + str(c))
#     Lq = []
#     S = 1
#     MMCN()
#     plt.plot(R, Lq, label='μ=1')
#
#     Lq = []
#     S = 2
#     MMCN()
#     plt.plot(R, Lq, label='μ=2')
#
#     Lq = []
#     S = 3
#     MMCN()
#     plt.plot(R, Lq, label='μ=3')
#
#     Lq = []
#     S = 4
#     MMCN()
#     plt.plot(R, Lq, label='μ=4')
#
#     Lq = []
#     S = 5
#     MMCN()
#     plt.plot(R, Lq, label='μ=5')
#
#     Lq = []
#     S = 6
#     MMCN()
#     plt.plot(R, Lq, label='μ=6')
#
#     plt.title("平均队列长度")
#     plt.legend()
#     plt.xlabel("请求到达率λ")
#     plt.ylabel("平均队列长度Lq")
#
# plt.title("平均队列长度")
# plt.legend()
# plt.xlabel("请求到达率λ")
# plt.ylabel("平均队列长度Lq")
#
# plt.show()











# 测试一：
# x = np.array([1, 2, 3], dtype=int)
# y = pow(x, 2)
# print(y)
# 测试二
# x = np.array([1, 2, 3], dtype=int)
# y = x / 2
# print(y)
# 测试三 画隐函数函数
# exc = lambda exper: plot_implicit(parse_expr(exper))
# exc('x**2+(y-x**(2/3))**2-1')