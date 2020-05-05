# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.6.0
# @auth : elviscttian
# @func : 本代码为利用 Matplotlib 库 画柱状图
# ------------------------------------
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # 字体属性设置

font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # 使用本地字体(Windows操作系统)

names = ["猩球崛起3:终极之战", "敦刻尔克", "蜘蛛侠英雄归来", "战狼2"]
b_16 = [15746, 312, 4497, 319]
b_15 = [12357, 156, 2045, 168]
b_14 = [2358, 399, 2358, 362]

bar_width = 0.15  # 单个柱状图的宽度

# x_14 = list(range(len(names)))
# x_15 = [i+bar_width for i in x_14]
# x_16 = [i+bar_width*2 for i in x_14]
day_01 = np.arange(len(names))
day_02 = day_01 + bar_width
day_03 = day_01 + bar_width * 2
print(bar_width * 2)
print(day_01)
print(day_02)
print(day_03)

plt.figure(figsize=[20, 15], dpi=80)  # 设置图形大小
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)  # 设置图像位置

plt.bar(day_01, b_14, width=bar_width, label="9月14日")
plt.bar(day_02, b_15, width=bar_width, label="9月14日")
plt.bar(day_03, b_16, width=bar_width, label="9月14日")

# 设置图例
plt.legend(prop=font, loc='upper right')

# 设置x轴的刻度
plt.xticks(range(len(names)), names, fontproperties='SimHei', size=16, rotation=0)
plt.title('电影票房多日统计对比', fontproperties='SimHei', size=20, rotation=0)

plt.savefig('./票房对比.jpg')
plt.pause(1)  # 显示图像 3s 后自动关闭
# plt.show()  # 展示图像