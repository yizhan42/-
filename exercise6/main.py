# 6. 练习：使用柱状图可视化 PM2.5数值
# * 题目要求: 
# * 使用Pandas查看数据文件的基本信息 
# * 使用Pandas进行数据分析及可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/Beijing_PM.csv 
# * Beijing_PM.csv，包含了2013-2015年北京每小时的PM2.5值。每行记录为1小时的数据。 
# * 共7列数据，分别表示： 
# 1. year: 年，2013-2015 
# 2. month: 月，1-12 
# 3. day: 日，1-31 
# 4. hour: 小时，0-23 
# 5. season：季度，1-4 
# 6. PM_China: 中国环保部检测的PM2.5值 
# 7. PM_US: 美国使馆检测的PM2.5值


# * 问题拆解提示：
# 1. 如何使用Pandas读取csv数据文件？
# 2. 如何使用Pandas查看数据文件的基本信息？
# 3. 如何按照year列进行分组统计？
# 4. 如何使用Pandas保存结果？
# 5. 如何使用Pandas绘制柱状图？
# * 问题解决提示：
# 1. 使用Pandas模块中的read_csv()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html)方法读取csv数据文件；
# 2. 在Pandas模块中，有3个常用的方法可用于数据基本信息的查看：
# * head()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.head.html)数据预览
# * info()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html)数据文件的基本信息
# * describe()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html)数据内容的统计信息
# 3. 使用Pandas的groupby()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)方法进行分组统计；
# 4. 使用Pandas模块中的to_csv()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html)方法保存结果到csv文件；
# 5. 使用Pandas模块中的plot()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)方法绘制柱状图，注意需要指定参数kind='bar'，因为默认绘制类型为折线图,即kind='line'；


# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


# 1. 读取csv数据文件
data_df = pd.read_csv('./Beijing_PM.csv')

# 2. 查看数据文件的基本信息
print('数据预览：')
print(data_df.head())

print('数据文件的基本信息：')
print(data_df.info())

print('数据内容的统计信息：')
print(data_df.describe())

# 4. 按照year列进行分组统计
year_average_pm = data_df.groupby('year')['PM_China'].mean()

# 4. 结果保存
year_average_pm.to_csv('./year_average_pm.csv')

# 5. 绘制柱状图
year_average_pm.plot(kind='bar')
plt.tight_layout()
plt.show()
