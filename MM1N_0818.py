import torch
import numpy as np
import math
from torch.autograd import Variable
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from sympy import plot_implicit

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')

# # M/M/1/N排队论模型
S = 33.4             # μ顾客的平均被服务数 1，2，4，8
N = 937
#
Lq = []
NTem = []
Ls = []
Wq = []
Ws = []

def MM1N():
    for R in np.arange(0.01, 6.0, 0.02):
        # N = R - 2
        load = R / S
        p0 = (1 - load) / (1 - pow(load, N + 1))
        # pn = p0 * pow(load, N)
        LsTem = load / (1 - load) - (N + 1) * pow(load, N + 1) / (1 - pow(load, N + 1))
        Ls.append(LsTem)
        # NTem.append(N)

MM1N()

R = np.arange(0.01, 6.0, 0.02)       # λ顾客平均到达率
plt.title("系统队列长度")
plt.xlabel("请求到达率λ")
plt.ylabel("系统队列长度Ls")
plt.plot(R, Ls, label = 'Ls')
# plt.plot(R, NTem, label='N')
plt.legend()
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