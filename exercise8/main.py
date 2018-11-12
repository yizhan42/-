# 8. 练习：分析房屋价格数据
# * 题目描述：分析房屋价格数据 
# 1. 通过盒形图可视化不同卧室个数对应的房屋价格的分布 
# 2. 通过双变量图观察卫生间个数与房屋价格的关系 
# 3. 通过热图可视化变量间的关系 

# * 题目要求: 
# * 使用Pandas和Seaborn进行数据分析及可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/house_data.csv 
# * house_data.csv，包含了某美国城市的房屋价格。每行记录为单个房屋的数据。 
# * 共5列数据，分别表示： 
# 1. price: 房屋价格，单位：美元 
# 2. bedrooms: 卧室个数 
# 3. bathrooms: 卫生间个数 
# 4. area: 房屋面积，单位：平方米 
# 5. yr_built：房屋建造的年份


# * 问题拆解提示：
# 1. 如何绘制盒形图？
# 2. 如何绘制双变量图？
# 3. 如何计算相关系数？
# 4. 如何可视化相关系数？
# * 问题解决提示：
# 1. 使用Seaborn模块中的boxplot()(https://seaborn.pydata.org/generated/seaborn.boxplot.html)方法绘制盒形图，主要参数有：
# * x: 横轴变量，这里应为bedrooms
# * y: 纵轴变量，这里应为price
# * data: 数据，通常为DataFrame类型
# 2. 使用Seaborn中的joinplot()(https://seaborn.pydata.org/generated/seaborn.jointplot.html)方法绘制双变量图，主要参数有；
# * x: 变量1，这里应为bathrooms
# * y: 变量2，这里应为price
# * data: 数据，通常为DataFrame类型
# 3. 使用Pandas的corr()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.corr.html)方法计算没两列数据的相关系数，可更改method参数指定计算相关系数的方法，默认为皮尔逊相关系数；
# 4. 使用热图可视化相关系数结果，其中热图可使用Seaborn模块中的heatmap()(https://seaborn.pydata.org/generated/seaborn.heatmap.html)方法绘制,主要参数有：
# * data: 数据，通常为DataFrame类型，这里为相关系数结果
# * annot: 是否在热图中显示数值，默认为False


# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 读取csv数据文件
data_df = pd.read_csv('./house_data.csv')

# 1. 通过盒形图可视化不同卧室个数对应的房屋价格的分布
sns.boxplot(x='bedrooms', y='price', data=data_df)
plt.show()

# 2. 通过双变量图观察卫生间个数与房屋价格的关系
sns.jointplot(x='bathrooms', y='price', data=data_df)
plt.show()

# 3. 通过热图可视化变量间的关系
corr_result = data_df.corr()
sns.heatmap(data=corr_result, annot=True)
plt.show()

