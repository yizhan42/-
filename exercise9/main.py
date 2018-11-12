# 9. 练习：统计不同专业的员工平均薪资
# * 题目描述：统计不同专业背景的员工的平均薪资，并用柱状图显示结果 

# * 题目要求: 
# * 使用Pandas进行数据分析及可视化 

# * 数据文件： 
# * 数据源下载地址：https://video.mugglecode.com/data_employee.zip，下载压缩包后解压即可 
# * employee_info.csv，包含了员工的基本信息，共4列数据，分别表示： 
# 1. EmployeeNumber: 员工编号 
# 2. Age: 年龄 
# 3. Department: 所处部门 
# 4. MonthlyIncome: 月收入 

# * employee_edu.csv，包含部分员工的专业背景，共2列数据： 
# * EmployeeNumber: 员工编号 
# * EducationField: 专业背景

# * 问题拆解提示：
# 1. 如何联合两个csv数据文件？
# 2. 如何进行分组统计？
# 3. 如何绘制柱状图？
# * 问题解决提示：
# 1. 使用Pandas模块中的merge()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.merge.html)方法联合有关系的数据，主要参数有：
# * left: 左侧数据集，这里为员工基本信息数据
# * right: 右侧数据集，这里为员工专业背景数据
# * how: 联合的方式，默认为inner
# * on: 两个数据集内可以关联起来的列名，这里为EmployeeNumber
# 2. 使用Pandas中的groupby()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html)方法进行分组统计
# 3. 使用Pandas模块中的plot()(https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html)方法绘制柱状图，注意需要指定参数kind='bar'，因为默认绘制类型为折线图,即kind='line'；

# my answer
import os
import pandas as pd 
import matplotlib as plt 

employee_edu_file = './data_employee/employee_edu.csv'
employee_info_file = './data_employee/employee_info.csv'

employ_merged = pd.merge(employee_edu_file, employee_info_file, on = 'EmployeeNumber')

employ_group = employ_merged.groupby('EducationField')['MonthlyIncome'].mean()

employ_group.plot(kind = 'bar')


# teacher answer
# # -*- coding: utf-8 -*-

# import pandas as pd
# import matplotlib.pyplot as plt


# # 读取csv数据文件
# employee_info_df = pd.read_csv('./employee_info.csv')
# employee_edu_df = pd.read_csv('./employee_edu.csv')

# # 1. 联合两个csv数据文件
# combined_df = pd.merge(left=employee_info_df, right=employee_edu_df, how='inner', on='EmployeeNumber')
# # 将联合的结果进行保存
# combined_df.to_csv('./employee_all_info.csv', index=False)

# # 2. 分组统计不同专业背景的员工平均薪资
# edu_ave_income = combined_df.groupby('EducationField')['MonthlyIncome'].mean()

# # 3. 绘制柱状图
# edu_ave_income.plot(kind='bar')
# plt.tight_layout()
# plt.show()
