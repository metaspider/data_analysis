# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.x
# @auth : elviscttian
# @func : 本代码为利用 Matplotlib 库 画正余弦函数
# ------------------------------------

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # 字体属性设置

font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # 使用本地字体(Windows操作系统)

x = np.arange(100) / 10
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=[20, 8], dpi=80)  # 图像大小
plt.title('正弦/余弦函数图像', fontproperties="SimHei", size=20)  # 标题
plt.xlabel('x 轴', fontproperties="SimHei", size=16)  # x轴设置
plt.ylabel('y 轴', fontproperties="SimHei", rotation=90, size=16)  # y轴设置
plt.xticks(x[::10], x[::10])  # x轴刻度设置
plt.grid(alpha=0.5)  # 添加网格 , 并设置网格透明度

plt.plot(x, y1, label="sin函数", color="red", linestyle=None, linewidth=3, alpha=0.7)
plt.plot(x, y2, label="cos函数", color="cyan", linestyle='--')

plt.legend(prop=font, fontsize=18, loc='upper left')  # 添加图例 , 即显示plt.plot的label

plt.savefig('./正余弦函数图像')  # 保存图像
plt.pause(1)  # 显示图像 3s 后自动关闭
# plt.show()  # 展示图像
