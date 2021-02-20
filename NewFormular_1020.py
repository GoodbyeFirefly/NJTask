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
    for lanmuda in np.arange(0.0, 4.80, 0.01):
        a = (((lanmuda + miu) * miu_ + miu_ * miu_) - miu_ * (pow(miu_ * miu_ + 2 * miu_ * (lanmuda + miu) + pow(lanmuda - miu, 2), 0.5))) / (2 * miu_ * miu_)
        tem = a / (1 - a)
        Ls.append(tem)
        Lq.append(tem * a)
        Wq.append(tem / miu_)
        Ws.append(tem / miu_ / a)

MM1N()

font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12, }

# 论文终稿figure11a figure11b
R = np.arange(0.0, 4.80, 0.01)  # λ顾客平均到达率
plt.title('System Ⅱ: Ls and Lq of Cross-chain requirements', font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("System queue length Ls, Average queue length Lq", font)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.grid(True, linestyle="--", color='gray', linewidth='0.5', axis='both')
plt.plot(R, Ls, label='Ls')
plt.plot(R, Lq, ls = '--', label = 'Lq')
plt.legend()
plt.show()

plt.title("System Ⅱ: Ws and Wq of Cross-chain transactions", font)
plt.xlabel("Request arrival rate λ", font)
plt.ylabel("Response time in system Ws, transactions queue time Wq", font)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.grid(True,linestyle = "--",color = 'gray' ,linewidth = '0.5',axis='both')
plt.plot(R, Ws, label = 'Ws')
plt.plot(R, Wq, ls = '--', label = 'Wq')
plt.legend()
plt.show()