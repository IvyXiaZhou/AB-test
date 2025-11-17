# AB-test
# 营销效果分析项目
## 项目描述
本项目用于分析不同营销策略对用户行为的影响，通过统计检验比较各策略组的转化率差异。
## **数据来源**
本数据集来自阿里云天池，详细数据情况请查看原文档链接：  
[阿里云天池 - Audience Expansion Dataset](https://tianchi.aliyun.com/dataset/dataDetail?dataId=50893&lang=zh-cn)
该数据集包含三张表，分别记录了支付宝两组营销策略的活动情况：
* emb_tb_2.csv: 用户特征数据集
* effect_tb.csv: 广告点击情况数据集
* seed_cand_tb.csv: 用户类型数据集
## 数据说明
- `dt`: 日期
- `user_id`: 用户ID
- `label`: 用户行为标签（0/1）
- `dmp_id`: 实验组别（1:对照组, 2:策略一, 3:策略二）

## Marketing Effect Analysis Project
## Project Description
This project is designed to analyze the impact of different marketing strategies on user behavior, comparing the conversion rate differences among various strategy groups through statistical tests.
## **Data Source**
The dataset is from Alibaba Cloud Tianchi. For detailed data information, please refer to the original document link:
[AliyunTianchi - Audience Expansion Dataset](https://tianchi.aliyun.com/dataset/dataDetail?dataId=50893&lang=zh-cn)
This dataset includes three tables that record the activity of two Alipay marketing strategies respectively:
emb_tb_2.csv: User feature dataset
effect_tb.csv: Ad click status dataset
seed_cand_tb.csv: User type dataset
## Data Explanation
dt: Date
user_id: User ID
label: User behavior label (0/1)
dmp_id: Experimental group (1: Control group, 2: Strategy 1, 3: Strategy 2)
