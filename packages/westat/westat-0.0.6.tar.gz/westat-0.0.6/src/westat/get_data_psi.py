import numpy as np
from numpy import inf
import pandas as pd

from westat.get_tree_bins import get_tree_bins



def get_data_psi(data_actual: pd.DataFrame,
               data_expected: str,
               qcut=10,      
               total=False,
               precision=2,
               language='en') -> pd.DataFrame:
    """
    计算数据集PSI
    Args:
        data_actual: DataFrame,实际数据集
        data_expected: DataFrame,预期数据集
        qcut: int,等额分箱的分组数
        target: str,目标变量名称，默认为'y'
        total:bool,是否显示汇总信息
        precision:数据精度，小数点位数，默认为2        
        language: str,数据结果标题列显示语言，默认为 'en',可手动修改为'cn'

    Returns:
        结果数据集保存数据集对应的PSI
    """
    bins_actual = pd.cut(data_actual['Score'],qcut=qcut,duplicates='drop',retbins=True)[1]
    bins_actual[0] = -inf
    bins_actual[-1] = inf
    
    data_actual['Score Range'] = pd.cut(data_actual['Score'],bins=bins_actual)
    data_expected['Score Range'] = pd.cut(data_expected['Score'],bins=bins_actual)
    df_actual = data_actual[['Score Range']].groupby(by='Score Range').count()
    df_expected = data_expected[['Score Range']].groupby(by='Score Range').count()
    df_expected.index=df_actual.index
    result = pd.concat([df_actual,df_expected],axis=1)
    result.columns = ['#Actual','#Expected']
    result['#Total'] = result['#Actual'] + result['#Expected']
    result['%Actual'] = result['#Actual'] / result['#Actual'].sum()
    result['%Expected'] = result['#Expected'] / result['#Expected'].sum()
    result['%Total'] = result['#Total'] / result['#Total'].sum()
    result['PSI'] = (result['%Actual'] - result['%Expected']) * np.log(result['%Actual'] / result['%Expected'])
    result['Total PSI'] = result['PSI'].fillna(0).sum()
    result['Score Range'] = result.index
    result.reset_index(drop=True,inplace=True)
    result['No.'] = result.index
    

    # 设置显示格式
    result['No.'] = result['No.'] + 1
    result['#Total'] = result['#Total'].apply(lambda x: round(x, precision))
    result['#Actual'] = result['#Actual'].apply(lambda x: round(x, precision))
    result['#Expected'] = result['#Expected'].apply(lambda x: round(x, precision))
    result['%Total'] = result['%Total'].apply(lambda x: format(x, '.' + str(precision) + '%'))
    result['%Actual'] = result['%Actual'].apply(lambda x: format(x, '.' + str(precision) + '%'))
    result['%Expected'] = result['%Expected'].apply(lambda x: format(x, '.' + str(precision) + '%'))
    result['#PSI'] = result['#PSI'].apply(lambda x: round(x, precision))
    result['#Total PSI'] = result['#Total PSI'].apply(lambda x: round(x, precision))

    if language == 'cn':
        result[['No.','Score Range','#Total','#Actual','#Expected','%Total','%Actual','%Expected','PSI','Total PSI']]
        result.rename(columns={'No.':'序号','Score Range':'分数区间','#Total':'#汇总','#Actual':'#实际','#Expected':'#预期','%Total':'%汇总','%Actual':'%实际','%Expected':'%预期','Total PSI':'PSI 汇总'},inplace=True)
        
    else:
        result[['No.','Score Range','#Total','#Actual','#Expected','%Total','%Actual','%Expected','PSI','Total PSI']]
     
    return result
