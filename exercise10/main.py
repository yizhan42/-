# 10. 练习：滚动统计PM2.5指标的3日/5日/7日均值
# * 题目描述：滚动统计PM2.5指标的3日均值、5日均值、7日均值，并对结果进行可视化 

# * 题目要求: 
# * 使用Pandas进行数据分析及可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/pm1.csv 
# * pm1.csv，包含了2013-2015年某地区每小时的PM2.5值。每行记录为1小时的数据。 
# * 共2列数据，分别表示： 
# 1. Timestamp: 年月日及小时 
# 2. PM: PM2.5值

# * 问题拆解提示：
# 1. 操作时序数据有哪些需要注意的？
# 2. 如何对数据按天进行重采样？
# 3. 如何对数据进行滚动统计？
# * 问题解决提示：
# 1. 操作时序数据需要注意以下几点：
# * 需要对时间日期列通过Pandas的to_datetime()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html)进行类型转换；
# * 需要将时间日期列通过set_index()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.set_index.html)设为索引；
# 1. 使用Pandas模块中的resample()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.resample.html)方法进行重采样，
# 这里的基础频率应为'D'，即按天重采样；
# 2. 使用Pandas模块中的rolling()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html)方法进行滚动统计，
# 参数window为滚动窗口的大小，这里应为3, 5, 7

# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


# 读取csv数据文件
data_df = pd.read_csv('/Users/zhanyi/Job hunting/MuggleCode/DataAnalysis/exercise10/pm1.csv')

# 1. 操作时序数据准备工作
# 类型转换
data_df['Timestamp'] = pd.to_datetime(data_df['Timestamp'])
# 索引设置
data_df.set_index('Timestamp', inplace=True)

# 2. 按天进行重采样
# 取小时均值作为按天的统计值
resampled_df = data_df.resample('D').mean()

# 3. 对数据进行滚动统计
resampled_df['MA 5'] = resampled_df['PM'].rolling(window=3).mean()
resampled_df['MA 3'] = resampled_df['PM'].rolling(window=5).mean()
resampled_df['MA 7'] = resampled_df['PM'].rolling(window=7).mean()

# 保存结果
resampled_df.to_csv('./day_stats.csv')

# 结果可视化
resampled_df.plot()
plt.tight_layout()
plt.show()