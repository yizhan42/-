# 4. 练习：统计不同气温的天数直方图
# * 题目描述：统计1-3月气温在-10℃~10℃的天数统计直方图 

# * 题目要求: 
# * 使用NumPy进行直方图统计 
# * 使用Matplotlib进行直返图绘制 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/temp2.csv（数据源与第二节练习相同）
# * temp2.csv，包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
# * 共2列数据，第1列month为月份，第2列temperature为摄氏温度


# * 问题拆解提示：
# 1. 直方图统计需要哪些信息？
# 2. 如何使用NumPy进行直方图统计？
# 3. 如何可视化直方图？
# * 问题解决提示：
# 1. 直方图统计需要3个信息：
# * 需要统计的数据
# * 需要统计的数据范围range，默认为所有数据
# * 分桶的个数bins，默认为10
# 2. 使用NumPy中的histogram()(https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.histogram.html)方法进行直方图统计；
# 3. 使用Matplotlib中的提供的hist()(https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html)方法可视化直方图。

# my answer
import os
import numpy as np
import matplotlib.pyplot as plt

month_list = [1,2,3]

month_arr = []

r_range = (-10,10)
n_bins = 10

output_path = '/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise4-different temperature Histogram/chart/'

if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_and_process_data():
    data_arr = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise4-different temperature Histogram/temp2.csv', delimiter=',', skiprows=1)
    # for month in month_list:
    #     month_bool_arr = data_arr[:, 0] == month
    #     month_temp_arr = data_arr[month_bool_arr][:, 1]
    #     # duration_member_type_arr = np.concatenate([duration_col, member_type_col], axis=1)
    #     month_arr.append(month_temp_arr)
    # Jan_to_March_arr = np.concatenate(month_arr, axis=0)
    # Jan_arr = Jan_to_March_arr[Jan_to_March_arr[0] == 1]
    # Feb_arr = Jan_to_March_arr[Jan_to_March_arr[0] == 2]
    # Mar_arr = Jan_to_March_arr[Jan_to_March_arr[0] == 3]
    Jan_to_March_arr = data_arr[:,1]

    # Jan_to_March_arr = np.concatenate(month_arr, axis=0)
    return Jan_to_March_arr

def analyze_data(Jan_to_March_arr):
    Month_duration_hist, Month_bin_edges = np.histogram(Jan_to_March_arr, range=r_range, bins=n_bins)
    # F_duration_hist, F_bin_edges = np.histogram(Feb_arr, range=r_range, bins=n_bins)
    # M_duration_hist, M_bin_edges = np.histogram(Mar_arr, range=r_range, bins=n_bins)
    # print('January:{}, 直方图分组边界:{}'.format(J_duration_hist, J_bin_edges))
    # print('February：{}, 直方图分组边界:{}'.format(F_duration_hist, F_bin_edges))
    print('Month{}, Hist edges:{}'.format(Month_duration_hist, Month_bin_edges))
    return Month_bin_edges

def show_result(Jan_to_March_arr,Month_bin_edges):
    plt.figure(figsize=(10, 5))
    # ax1 = fig.add_subplot(1, 3, 1)
    # ax2 = fig.add_subplot(1, 3, 2, sharey=ax1)
    # ax3 = fig.add_subplot(1, 3, 3, sharey=ax1)

    # 一月份直方图
    plt.hist(Jan_to_March_arr, range=r_range, bins=n_bins)
    # ax1.set_xticks(range(-10, 10, 2))
    # ax1.set_title('Month')
    # ax1.set_ylabel('Count')

    # # 二月份直方图
    # ax2.hist(Feb_arr, range=r_range, bins=n_bins)
    # ax2.set_xticks(range(-10, 10, 2))
    # ax2.set_title('February')
    # ax2.set_ylabel('Count')

    # # 三月份直方图
    # ax3.hist(Mar_arr, range=r_range, bins=n_bins)
    # ax3.set_xticks(range(-10, 10, 2))
    # ax3.set_title('March')
    # ax3.set_ylabel('Count')

    # plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'temperature_histogram.png'))
    plt.xticks(Month_bin_edges)
    plt.show()



def main():
    Jan_to_March_arr = collect_and_process_data()
    Month_bin_edges  = analyze_data(Jan_to_March_arr)
    show_result(Jan_to_March_arr,Month_bin_edges)
    
if __name__  == '__main__':
    main()


# teacher answer
# -*- coding: utf-8 -*-

# import numpy as np
# import matplotlib.pyplot as plt

# # 读取csv数据文件
# data_arr = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise4-different temperature Histogram/temp2.csv', delimiter=',', skiprows=1)

# # 1. 统计直方图所需信息
# # 气温数据
# temp_arr = data_arr[:, 1]

# # 统计的数据范围范围
# hist_range = (-10, 10)

# # 分桶个数
# n_bins = 5

# # 2. 直方图统计
# stats, bin_edges = np.histogram(temp_arr, range=hist_range, bins=n_bins)
# # print('气温直方图统计信息：{}, 直方图分组边界:{}'.format(stats, bin_edges))
# # print('Temperature Hist Imformation：{}, Hist edge:{}'.format(stats, bin_edges))
# print(stats, bin_edges)

# # 3. 可视化直方图
# plt.figure()
# plt.hist(temp_arr, range=hist_range, bins=n_bins)
# # 设置x轴坐标点显示为分组边界
# plt.xticks(bin_edges)
# plt.show()