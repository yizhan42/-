# 3. 练习：使用饼状图可视化不同气温的天数占比
# * 题目描述：将1-3个月份的气温数据进行合并，并使用饼状图可视化所有数据的零上气温和零下气温的天数占比情况。 

# * 题目要求: 
# * 使用NumPy进行数组合并 
# * 使用Matplotlib进行可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/data_temp.zip，下载压缩包后解压即可 
# * 201801_temp.csv、201802_temp.csv、201803_temp.csv分别包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
# * 每个文件中只包含一列气温数据：temperature为摄氏温度



# * 问题拆解提示：
# 1. 如何使用NumPy读取csv数据文件？
# 2. 如何使用NumPy进行数组合并？
# 3. 如何构造布尔型数组并进行过滤？
# 4. 如何进行饼状图可视化占比？
# * 问题解决提示：
# 1. 利用NumPy模块中的loadtxt()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)方法读取csv数据文件，
# 需要指定2个参数的值
# * delimiter=','：csv文件的数据分隔符，默认为空格；
# * skiprows=1：跳过第一行（表头），默认为0，表示数据包含第一行；
# * 可以不指定dtype参数。由于csv中的数据全部可以转换为float类型，所以dtype使用默认的float即可；
# 2. 使用NumPy模块中的concatenate()(https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.concatenate.html)方法进行数组合并，
# 其中参数为包含多个数组的序列。
# 3. 使用一列数据和0做比较，构造布尔型数组；将布尔型数组放在向量的索引操作中；
# 4. 使用Matplotlib提供的pie()(https://matplotlib.org/api/_as_gen/matplotlib.pyplot.pie.html)进行饼状图可视化。


# my answer
import os
import numpy as np 
import matplotlib.pyplot as plt


data_path = '/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise3-show percentage of different weather/data_temp/'
data_files = ['201801_temp.csv', '201802_temp.csv', '201803_temp.csv']


# 结果保存路径
output_path = '/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise3-show percentage of different weather/output'
if not os.path.exists(output_path):
    os.makedirs(output_path)


def collect_and_process_data():
    data_arr_list = []
    for data_file in data_files:
        datafilename = os.path.join(data_path, data_file)
        data_arr = np.loadtxt(datafilename, delimiter=',', skiprows=1)
        data_arr_list.append(data_arr)

    combined_data_arr = np.concatenate(data_arr_list)
    # print(combined_data_arr.shape)
    return combined_data_arr

def analyze_data(combined_data_arr):
    # n_year = n_year.reshape(-1,1)
    # n_overzero = combined_data_arr[combined_data_arr >= 0].shape[0]
    # n_belowzero = combined_data_arr[combined_data_arr < 0].shape[0]
    # print(combined_data_arr[combined_data_arr >= 0])
    n_positive_days = combined_data_arr[combined_data_arr >= 0].shape[0]

    # 获取零下气温的天数
    n_negative_days = combined_data_arr[combined_data_arr < 0].shape[0]
    n_all = [n_positive_days, n_negative_days]
    return n_all


def save_and_show_results(n_all):
    plt.figure()
    plt.pie(n_all, labels=['>=0', '<0'], autopct='%.2f%%', shadow=True, explode=(0.05, 0))
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, './piechart.png'))
    plt.show()



def main():
    """
        主函数
    """
    combined_data_arr = collect_and_process_data()

    n_all = analyze_data(combined_data_arr)

    save_and_show_results(n_all)


if __name__ == '__main__':
    main()


# teacher answer
# -*- coding: utf-8 -*-

# import numpy as np
# import matplotlib.pyplot as plt

# # 1. 读取csv数据文件
# data_arr1 = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise3-show percentage of different weather/data_temp/201801_temp.csv', delimiter=',', skiprows=1)
# data_arr2 = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise3-show percentage of different weather/data_temp/201802_temp.csv', delimiter=',', skiprows=1)
# data_arr3 = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise3-show percentage of different weather/data_temp/201803_temp.csv', delimiter=',', skiprows=1)

# # 2. 数组合并
# combined_data_arr = np.concatenate([data_arr1, data_arr2, data_arr3])

# # 3. 使用布尔型数组数据过滤
# # 获取零上气温的天数
# # shape返回行数和列数，第0个元素是行数，即记录个数
# n_positive_days = combined_data_arr[combined_data_arr >= 0].shape[0]
# print(combined_data_arr[combined_data_arr >= 0])

# # 获取零下气温的天数
# n_negative_days = combined_data_arr[combined_data_arr < 0].shape[0]

# # n_overzero = combined_data_arr[combined_data_arr >= 0].shape[0]
# # n_belowzero = combined_data_arr[combined_data_arr < 0].shape[0]

# n_days = [n_positive_days, n_negative_days]

# # 4. 进行饼状图可视化占比
# plt.figure()
# plt.pie(n_days, labels=['>=0', '<0'], autopct='%.2f%%')
# plt.axis('equal')
# plt.tight_layout()
# plt.show()