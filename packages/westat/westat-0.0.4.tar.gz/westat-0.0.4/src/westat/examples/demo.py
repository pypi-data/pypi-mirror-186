import numpy as np
from numpy import inf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


from westat.get_woe_iv import get_woe_iv

mpl.rcParams['font.family'] = 'SimHei'  # 设置中文字体
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def plot_woe(data: pd.DataFrame,
                col: str,
                target='y',
                criterion='tree',
                bins=[],
                qcut=0,
                missing=[np.nan, 'nan', '', -99999999, '-99999999', -99999999.0, -99999999.0],
                precision=2,
                language='en'):
    """
    绘制条形图，data数据集中目标变量col的WoE和IV值，可用于检查WoE分布是否满足单调性要求
    Args:
        data: DataFrame,目标数据集
        col: str,需要计算WoE和IV的列名
        target: str,目标变量名称，默认为'y'
        criterion: 分箱方法，默认为决策树分箱
        bins: list,手动指定的分箱列表
        qcut: int,等额分箱的分组数
        missing: list,缺失值列表
        precision: int,数据精度，小数点位数，默认为2
        language: str,数据结果标题列显示语言，默认为 'en',可手动修改为'cn'

    Returns:
        matplotlib条形图结果
    """

    result = get_woe_iv(dataframe=data, col=col, target=target, criterion=criterion, bins=bins, qcut=qcut, missing=missing, precision=precision)

    fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    
    x = [str(x) for x in result['Bin']]
    woe = result['WoE']
    iv = result['IV']


    axs[0].bar(x, woe, align='center',color='darkblue')
    axs[0].set_title('WoE Distributions')
    axs[0].set_xlabel(col)
    axs[0].set_ylabel('WoE')
#     ax1.xaxis.set_ticks_position('bottom')
#     ax1.yaxis.set_ticks_position('left')
#     ax1.set_xticks(rotation=0, fontsize='small')
    
    # 设置数字标签
    for x,w in zip(x,woe):
        if w < 0:
            p = 0.1
        else:
            p = w + 0.1
        axs[0].text(x, p, w, ha='center', va= 'center',fontsize=12)
    

#     # 设置绘图显示语言
#     if language == 'cn':
#         fig.suptitle('WoE/IV 分布', fontsize=14, fontweight='bold')
#     else:
#         fig.suptitle('WoE/IV Distributions', fontsize=14, fontweight='bold')
    
    plt.show()
    
plot_woe_iv(data,'PAY_0',target='target',language='cn',show_iv=True)