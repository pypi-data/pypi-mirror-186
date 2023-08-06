# 版本号
global version 
version = '0.0.6'

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

import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_curve, auc

mpl.rcParams['font.family'] = 'SimHei'  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

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
from westat.plot_woe import plot_woe
from westat.plot_iv import plot_iv

from westat.check_data_target import check_data_target
# from westat.dataframe_to_table import dataframe_to_table
from westat.get_col_type import get_col_type
from westat.get_col_bins import get_col_bins
from westat.get_modify_bins import get_modify_bins
from westat.feature_selection import get_feature_by_ivcorr

from westat.get_model_iv import get_model_iv
from westat.get_scorecard import get_scorecard

# 决策树文件转换
from westat.tree_to_img import tree_to_img
from westat.tree_to_pdf import tree_to_pdf

# 日期处理函数
from westat.date_diff import date_diff

# 设置函数别名
get_data_desc = get_data_describe
get_data_dist = get_data_distribution
get_data_part = get_data_partition




# 按切分点划分数据，得到全部的离散数据
def get_cut_result(data,
                   bins,
                   missing=[np.nan, 'nan', '', -99999999, '-99999999', -99999999.0, -99999999.0]):
    logger.info('根据cut离散化连续变量进行中。。。')
    cols = [i for i in data.columns if i not in [i[0] for i in bins]]
    data_cut_result = data[cols].copy()
    for i in tqdm(range(len(bins))):
        col = bins.iloc[i, 0]
        cut_points = bins.iloc[i, 1]
        data_cut_result[col] = pd.cut(data[col], cut_points).astype('str')

    # 缺失值替换
    data_cut_result.replace(missing, ['missing'] * len(missing), inplace=True)
    data_cut_result.fillna('missing', inplace=True)
    logging.info('根据cut离散化连续变量完成！')
    return data_cut_result


# 按变量，离散化数据
def get_col_cut_result(data, col, bins):
    col_cut_result = pd.cut(data[col], bins).astype('str')

    # 缺失值替换
    col_cut_result.replace(['nan', '', -99999999, '-99999999', -99999999.0],
                           ['missing', 'missing', 'missing', 'missing', 'missing'], inplace=True)
    col_cut_result.fillna('missing', inplace=True)
    return col_cut_result


def predict_score_proba(data, score_card, clf=False, X=False, delta_score=20, init_score=600):
    logging.info('预测用户分数中。。。')
    b = -delta_score / np.log(2)
    a = init_score - score_card['Intercept'][0] * b
    col_result = score_card['Name'].unique().tolist() + ['y']
    col_continuous_cut_points = score_card[['Name', 'Bins']][score_card['Type'] == 'continuous'].drop_duplicates('Name')
    data_discrete = get_cut_result(data[col_result], col_continuous_cut_points)
    data_score_proba = pd.DataFrame()
    for col in score_card['Name'].unique():
        col_score = col + '_score'
        cut_points = score_card['Bin'][score_card['Name'] == col].tolist()
        score = score_card['Score'][score_card['Name'] == col].tolist()
        data_score_proba[col_score] = data_discrete[col].replace(cut_points, score)
    data_score_proba['y'] = data_discrete['y']
    data_score_proba['Score'] = data_score_proba.sum(axis=1) + score_card['Intercept'][0] * b + a
    if clf:
        data_score_proba['Proba'] = clf.predict_proba(X)[:, 1]
    else:
        data_score_proba['Proba'] = 1 - 1 / (1 + np.e ** ((data_score_proba['Score'] - a) / b))
    return data_score_proba


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


def get_score_dist(data, score_card, qcut=10, precision=2, language='en'):
    result_score = predict_score_proba(data, score_card)

    if qcut:
        result_score['Score'] = pd.qcut(result_score['Score'], qcut)

    result = result_score.groupby('Score')['y'].agg([('#Bad', lambda y: (y == 1).sum()),
                                                     ('#Good', lambda y: (y == 0).sum()),
                                                     ('#Total', 'count')]).reset_index()
    result['%Bad'] = result['#Bad'] / result['#Bad'].sum()
    result['%Good'] = result['#Good'] / result['#Good'].sum()
    result['%Total'] = result['#Total'] / result['#Total'].sum()
    result['%BadRate'] = result['#Bad'] / result['#Total']

    result['#CumBad'] = result['#Bad'].cumsum()
    result['#CumGood'] = result['#Good'].cumsum()
    result['#CumTotal'] = result['#Total'].cumsum()
    result['%CumBad'] = result['#CumBad'] / result['#Bad'].sum()
    result['%CumGood'] = result['#CumGood'] / result['#Good'].sum()
    result['LIFT'] = (result['#Bad'] / result['#Total']) / (result['#Bad'].sum() / result['#Total'].sum())

    precision_str = '.' + str(precision)
    result['%Total'] = result['%Total'].apply(lambda x: format(x, precision_str + '%'))
    result['%Bad'] = result['%Bad'].apply(lambda x: format(x, precision_str + '%'))
    result['%Good'] = result['%Good'].apply(lambda x: format(x, precision_str + '%'))
    result['%BadRate'] = result['%BadRate'].apply(lambda x: format(x, precision_str + '%'))
    result['%CumBad'] = result['%CumBad'].apply(lambda x: format(x, precision_str + '%'))
    result['%CumGood'] = result['%CumGood'].apply(lambda x: format(x, precision_str + '%'))
    result['LIFT'] = result['LIFT'].apply(lambda x: round(x, precision))
    result['NO.'] = result.index + 1

    result = result[
        ['NO.', 'Score', '#Total', '#Bad', '#Good', '%Total', '%Bad', '%Good', '%BadRate', '%CumBad', 'LIFT']]

    return result


def view_score_dist(data, score_card, qcut=10, precision=2):
    result = get_score_dist(data=data, score_card=score_card, qcut=qcut, precision=precision)
    result['LIFT.'] = result['LIFT']
    result = result.style.bar(subset=['LIFT.'], color='#007bff')
    return result


class Table(pd.DataFrame):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'table for westat'
