from westat import pd
from westat import tqdm
from westat.get_woe_iv import get_woe_iv


def get_model_iv(data_discrete,
                 data_iv,
                 col_bins,
                 col_dict,
                 col_types,
                 target='y',
                 precision=2,
                 language='en'):
    result = pd.DataFrame()
    for col in tqdm(data_discrete.columns):
        if col != target and data_iv['IV'][data_iv['Name'] == col].values[0] != 0:
            df_woe = get_woe_iv(data=data_discrete, col=col, criterion='discrete', target=target, precision=precision)
            result = pd.concat([result, df_woe])

    # 如果数据字典不为空，则填充字段说明，否则字段说明为空
    if col_dict.empty:
        result_1 = result
        result_1['Label'] = ''
    else:
        result_1 = result.merge(col_dict, on='Name', how='left')
        result_1['Label'] = result_1.iloc[:, -1]

        # 合并数据类型
    result_2 = result_1.merge(col_types, on='Name', how='left')

    # 合并数据分箱
    result = result_2.merge(col_bins, on='Name', how='left')
    result.sort_values(by=['Total IV', 'Name', 'No.'], ascending=[False, True, True], inplace=True)
    result.reset_index(drop=True, inplace=True)

    result['WoE.'] = result['WoE']
    result['Style'] = result['Name'].apply(lambda x: list(result['Name'].unique()).index(x) % 2)

    # 语言设置
    if language == 'cn':
        result = result[['Name', 'Label', 'Type', 'No.', 'Bin', 'Bins', '#Total', '#Bad', '#Good', '%Total', '%Bad',
                         '%Good', '%BadRate', 'WoE', 'IV', 'Total IV', 'WoE.', 'Style']]
        result.rename(
            columns={'Name': '名称', 'Label': '描述', 'Type': '类型', 'No.': '分箱序号', 'Bin': '分箱', 'Bins': '切分点',
                     '#Total': '#合计', '#Bad': '#坏', '#Good': '好', '%Total': '%合计', '%Bad': '%坏', '%Good': '%好',
                     '%BadRate': '%坏件率', 'Total IV': 'IV合计', 'Style': '样式'}, inplace=True)
    else:
        result = result[['Name', 'Label', 'Type', 'No.', 'Bin', 'Bins', '#Total', '#Bad', '#Good', '%Total', '%Bad',
                         '%Good', '%BadRate', 'WoE', 'IV', 'Total IV', 'WoE.', 'Style']]
    return result
