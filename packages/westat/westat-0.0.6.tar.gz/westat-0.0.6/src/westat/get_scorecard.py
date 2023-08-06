from westat import pd, np
from westat.get_col_type import get_col_type
from westat.get_data_discrete import get_data_discrete
from westat.get_data_woe_transform import get_data_woe_transform
from westat.get_model_iv import get_model_iv
from westat.get_data_iv import get_data_iv


def get_scorecard(data,
                  col_bins=pd.DataFrame(),
                  col_dict=pd.DataFrame(),
                  init_score=600,
                  pdo=20,
                  target='y',
                  return_lr=False,
                  precision=2,
                  language='en'):
    import statsmodels.api as sm
    # 数据类型
    col_types = get_col_type(data)

    # 数据离散化
    data_discrete = get_data_discrete(data=data, col_bins=col_bins, target=target)

    # WoE 转换
    data_woe = get_data_woe_transform(data_discrete, target=target)

    # 根据手动调整后的分箱，批量计算IV
    data_iv = get_data_iv(data_discrete, target='target', criterion='discrete')

    # 逻辑回归模型
    y = data_woe[target]
    x = data_woe[[col for col in data.columns if col != target]]
    x = sm.add_constant(x)

    lr = sm.Logit(y, x).fit()

    # 开发评分卡
    odds = data[target].sum() / (data[target].count() - data[target].sum())

    b = pdo / np.log(odds)
    a = init_score + b * np.log(odds)

    result = get_model_iv(data_discrete=data_discrete,
                          data_iv=data_iv,
                          col_bins=col_bins,
                          col_dict=col_dict,
                          col_types=col_types,
                          target='target',
                          precision=precision)

    # 评分卡模型的截距项
    result['Intercept'] = lr.params[0]
    result['Label'].fillna('', inplace=True)

    # 评分卡模型的参数
    df_coef = pd.DataFrame(data=lr.params, columns=['Coef'])
    df_coef['Name'] = df_coef.index
    result = result.merge(df_coef, how='left', on='Name')

    # 特征的顺序
    result['Bins No.'] = result['No.']
    result['No.'] = result['Name'].apply(lambda x: list(result['Name'].unique()).index(x) + 1)

    # 评分卡模型的特征得分
    result['Score'] = result['WoE'] * result['Coef'] * b
    result.reset_index(drop=True, inplace=True)

    # 设置显示格式
    result['Intercept'] = result['Intercept'].apply(lambda x: round(x, precision))
    result['Coef'] = result['Coef'].apply(lambda x: round(x, precision))
    result['Score'] = result['Score'].apply(lambda x: round(x, precision))

    # 语言设置
    if language == 'cn':
        result = result[['No.', 'Name', 'Label', 'Type', 'Bins No.', 'Bin', 'Bins', '#Total', '#Bad',
                         '#Good', '%Total', '%Bad', '%Good', '%BadRate', 'WoE', 'IV', 'Total IV',
                         'WoE.', 'Style', 'Intercept', 'Coef', 'Score']]
        result.rename(
            columns={'No.': '序号', 'Name': '名称', 'Label': '描述', 'Type': '类型', 'Bins No.': '分箱序号',
                     'Bin': '分箱', 'Bins': '切分点', '#Total': '#合计', '#Bad': '#坏', '#Good': '好',
                     '%Total': '%合计',
                     '%Bad': '%坏', '%Good': '%好', '%BadRate': '%坏件率', 'Total IV': 'IV合计', 'Intercept': '截距',
                     'Coef': '系数',
                     'Score': '分数', 'Style': '样式'}, inplace=True)
    else:
        result = result[['No.', 'Name', 'Label', 'Type', 'Bins No.', 'Bin', 'Bins', '#Total', '#Bad',
                         '#Good', '%Total', '%Bad', '%Good', '%BadRate', 'WoE', 'IV', 'Total IV',
                         'WoE.', 'Style', 'Intercept', 'Coef', 'Score']]

    if return_lr:
        return result, lr
    else:
        return result
