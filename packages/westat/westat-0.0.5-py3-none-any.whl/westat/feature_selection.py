import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
from westat.logger import logger
from westat.get_woe_iv import get_woe_iv
from westat.get_data_iv import get_data_iv

def get_feature_by_ivcorr(data: pd.DataFrame,    
                          col_iv: pd.DataFrame = pd.DataFrame(),                   
                          min_iv: float = 0.02,
                          max_corr: float = 0.6,
                          keep: list = [],
                          drop: list = [],
                          target: str = 'target',
                          return_drop: bool = False):
    """
    根据最小IV值 和 最大相关性 筛选特征
    Args:
        data:DataFrame,将要筛选特征的数据集
        col_iv:DataFrame,列的IV汇总，包含Name,IV 两列的数据集
        min_iv:筛选后允许的最小IV值
        max_corr:筛选后允许的最大相关性
        keep:list,需要保留的特征
        drop:list,需要删除的特征
        target:str,目标变量名称，默认为'y'
        return_drop:是否返回已删除的特征

    Returns:
        默认返回筛选后的特征名单，
        当return_drop为True时，同时返回筛选后的特征名单、删除的特征名单、相关性和IV数据表
    """
    if col_iv.empty:
        col_iv = get_data_iv(data, target=target)

    # 根据每一列的IV值，计算相关矩阵
    col_iv_filter = col_iv[col_iv['IV'] >= min_iv]
    data_corr = data[col_iv_filter['Name']].corr()

    col_iv_result = []
    for i in range(len(col_iv_filter)):
        for j in range(len(col_iv_filter)):
            col1 = col_iv_filter.iloc[i, 0]
            iv1 = col_iv_filter.iloc[i, 1]
            col2 = col_iv_filter.iloc[j, 0]
            iv2 = col_iv_filter.iloc[j, 1]
            col_iv_result.append([col1, col2, iv1, iv2, iv1 - iv2])

    result = pd.DataFrame(col_iv_result, columns=['Name1', 'Name2', 'IV1', 'IV2', 'IV1-IV2'])
    result['Corr'] = data_corr.values.reshape(-1, 1)
    result = result[result['Name1'] != result['Name2']]

    col_delete_iv_corr = result['Name1'][(result['IV1'] <= min_iv) | (
            (result['Corr'] > max_corr) & (result['IV1-IV2'] < 0))].unique()

    col_result = [col for col in result['Name1'].unique() if col not in col_delete_iv_corr and col not in drop]
    col_keep = sorted(list(set(col_result + keep)))
    col_drop = sorted(list(set(list(col_delete_iv_corr) + drop)))

    # 是否返回已删除特征
    if return_drop:
        return col_keep, col_drop, result
    else:
        return col_keep
