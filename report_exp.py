from WindPy import w
import pandas as pd
import datetime

def up_or_down(num):
    if num < 0:
        return '下跌📉'
    else:
        return '上涨📈'

def report_export(date=datetime.datetime.now()):
    data_ = w.wsd("000001.SH,881001.WI", "pct_chg", date.strftime("%Y-%m-%d"), date.strftime("%Y-%m-%d"), "").Data[0]
    if None in data_:
        print('Warning: 报告存在缺失数据，请检查现在数据是否已经公布!')
    data_ = [round(i, 2) if i is not None else 0 for i in data_]
    # data_ = [1.2, -1.3]
    data_1 = pd.read_excel(f'./output/{date.strftime("%Y-%m-%d")}.xlsx',sheet_name='每日',index_col=0).round(2)
    data_2 = pd.read_excel(f'./output/{date.strftime("%Y-%m-%d")}.xlsx',sheet_name='同业',index_col=0).round(2)
    text_block_1 = f"""📍【市场指数表现】📍
上证指数{up_or_down(data_[0])}：{abs(data_[0])}%
万得全A{up_or_down(data_[1])}：{abs(data_[1])}%
    """
    text_block_2 = f"""🌼平安睿享文娱-黄维（002450）
本日{up_or_down(data_1['当期复权单位净值增长率']['002450.OF'])}：{abs(data_1['当期复权单位净值增长率']['002450.OF'])}%
近一月{up_or_down(data_1['复权单位净值增长率(截止日1月前)']['002450.OF'])}：{abs(data_1['复权单位净值增长率(截止日1月前)']['002450.OF'])}%
    """
    text_block_3 = f"""🌼平安策略先锋-神爱前（700003）
今日{up_or_down(data_1['当期复权单位净值增长率']['700003.OF'])}：{abs(data_1['当期复权单位净值增长率']['700003.OF'])}%
近一年{up_or_down(data_1['复权单位净值增长率(截止日1年前)']['700003.OF'])}：{abs(data_1['复权单位净值增长率(截止日1年前)']['700003.OF'])}%
    """
    text_block_4 = f"""🌼平安转型创新-神爱前（004390）
今日{up_or_down(data_1['当期复权单位净值增长率']['004390.OF'])}：{abs(data_1['当期复权单位净值增长率']['004390.OF'])}%
近一年{up_or_down(data_1['复权单位净值增长率(截止日1年前)']['004390.OF'])}：{abs(data_1['复权单位净值增长率(截止日1年前)']['004390.OF'])}%
    """
    text_block_5 = f"""🌼平安惠澜纯债A（007935）
今日{up_or_down(data_1['当期复权单位净值增长率']['007935.OF'])}：{abs(data_1['当期复权单位净值增长率']['007935.OF'])}%
近一年{up_or_down(data_1['复权单位净值增长率(截止日1年前)']['007935.OF'])}：{abs(data_1['复权单位净值增长率(截止日1年前)']['007935.OF'])}%
    """
    text_block_6 = f"""🌼平安低碳经济-何杰（009878）
今日{up_or_down(data_1['当期复权单位净值增长率']['009878.OF'])}：{abs(data_1['当期复权单位净值增长率']['009878.OF'])}%
近一月{up_or_down(data_1['复权单位净值增长率(截止日1月前)']['009878.OF'])}：{abs(data_1['复权单位净值增长率(截止日1月前)']['009878.OF'])}%
    """
    text_block_7 = f"""🌼平安同业存单（015645）
本日{up_or_down(data_2['当期复权单位净值增长率'][0])}：{abs(data_2['当期复权单位净值增长率'][0])}%
近七天年化{up_or_down(data_2['近1周回报'][0])}：{abs(data_2['近1周回报'][0])}%
"""
    text_block_8 = f"""🌼平安品质优选-神爱前（014460）
本日{up_or_down(data_1['当期复权单位净值增长率']['014460.OF'])}：{abs(data_1['当期复权单位净值增长率']['014460.OF'])}%
近一月{up_or_down(data_1['复权单位净值增长率(截止日1月前)']['014460.OF'])}：{abs(data_1['复权单位净值增长率(截止日1月前)']['014460.OF'])}%
"""
    data = f"""🏅 净值播报{date.strftime('%m.%d')}

{text_block_1}
{text_block_2}
{text_block_3}
{text_block_4}
{text_block_5}
{text_block_6}
{text_block_7}
{text_block_8}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—广发证券

{text_block_1}
📍【持营池产品】📍
权益可坚持定投
{text_block_2}
{text_block_7}
📍【纯债推荐】📍
{text_block_5}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—中金财富

{text_block_1}
📍【持营池产品】📍
{text_block_8}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—粤开证券

{text_block_1}
📍【持营池产品】📍
{text_block_3}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—国海证券

{text_block_1}
📍【持营池产品】📍
{text_block_4}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—万联证券

{text_block_1}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—招商证券

{text_block_1}
📍【核心公募产品】📍
{text_block_4}
{text_block_7}
📍【持营池产品】📍
{text_block_5}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—国信证券

{text_block_1}
📍【持营池产品】📍
{text_block_6}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—国盛证券

{text_block_1}
📍【持营池产品】📍
{text_block_4}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—长城证券

{text_block_1}
📍【货币+】
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]



🏅 净值播报{date.strftime('%m.%d')}—安信证券
{text_block_1}
📍【持营精选池】📍
货币+
{text_block_7}
平安基金与您携手同行
祝晚安[月亮]
    """
    with open(f'./output/净报{date.strftime("%Y-%m-%d")}.txt', 'w', encoding='utf-8') as f:
        f.write(data)