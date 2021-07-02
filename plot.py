import numpy as np
import pylab as mpl
import matplotlib.pyplot as plt


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False


x_label = ['0-1000', '1000-2000', '2000-3000', '3000-4000',
           '4000-5000', '5000-6000', '6000-7000', '7000-8000',
           '8000-9000', '>=9000', ]
x = np.array([_ for _ in range(len(x_label))])
y1 = [1500, 629, 709, 931, 1038, 1211, 986, 747, 589, 1463]
y2 = [1494, 666, 719, 907, 1007, 1150, 992, 746, 595, 1557]
# y3 = [0.7583, 0.7938, 0.7756]


width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(x-width/2, y1, width, label='训练集')
rects2 = ax.bar(x+width/2, y2, width, label='测试集')
# rects3 = ax.bar(x+width/2, y3, width/2, label='electra-180g-base')
# rects4 = ax.bar(x+width/2, y4, width/4, label='xlnet-base')

ax.set_ylim(0, 2000)
ax.set_xlabel('文本长度范围')
ax.set_ylabel('文本数量')
ax.set_xticks(x)
ax.set_xticklabels(x_label)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
ax.legend()
ax.bar_label(rects1)
ax.bar_label(rects2)
# ax.bar_label(rects3)
#ax.bar_label(rects4)
plt.show()