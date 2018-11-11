# 7. 练习：使用堆叠柱状图比较不同来源的 PM2.5数值差异
# * 题目描述： 
# 1. 添加一列diff用于比较中国环保部和美国使馆检测的PM2.5值的差异（两列数据的绝对值差） 
# 2. 找出差别最大的10天的记录 
# 3. 使用分组柱状图比较中国环保部和美国使馆检测的每年平均PM2.5的值 

# * 题目要求: 
# * 使用Pandas进行数据分析及可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/Beijing_PM.csv （数据源与上节课相同） 
# * Beijing_PM.csv，包含了2013-2015年北京每小时的PM2.5值。每行记录为1小时的数据。 
# * 共7列数据，分别表示： 
# 1. year: 年，2013-2015 
# 2. month: 月，1-12 
# 3. day: 日，1-31 
# 4. hour: 小时，0-23 
# 5. season：季度，1-4 
# 6. PM_China: 中国环保部检测的PM2.5值 
# 7. PM_US: 美国使馆检测的PM2.5值


# 提示
# * 问题拆解提示：
# 1. 如何处理空值记录？
# 2. 如何为数据添加列？
# 3. 如何对列数据进行绝对值操作？
# 4. 如何对数据进行排序并选取Top n？
# 5. 如何绘制分组柱状图？
# * 问题解决提示：
# 1. 使用Pandas模块中的drop_na()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html)方法清除记录中的空值。要注意inplace参数的使用方法，如果在原始数据上进行操作，需使用inplace=True；如果需要将结果赋值给一个新的变量，需使用inplace=False，其默认值为False；
# 2. Pandas中列的添加，可直接使用[]内包含新的列名，并赋值新的数据；
# 3. 使用Pandas中的abs()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.abs.html)方法；
# 4. 使用Pandas的sort_values()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html)方法对数据进行排序，常用的参数有2个：
# * by，指定排序的列
# * ascending，默认为升序，如果是降序，需要设定为False
# Top n操作可以使用head()方法返回排序后的前n个记录
# 5. 使用Pandas模块中的plot()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)方法支持分组柱状图的绘制，只需要传递多列数据。



# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


# 读取csv数据文件
data_df = pd.read_csv('./Beijing_PM.csv')

# 1. 处理空值记录
data_df.dropna(inplace=True)

# 2. 为数据添加列
data_df['diff'] = data_df['PM_China'] - data_df['PM_US']

# 3. 进行绝对值操作
data_df['diff'] = data_df['diff'].abs()

# 4. 数据排序
top_10_diff = data_df.sort_values(by='diff', ascending=False).head(10)
print('相差最大的10条记录：')
print(top_10_diff)

# 5. 绘制分组柱状图
year_average_pm = data_df.groupby('year')[['PM_China', 'PM_US']].mean()
year_average_pm.plot(kind='bar')
plt.tight_layout()
plt.show()