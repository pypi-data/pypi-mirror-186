import numpy as np
from numpy import inf
import pandas as pd

from westat.get_tree_bins import get_tree_bins



def get_col_psi(data_actual: pd.DataFrame,
               data_expected: str,
               col:str,
               bin:list,
               qcut=10,    
               missing: list = [np.nan, None, ''],      
               total=False,
               precision=2,
               language='en') -> pd.DataFrame:
    """
    计算数据集PSI
    Args:
        data_actual: DataFrame,实际数据集
        data_expected: DataFrame,预期数据集
        col:str,需要计算PSI的列名
        bin:list，计算PSI的分箱
        qcut: int,等额分箱的分组数
        target: str,目标变量名称，默认为'y'
        total:bool,是否显示汇总信息
        precision:数据精度，小数点位数，默认为2        
        language: str,数据结果标题列显示语言，默认为 'en',可手动修改为'cn'

    Returns:
        结果数据集保存数据集对应的PSI
    """
    if len(bin) > 0:
        data_actual['Bins']=pd.cut(data_actual[col],bin,duplicates='drop')
        data_expected['Bins']=pd.cut(data_actual[col],bin,duplicates='drop')
    else:
        data_actual['Bins'] = data_actual[col].replace(missing,np.nan)
        data_expected['Bins'] = data_expected[col].replace(missing,np.nan)
        
    bins_actual = pd.cut(data_actual['Bins'],qcut=qcut,duplicates='drop',retbins=True)[1]
    bins_actual[0] = -inf
    bins_actual[-1] = inf
    
    data_actual['Bins Range'] = pd.cut(data_actual['Bins'],bins=bins_actual)
    data_expected['Bins Range'] = pd.cut(data_expected['Bins'],bins=bins_actual)
    df_actual = data_actual[['Bins Range']].groupby(by='Bins Range').count()
    df_expected = data_expected[['Bins Range']].groupby(by='Bins Range').count()
    df_expected.index=df_actual.index
    result = pd.concat([df_actual,df_expected],axis=1)
    result.columns = ['#Actual','#Expected']
    result['#Total'] = result['#Actual'] + result['#Expected']
    result['%Actual'] = result['#Actual'] / result['#Actual'].sum()
    result['%Expected'] = result['#Expected'] / result['#Expected'].sum()
    result['%Total'] = result['#Total'] / result['#Total'].sum()
    result['PSI'] = (result['%Actual'] - result['%Expected']) * np.log(result['%Actual'] / result['%Expected'])
    result['Total PSI'] = result['PSI'].fillna(0).sum()
    result['Bins Range'] = result.index
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
        result[['No.','Bins Range','#Total','#Actual','#Expected','%Total','%Actual','%Expected','PSI','Total PSI']]
        result.rename(columns={'No.':'序号','Bins Range':'分组','#Total':'#汇总','#Actual':'#实际','#Expected':'#预期','%Total':'%汇总','%Actual':'%实际','%Expected':'%预期','Total PSI':'PSI 汇总'},inplace=True)
        
    else:
        result[['No.','Bins Range','#Total','#Actual','#Expected','%Total','%Actual','%Expected','PSI','Total PSI']]
     
    return result
