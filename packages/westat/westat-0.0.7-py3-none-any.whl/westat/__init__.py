# 版本号
global version
version = '0.0.7'


def get_version():
    return version


import sys
import os
from datetime import datetime

from tqdm.notebook import tqdm

import numpy as np
from numpy import inf
import pandas as pd

# pd.set_option('display.float_format', lambda x: '%.4f' % x)  # 在dataframe中不以科学计数法显示数值


# import seaborn as sns

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

from sklearn.metrics import roc_curve, auc

from pandas import read_csv, read_excel
# from westat.LogisticScoreCard import *

from westat.logger import logger
from westat.get_data_describe import get_data_describe
from westat.get_data_distribution import get_data_distribution
from westat.get_data_partition import get_data_partition
from westat.get_data_discrete import get_data_discrete
from westat.get_data_iv import get_data_iv
from westat.get_data_woe import get_data_woe
from westat.get_data_woe_transform import get_data_woe_transform
from westat.get_tree_bins import get_tree_bins
from westat.get_woe_iv import get_woe_iv, view_woe_iv

from westat.check_data_target import check_data_target
# from westat.dataframe_to_table import dataframe_to_table
from westat.get_col_type import get_col_type
from westat.get_col_bins import get_col_bins
from westat.get_col_psi import get_col_psi,view_col_psi
from westat.get_modify_bins import get_modify_bins
from westat.feature_selection import get_feature_by_ivcorr

from westat.get_model_iv import get_model_iv
from westat.get_scorecard import get_scorecard
from westat.get_predict_score import get_predict_score
from westat.get_score_distribution import get_score_distribution, view_score_distribution

# 绘图
from westat.plot_woe import plot_woe
from westat.plot_iv import plot_iv
from westat.plot_corr import plot_corr
from westat.plot_lift import plot_lift

# 决策树文件转换
from westat.tree_to_img import tree_to_img
from westat.tree_to_pdf import tree_to_pdf

# 日期处理函数
from westat.date_diff import date_diff

# 设置函数别名
get_data_desc = get_data_describe
get_data_dist = get_data_distribution
get_data_part = get_data_partition
get_score_dist = get_score_distribution
view_score_dist = view_score_distribution



def plot_roc_ks(data, score_card):
    data_score_proba = predict_score_proba(data, score_card)
    false_positive_rate, recall, thresholds = roc_curve(data['y'], data_score_proba['Proba'], drop_intermediate=False)
    roc_auc = auc(false_positive_rate, recall)
    plt.figure(figsize=(20, 10))

    # ROC曲线
    plt.subplot(121)
    plt.title('ROC')
    plt.plot(false_positive_rate, recall, 'b', label='AUC = %0.4f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.xlabel('false_positive_rate')
    plt.ylabel('recall')

    # KS曲线
    plt.subplot(122)
    pre = sorted(data_score_proba['Proba'], reverse=True)
    num = [(i) * int(len(pre) / 10) for i in range(10)]
    num = num + [(len(pre) - 1)]
    ks_thresholds = [max(thresholds[thresholds <= pre[i]]) for i in num]
    data_ks = pd.DataFrame([false_positive_rate, recall, thresholds]).T
    data_ks.columns = ['fpr', 'tpr', 'thresholds']
    data_ks = pd.merge(data_ks, pd.DataFrame(ks_thresholds, columns=['thresholds']), on='thresholds', how='inner')
    ks = max(recall - false_positive_rate)
    plt.title('KS')
    plt.plot(np.array(range(len(num))), data_ks['tpr'])
    plt.plot(np.array(range(len(num))), data_ks['fpr'])
    plt.plot(np.array(range(len(num))), data_ks['tpr'] - data_ks['fpr'], label='K-S = %0.4f' % ks)
    plt.legend(loc='lower right')
    plt.xlim([0, 10])
    plt.ylim([0.0, 1.0])
    plt.xlabel('label')
    plt.show()


class Table(pd.DataFrame):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'table for westat'
