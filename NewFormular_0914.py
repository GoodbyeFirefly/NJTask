import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')

miu = 8.27
miu_ = 3.08
Lq = []
W = []
Ls = []
Wq = []
Ws = []

def MM1N():
    for lanmuda in np.arange(0.0, 5.00, 0.01):
        a = (((lanmuda + miu) * miu_ + miu_ * miu_) - miu_ * (pow(miu_ * miu_ + 2 * miu_ * (lanmuda + miu) + pow(lanmuda - miu, 2), 0.5))) / (2 * miu_ * miu_)
        tem = a / (1 - a)
        Ls.append(tem)
        Lq.append(tem * a)
        Wq.append(tem / miu_)
        Ws.append(tem / miu_ / a)

MM1N()

font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12, }

# R = np.arange(0.0, 5.0, 0.01)       # λ顾客平均到达率
# plt.title("平均队长")
# plt.xlabel("请求到达率λ")
# plt.ylabel("平均队长Lq")
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams["axes.unicode_minus"]=False   # 正常显示负号
# plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
# plt.plot(R, Lq, label = 'Lq')
# plt.legend()
# plt.show()

# 论文终稿figure10
R = np.arange(0.0, 5.00, 0.01)  # λ顾客平均到达率
plt.title('System Ⅱ queue length', font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("System queue length Ls", font)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams["axes.unicode_minus"]=False   # 正常显示负号
plt.grid(True, linestyle="--", color='gray', linewidth='0.5', axis='both')
plt.plot(R, Ls, label='Ls')
plt.legend()
plt.show()

# plt.title("System Ⅱ Average queue length", font)
# plt.xlabel("Request arrival rate λ", font)
# plt.ylabel("Average queue length Lq", font)
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
# plt.plot(R, Lq, label = 'Lq')
# plt.legend()
# plt.show()

# plt.title("System Ⅱ Cross-chain requirements for dwell time in the system", font)
# plt.xlabel("Request arrival rate λ", font)
# plt.ylabel("Cross-chain requirements for dwell time in the system Ws", font)
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
# plt.plot(R, Ws, label = 'Ws')
# plt.legend()
# plt.show()

# plt.title("System Ⅱ Cross-chain requirements queue time in the application chain", font)
# plt.xlabel("Request arrival rate λ", font)
# plt.ylabel("Cross-chain requirements queue time in the application chain Wq", font)
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
# plt.plot(R, Wq, label = 'Wq')
# plt.legend()
# plt.show()

# plt.title("平均支持时间")
# plt.xlabel("请求到达率λ")
# plt.ylabel("平均支持时间W")
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams["axes.unicode_minus"]=False   # 正常显示负号
# plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
# plt.plot(R, W, label = 'W')
# plt.legend()
# plt.show()

# lanmuda = 2
# a = (((lanmuda + miu) * miu_ + miu_ * miu_) - (
#     pow(miu_ * miu_ + 2 * miu_ * (lanmuda + miu) + pow(lanmuda - miu, 2), 0.5))) / (2 * miu_ * miu_)
# print(a)