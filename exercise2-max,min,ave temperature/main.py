# 2. 练习：统计每月气温的最大值、最小值及平均值
# 题目描述：按月份统计每月气温的最大值、最小值及平均值。 

# 题目要求:使用NumPy中布尔型数组进行数据过滤 

# 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/temp2.csv。temp2.csv 中包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
# * 共2列数据，第1列month为月份，第2列temperature为摄氏温度

# * 问题拆解提示：
# 1. 如何使用NumPy读取csv数据文件？
# 2. 如何构造布尔型数组？
# 3. 如何使用布尔型数组进行数据过滤？
# 4. 如何统计最大值、最小值及平均值？
# * 问题解决提示：
# 1. 利用NumPy模块中的loadtxt()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)方法读取csv数据文件，
# 需要指定2个参数的值
# * delimiter=','：csv文件的数据分隔符，默认为空格；
# * skiprows=1：跳过第一行（表头），默认为0，表示数据包含第一行；
# * 可以不指定dtype参数。由于csv中的数据全部可以转换为float类型，所以dtype使用默认的float即可；
# 2. 使用一列数据和月份值做比较，构造布尔型数组
# 3. 将布尔型数组放在向量的索引操作中；
# 4. 直接使用NumPy提供的max()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.max.html)、
# min()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.minimum.html)
# 及mean()(https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.mean.html)可以获取一组数据的最大值、最小值及平均值。


# my answer
import os
import numpy as np 
import matplotlib.pyplot as plt

# def collect_process_data():
#     Jan = []
#     Feb = []
#     Mar = []
#     datafilename = '/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise2-max,min,ave temperature/temp2.csv'
#     data_arr = np.loadtxt(datafilename, delimiter=',', skiprows=1)
#     # print(data_arr[0])
#     for idx in range(data_arr.shape[0]):
#         if data_arr[idx][0] == 1:
#             Jan.append(data_arr[idx][1])
#         if data_arr[idx][0] == 2:
#             Feb.append(data_arr[idx][1])
#         if data_arr[idx][0] == 3:
#             Mar.append(data_arr[idx][1])
   
#     JanMax = np.max(Jan)
#     JanMin = np.min(Jan)
#     JanMean = np.mean(Jan)

#     FebMax = np.max(Feb)
#     FebMin = np.min(Feb)
#     FebMean = np.mean(Feb)

#     MarMax = np.max(Mar)
#     MarMin = np.min(Mar)
#     MarMean = np.mean(Mar)

#     print(JanMax, JanMin, JanMean)
#     print("***")
#     print(FebMax, FebMin, FebMean)
#     print("***")
#     print(MarMax, MarMin, MarMean)
#     print("***")


# if __name__ == '__main__':
#     collect_process_data()



# teacher answer
# -*- coding: utf-8 -*-

import numpy as np

# 1. 读取csv数据文件
data_arr = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise2-max,min,ave temperature/temp2.csv', delimiter=',', skiprows=1)

month_list = [1, 2, 3]
for month in month_list:
    # 2. 构造布尔型数组
    # data_arr[:, 0]表示月份列
    month_bool_arr = data_arr[:, 0] == month
    print(month_bool_arr)

    # 3. 使用布尔型数组进行数据过滤
    month_temp_arr = data_arr[month_bool_arr][:, 1]

    # 4. 统计最大值、最小值及平均值
    month_max_temp = np.max(month_temp_arr)
    month_min_temp = np.min(month_temp_arr)
    month_ave_temp = np.mean(month_temp_arr)

    # 输出统计结果
    # :.2f表示保留小数点后2位输出
    # print('第{}月，气温最大值={:.2f}，最小值={:.2f}，平均值={:.2f}'.format(month,month_max_temp, month_min_temp, month_ave_temp))
    print('the {} month, max temperature = {:.2f}, min temperature = {:2f}, average temperature = {:2f} '.format(month,
    month_max_temp, month_min_temp, month_ave_temp))

# result
# 1 -3.0 -12.0 -7.129032258064516
# 2 0.0 -10.0 -5.642857142857143
# 3 11.0 -4.0 2.3225806451612905