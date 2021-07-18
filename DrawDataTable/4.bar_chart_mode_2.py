# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.6.0
# @auth : elviscttian
# @func : 本代码为利用 Matplotlib 库 画直方图
# ------------------------------------

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # 字体属性设置
 
font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # 使用本地字体(Windows操作系统)
 
interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 3, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]
 
# 画布大小
plt.figure(figsize=[12,8], dpi=80)
 
plt.bar(range(len(quantity)), quantity, width=1)
 
# 设置x轴刻度
_x = [i for i in range(len(interval))]
_xtick_labels = interval + [150]
plt.xticks(_x, _xtick_labels)  # x轴刻度
 
plt.show()