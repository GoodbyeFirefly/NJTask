import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.grid(True, linestyle="--", color='gray', linewidth='0.5', axis='both')

# 参考公式为C:\Users\许逍遥\Desktop\南软任务安排 跨链流程_0805
# # M/M/1/N排队论模型
S = 8.27  # μ顾客的平均被服务数 1，2，4，8
N = 60
#
Lq = []
NTem = []
Ls = []
Wq = []
Ws = []


def MM1N():
    for R in np.arange(0.0, 1.0, 0.01):
        load = R / S
        p0 = (1 - load) / (1 - pow(load, N + 1))
        # pn = p0 * pow(load, N)
        LsTem = load / (1 - load) - ((N + 1) * pow(load, N + 1)) / (1 - pow(load, N + 1))
        Ls.append(LsTem)
        Lq.append(LsTem - 1 + p0)
        WsTem = LsTem / (S * (1 - p0))
        Ws.append(WsTem)
        Wq.append(WsTem - 1 / S)


MM1N()

font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12, }

R = np.arange(0.0, 1.0, 0.01)  # λ顾客平均到达率
plt.title('System Ⅰ queue length', font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("System queue length Ls", font)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.grid(True, linestyle="--", color='gray', linewidth='0.5', axis='both')
plt.plot(R, Ls, label='Ls')
plt.legend()
plt.show()

plt.title("System Ⅰ Average queue length", font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("Average queue length Lq", font)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
plt.plot(R, Lq, label = 'Lq')
plt.legend()
plt.show()

plt.title("System Ⅰ Cross-chain requirements for dwell time in the system", font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("Cross-chain requirements for dwell time in the system Ws", font)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
plt.plot(R, Ws, label = 'Ws')
plt.legend()
plt.show()

plt.title("System Ⅰ Cross-chain requirements queue time in the application chain", font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("Cross-chain requirements queue time in the application chain Wq", font)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
plt.plot(R, Wq, label = 'Wq')
plt.legend()
plt.show()
