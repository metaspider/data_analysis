# -*- encoding: utf-8 -*-
# ------------------------------------
# @env : python 3.6.0
# @auth : elviscttian
# @func : 本代码为利用 Matplotlib 库 画直方图
# ------------------------------------

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties  # 字体属性设置
 
font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=14)  # 使用本地字体(Windows操作系统)
 
# 从网络上抓取的250个电影的影视时间长度列表
movie_time = [131, 98, 125, 131, 124, 139, 131, 117, 128, 108, 135, 138, 131, 102, 107, 114, 119, 128, 121, 142, 127, 130, 124,
     101, 110, 116, 117, 110, 128, 128, 115, 99, 136, 126, 134, 95, 138, 117, 111, 78, 132, 124, 113, 150, 110, 117, 86,
     95, 144, 105, 126, 130, 126, 130, 126, 116, 123, 106, 112, 138, 123, 86, 101, 99, 136, 123, 117, 119, 105, 137,
     123, 128, 125, 104, 109, 134, 125, 127, 105, 120, 107, 129, 116, 108, 132, 103, 136, 118, 102, 120, 114, 105, 115,
     132, 145, 119, 121, 112, 139, 125, 138, 109, 132, 134, 156, 106, 117, 127, 144, 139, 139, 119, 140, 83, 110, 102,
     123, 107, 143, 115, 136, 118, 139, 123, 112, 118, 125, 109, 119, 133, 112, 114, 122, 109, 106, 123, 116, 131, 127,
     115, 118, 112, 135, 115, 146, 137, 116, 103, 144, 83, 123, 111, 110, 111, 100, 154, 136, 100, 118, 119, 133, 134,
     106, 129, 126, 110, 111, 109, 141, 120, 117, 106, 149, 122, 122, 110, 118, 127, 121, 114, 125, 126, 114, 140, 103,
     130, 141, 117, 106, 114, 121, 114, 133, 137, 92, 121, 112, 146, 97, 137, 105, 98, 117, 112, 81, 97, 139, 113, 134,
     106, 144, 110, 137, 137, 111, 104, 117, 100, 111, 101, 110, 105, 129, 137, 112, 120, 113, 133, 112, 83, 94, 146,
     133, 101, 131, 116, 111, 84, 137, 115, 122, 106, 144, 109, 123, 116, 111, 111, 133, 150]
 
# 计算组数
group_distance = 10  # 组距
num_bins = (max(movie_time)-min(movie_time))//group_distance + 1  # 组数
print(num_bins)
 
plt.figure(figsize=[12, 8], dpi=80)  # 设置图像大小
 
plt.hist(movie_time, num_bins, rwidth=1)  # 绘制直方图
 
plt.xticks(range(min(movie_time), max(movie_time) + group_distance, group_distance), rotation=90)  # 设置x轴刻度
plt.title('影视时间长度分布直方图', fontproperties='SimHei', size=18)  # 直方图标题
plt.xlabel('影视播放时间(单位:分钟)', fontproperties='SimHei', size=16)  # x轴标签
plt.ylabel('影视个数(单位:个)', fontproperties='SimHei', size=16, rotation=90)  # y轴标签
plt.grid()  # 绘制网格
 
plt.savefig('./影视时间直方图')
plt.show()