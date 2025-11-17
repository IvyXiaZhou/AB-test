import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.stats.proportion as sp
from scipy.stats import norm

# 读取数据
data = pd.read_csv('./effect_tb.csv', header=None)
data.columns = ['dt', 'user_id', 'label', 'dmp_id']
data = data.drop(columns='dt')

print(data.head(3))
print(data.describe())
print(data.shape)
print(data.nunique())

# 数据清洗
print(data[data.duplicated(keep=False)].sort_values(by=['user_id']))
data = data.drop_duplicates()
print(data[data.duplicated(keep=False)])
print(data.info())
print(data.isnull().sum())

# 使用 pivot_table 分析
print(data.pivot_table(index='dmp_id', columns='label', values='user_id', aggfunc='count', margins=True))
print(data.dtypes)

# 计算转化率
print('对照组转化率:', data[data['dmp_id'] == 1]['label'].mean())
print(data['dmp_id'].value_counts())

# 保存数据
data.to_csv('./output.csv', index=False)

# 重新读取验证
data = pd.read_csv('./output.csv')
print('对照组：', data[data['dmp_id'] == 1]['label'].mean())
print('营销策略一：', data[data['dmp_id'] == 2]['label'].mean())
print('营销策略二：', data[data['dmp_id'] == 3]['label'].mean())

# 假设检验 
n_old = len(data[data.dmp_id == 1])
n_new = len(data[data.dmp_id == 3])
c_old = len(data[(data.dmp_id == 1) & (data.label == 1)])  
c_new = len(data[(data.dmp_id == 3) & (data.label == 1)])  

r_old = c_old / n_old
r_new = c_new / n_new
r = (c_old + c_new) / (n_old + n_new)
print('总和点击率', r)

z = (r_new - r_old) / np.sqrt(r * (1 - r) * (1 / n_old + 1 / n_new))
print('检验统计量z:', z)

z_alpha = norm.ppf(0.95)
print('临界值:', z_alpha)

# 使用 statsmodels 进行检验 
z_score, p = sp.proportions_ztest([c_new, c_old], [n_new, n_old], alternative='larger')
print('策略二 vs 对照组 - 检验统计量z:', z_score, 'P值:', p)

# 第二个检验 
c_strategy1 = len(data[(data.dmp_id == 2) & (data.label == 1)])
n_strategy1 = len(data[data.dmp_id == 2])

z_score, p = sp.proportions_ztest([c_strategy1, c_old], [n_strategy1, n_old], alternative='larger')
print('策略一 vs 对照组 - 检验统计量z:', z_score, 'P值:', p)
