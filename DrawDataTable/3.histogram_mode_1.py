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

names = ['哪吒之魔童降世', '流浪地球', '复仇者联盟4：终局之战', '我和我的祖国', '疯狂的外星人', '中国机长', '飞驰人生', '烈火英雄', '速度与激情：特别行动', '蜘蛛侠：英雄远征', '扫毒2天地对决', '大黄蜂', '惊奇队长', '比悲伤更悲伤的故事', '哥斯拉2：怪兽之王', '阿丽塔：战斗天使', '攀登者', '银河补习班', '狮子王', '反贪风暴4 ']  # 单位(亿)
box_office = [49.26, 46.18, 42.05, 23.36, 21.83, 21.23, 17.03, 16.74, 14.18, 14.01, 12.85, 11.38, 10.25, 9.46, 9.27, 8.88, 8.64, 8.63, 8.23, 7.88]

plt.figure(figsize=[20, 8], dpi=80)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.4)  # 设置图像位置
plt.bar(names, box_office, width=0.3, color='green')
plt.xlabel("影视名称", fontproperties='SimHei', size=16)
plt.ylabel("总票房(单位:亿)", fontproperties='SimHei', rotation=90, size=16)
plt.title("2019电影票房排行榜", fontproperties='SimHei', size=18)
plt.xticks(names, fontproperties='SimHei', rotation=90, size=16)

plt.savefig('./2019电影票行排行.jpg')
plt.pause(1)  # 显示图像 3s 后自动关闭
# plt.show()  # 展示图像