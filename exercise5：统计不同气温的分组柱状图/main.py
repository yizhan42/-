# 5. 练习：统计不同气温的分组柱状图
# * 题目描述：绘制1-3月的每月零上气温和零下气温天数的分组柱状图 

# * 题目要求: 
# * 使用Matplotlib进行分组柱状图的绘制 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/temp2.csv（数据源与第二节练习相同）
# * temp2.csv，包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
# * 共2列数据，第1列month为月份，第2列temperature为摄氏温度 

# * 问题拆解提示：
# 1. 如何过滤得到每月的气温数据？
# 2. 如何获取每月零上气温和零下气温的天数？
# 3. 如何绘制分组柱状图？
# * 问题解决提示：
# 1. 使用month列（数据的第0列）对比月份得到布尔型数组，然后使用布尔型数组过滤数据并获取每月的气温数据；
# 2. 使用temperature列（数据的第1列）对比0得到布尔型数组，然后使用布尔型数组过滤数据并获取零上、零下气温的天数；
# 3. 使用Matplotlib中的bar()进行柱状图绘制。由于是分组柱状图，需要考虑当绘制多组柱状图时，需要添加一定的“偏移量”从而保证多组柱状图之间不会重叠或遮挡。


# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 读取csv数据文件
data_arr = np.loadtxt('./temp2.csv', delimiter=',', skiprows=1)

month_list = [1, 2, 3]

# 初始化零上、零下气温的天数
n_positive_days_list = []
n_negative_days_list = []

for month in month_list:
    # 1. 根据月份过滤获取每月气温数据
    month_arr = data_arr[:, 0] == month
    month_temp_arr = data_arr[month_arr][:, 1]

    # 2. 对比0获得零上、零下气温天数
    n_positive_days = month_temp_arr[month_temp_arr >= 0].shape[0]
    n_negative_days = month_temp_arr[month_temp_arr < 0].shape[0]

    # 添加到列表中
    n_positive_days_list.append(n_positive_days)
    n_negative_days_list.append(n_negative_days)

# 3. 分组柱状图绘制
# 每组柱子的位置，3个月的数据
bar_locs = np.arange(3)
# 坐标轴标签
xtick_labels = np.arange(1, 4)
# 柱子宽度
bar_width = 0.35

plt.figure()
# 第一组柱状图
plt.bar(bar_locs, n_positive_days_list, width=bar_width, color='g', alpha=0.7, label='>=0')
# 第二组柱状图，注意添加了“偏移量”，即bar_width
plt.bar(bar_locs + bar_width, n_negative_days_list, width=bar_width, color='r', alpha=0.7, label='<0')
plt.xticks(bar_locs + bar_width / 2, xtick_labels)
plt.legend(loc='best')
plt.show()

