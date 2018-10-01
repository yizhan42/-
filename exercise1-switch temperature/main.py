# 题目描述：创建一个批量温度转换器，使其将摄氏温度批量地转换为华氏温度。
# 公式为: f = 1.8 *c + 32，其中 c 为摄氏温度，f为华氏温度。 

# 题目要求：使用NumPy中向量化的方法，不能使用循环操作 

# 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/temp.csv 
# * temp.csv 中包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。 
# * 共2列数据，第1列 month为月份，第2列 temperature 为摄氏温度，其中摄氏温度包含了单位 C

# * 问题拆解提示：
# 1. 如何使用 NumPy 读取csv数据文件？
# 2. 如何获取 temperature列的记录？
# 3. 由于气温数据的每条记录包含了单位，如 -6 C，表示零下6摄氏度。如何批量化替换字符串中的特殊字符？
# 4. 如何更改 NumPy 中数组的数据类型？
# 5. 如何实现公式进行批量化操作？
# * 问题解决提示：
# 1. 利用 NumPy 模块中的 loadtxt()(https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)方法读取 csv 数据文件，需要指定3个参数的值
# * delimiter=','：csv文件的数据分隔符，默认为空格；
# * dtype='str'：csv文件中的数据类型，默认为float；
# * skiprows=1：跳过第一行（表头），默认为0，表示数据包含第一行；
# 2. 利用 NumPy 的切片操作获取单列数据；
# 3. 利用 NumPy 模块中的 core.defchararray.replace()(https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.core.defchararray.replace.html)
# 4. 利用 NumPy 模块中的 astype() (https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.astype.html)方法；
# 5. 向量化操作时，将向量看作是普通的变量即可。在实现公式时，和普通操作没有区别

# -*- coding: utf-8 -*-

import numpy as np

# 1. 读取csv数据文件
data_arr = np.loadtxt('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise1/temp.csv', delimiter=',', dtype='str', skiprows=1)

# 2. 获取temperature列的记录，即所有行的第1列数据
c_temp_str_col = data_arr[:, 1]

# 3. 批量化替换字符串中的特殊字符
cln_c_temp_str_col = np.core.defchararray.replace(c_temp_str_col,  ' C', '')

# 4. 类型转换
c_temp_col = cln_c_temp_str_col.astype('float')

# 5. 实现公式进行批量化操作
f_temp_col = 1.8 * c_temp_col + 32

# print('摄氏温度数据：')
print(c_temp_col)

# print('转换后的华氏温度数据：')
print(f_temp_col)