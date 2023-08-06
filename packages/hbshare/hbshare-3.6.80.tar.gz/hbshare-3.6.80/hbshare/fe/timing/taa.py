# -*- coding: utf-8 -*-

from hbshare.fe.xwq.analysis.orm.fedb import FEDB
from hbshare.fe.xwq.analysis.orm.hbdb import HBDB
from datetime import datetime
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['kaiti']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
line_color_list = ['#F04950', '#6268A2', '#959595', '#333335', '#EE703F', '#7E4A9B', '#8A662C',
                  '#44488E', '#BA67E9', '#3FAEEE']
bar_color_list = ['#C94649', '#EEB2B4', '#E1777A', '#D57C56', '#E39A79', '#DB8A66', '#E5B88C',
                  '#8588B7', '#B4B6D1', '#55598D', '#628497', '#A9C6CB', '#866EA9', '#B79BC7',
                  '#7D7D7E', '#CACACA', '#A7A7A8', '#606063', '#C4C4C4', '#99999B', '#B7B7B7']
area_color_list = ['#D55659', '#E1777A', '#DB8A66', '#E5B88C', '#EEB2B4', '#D57C56', '#E39A79',
                   '#8588B7', '#626697', '#866EA9', '#B79BC7', '#B4B6D1', '#628497', '#A9C6CB',
                   '#7D7D7E', '#A7A7A8', '#99999B', '#B7B7B7', '#CACACA', '#969696', '#C4C4C4']
new_color_list = ['#F04950', '#959595', '#6268A2', '#333335', '#D57C56', '#628497']


def to_percent(temp, position):
    return '%1.0f'%(temp) + '%'

def to_percent_r2(temp, position):
    return '%0.01f'%(temp) + '%'

def to_100percent(temp, position):
    return '%1.0f'%(temp * 100) + '%'

def to_100percent_r2(temp, position):
    return '%0.01f'%(temp * 100) + '%'

def get_date(start_date, end_date):
    calendar_df = HBDB().read_cal(start_date, end_date)
    calendar_df = calendar_df.rename(columns={'JYRQ': 'CALENDAR_DATE', 'SFJJ': 'IS_OPEN', 'SFZM': 'IS_WEEK_END', 'SFYM': 'IS_MONTH_END'})
    calendar_df['CALENDAR_DATE'] = calendar_df['CALENDAR_DATE'].astype(str)
    calendar_df = calendar_df.sort_values('CALENDAR_DATE')
    calendar_df['IS_OPEN'] = calendar_df['IS_OPEN'].astype(int).replace({0: 1, 1: 0})
    calendar_df['YEAR_MONTH'] = calendar_df['CALENDAR_DATE'].apply(lambda x: x[:6])
    calendar_df['MONTH'] = calendar_df['CALENDAR_DATE'].apply(lambda x: x[4:6])
    calendar_df['MONTH_DAY'] = calendar_df['CALENDAR_DATE'].apply(lambda x: x[4:])
    calendar_df = calendar_df[(calendar_df['CALENDAR_DATE'] >= start_date) & (calendar_df['CALENDAR_DATE'] <= end_date)]
    trade_df = calendar_df[calendar_df['IS_OPEN'] == 1].rename(columns={'CALENDAR_DATE': 'TRADE_DATE'})
    trade_df = trade_df[(trade_df['TRADE_DATE'] >= start_date) & (trade_df['TRADE_DATE'] <= end_date)]
    report_df = calendar_df.drop_duplicates('YEAR_MONTH', keep='last').rename(columns={'CALENDAR_DATE': 'REPORT_DATE'})
    report_df = report_df[report_df['MONTH_DAY'].isin(['0331', '0630', '0930', '1231'])]
    report_df = report_df[(report_df['REPORT_DATE'] >= start_date) & (report_df['REPORT_DATE'] <= end_date)]
    report_trade_df = calendar_df[calendar_df['IS_OPEN'] == 1].rename(columns={'CALENDAR_DATE': 'TRADE_DATE'})
    report_trade_df = report_trade_df.sort_values('TRADE_DATE').drop_duplicates('YEAR_MONTH', keep='last')
    report_trade_df = report_trade_df[report_trade_df['MONTH'].isin(['03', '06', '09', '12'])]
    report_trade_df = report_trade_df[(report_trade_df['TRADE_DATE'] >= start_date) & (report_trade_df['TRADE_DATE'] <= end_date)]
    calendar_trade_df = calendar_df[['CALENDAR_DATE']].merge(trade_df[['TRADE_DATE']], left_on=['CALENDAR_DATE'], right_on=['TRADE_DATE'], how='left')
    calendar_trade_df['TRADE_DATE'] = calendar_trade_df['TRADE_DATE'].fillna(method='ffill')
    calendar_trade_df = calendar_trade_df[(calendar_trade_df['TRADE_DATE'] >= start_date) & (calendar_trade_df['TRADE_DATE'] <= end_date)]
    return calendar_df, report_df, trade_df, report_trade_df, calendar_trade_df

def quantile_definition(idxs, col, daily_df):
    part_df = daily_df.iloc[list(map(int, idxs))].copy(deep=True)
    q = (1.0 - np.count_nonzero(part_df[col].iloc[-1] <= part_df[col]) / len(part_df))
    return q

class StyleTest:
    def __init__(self, data_path, start_date, end_date):
        self.data_path = data_path
        self.start_date = start_date
        self.end_date = end_date
        self.calendar_df, self.report_df, self.trade_df, self.report_trade_df, self.calendar_trade_df = get_date('19000101', self.end_date)

    def test(self):
        style_data = FEDB().read_timing_data(['TRADE_DATE', 'GROWTH_CROWDING', 'VALUE_CROWDING', 'GROWTH_SPREAD', 'VALUE_SPREAD', 'GROWTH_MOMENTUM', 'VALUE_MOMENTUM'], 'timing_style', self.start_date, self.end_date)
        style_data = style_data[(style_data['TRADE_DATE'] > self.start_date) & (style_data['TRADE_DATE'] <= self.end_date)]
        style_data = style_data.dropna()

        growth_index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['399370'])
        growth_index = growth_index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        growth_index = growth_index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        growth_index['TRADE_DATE'] = growth_index['TRADE_DATE'].astype(str)
        growth_data = style_data[['TRADE_DATE', 'GROWTH_CROWDING', 'GROWTH_SPREAD', 'GROWTH_MOMENTUM']]
        growth_data['GROWTH_TIMING'] = (growth_data['GROWTH_CROWDING'] * (-1.0) + growth_data['GROWTH_MOMENTUM']) / 2.0
        # growth_data['GROWTH_TIMING'] = growth_data['GROWTH_CROWDING'] * (-1.0)
        # growth_data['GROWTH_TIMING'] = growth_data['GROWTH_TIMING'].rolling(window=20, min_periods=1, center=False).mean()
        growth_data = growth_data.merge(growth_index, on=['TRADE_DATE'], how='left')
        growth_data_disp = growth_data[growth_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        # growth_data_disp = growth_data.copy(deep=True)
        growth_data_disp['TRADE_DATE_DISP'] = growth_data_disp['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

        value_index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['399371'])
        value_index = value_index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        value_index = value_index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        value_index['TRADE_DATE'] = value_index['TRADE_DATE'].astype(str)
        value_data = style_data[['TRADE_DATE', 'VALUE_CROWDING', 'VALUE_SPREAD', 'VALUE_MOMENTUM']]
        value_data['VALUE_TIMING'] = (value_data['VALUE_CROWDING'] * (-1.0) + value_data['VALUE_MOMENTUM']) / 2.0
        # value_data['VALUE_TIMING'] = value_data['VALUE_CROWDING'] * (-1.0)
        # value_data['VALUE_TIMING'] = value_data['VALUE_TIMING'].rolling(window=20, min_periods=1, center=False).mean()
        value_data = value_data.merge(value_index, on=['TRADE_DATE'], how='left')
        value_data_disp = value_data[value_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        # value_data_disp = value_data.copy(deep=True)
        value_data_disp['TRADE_DATE_DISP'] = value_data_disp['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax2 = ax1.twinx()
        ax1.plot(growth_data_disp['TRADE_DATE_DISP'].values, growth_data_disp['GROWTH_TIMING'].values, color=line_color_list[0], label='成长择时因子')
        ax2.plot(growth_data_disp['TRADE_DATE_DISP'].values, growth_data_disp['CLOSE_INDEX'].values, color=line_color_list[1], label='国证成长指数走势（右轴）')
        ax1.plot(value_data_disp['TRADE_DATE_DISP'].values, value_data_disp['VALUE_TIMING'].values, color=line_color_list[2], label='价值择时因子')
        ax2.plot(value_data_disp['TRADE_DATE_DISP'].values, value_data_disp['CLOSE_INDEX'].values, color=line_color_list[3], label='国证价值指数走势（右轴）')
        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        plt.legend(handles=h1 + h2, labels=l1 + l2, loc=8, bbox_to_anchor=(0.5, -0.15), ncol=4)
        plt.title('风格择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=False, left=False, bottom=False)
        plt.savefig('{0}style_timing.png'.format(self.data_path))

        growth_data['GROWTH_TIMING_UP1'] = growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1,  center=False).mean() + 0.5 * growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        growth_data['GROWTH_TIMING_DOWN1'] = growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 0.5 * growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        growth_data['GROWTH_TIMING_UP15'] = growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 1.0 * growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        growth_data['GROWTH_TIMING_DOWN15'] = growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 1.0 * growth_data['GROWTH_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        growth_data['GROWTH_TIMING_SCORE'] = growth_data.apply(lambda x: 5 if x['GROWTH_TIMING'] >= x['GROWTH_TIMING_UP15'] else
                                                                         4 if x['GROWTH_TIMING'] >= x['GROWTH_TIMING_UP1'] else
                                                                         1 if x['GROWTH_TIMING'] <= x['GROWTH_TIMING_DOWN15'] else
                                                                         2 if x['GROWTH_TIMING'] <= x['GROWTH_TIMING_DOWN1'] else 3, axis=1)
        growth_res = growth_data[growth_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        growth_index['CLOSE_INDEX'] = growth_index['CLOSE_INDEX'] / growth_index['CLOSE_INDEX'].iloc[0]
        growth_index['RET'] = growth_index['CLOSE_INDEX'].pct_change()
        growth_index = growth_index.merge(growth_res[['TRADE_DATE', 'GROWTH_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        growth_index = growth_index.fillna(method='ffill')
        growth_index['RET_ADJ'] = growth_index.apply(lambda x: x['RET'] if x['GROWTH_TIMING_SCORE'] == 4 or x['GROWTH_TIMING_SCORE'] == 5 else 0.0, axis=1)
        growth_index['RET_ADJ'] = growth_index['RET_ADJ'].fillna(0.0)
        growth_index['NAV'] = (growth_index['RET_ADJ'] + 1).cumprod()
        growth_index['TRADE_DATE_DISP'] = growth_index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        growth_index_1 = growth_index[growth_index['GROWTH_TIMING_SCORE'] == 1]
        growth_index_2 = growth_index[growth_index['GROWTH_TIMING_SCORE'] == 2]
        growth_index_3 = growth_index[growth_index['GROWTH_TIMING_SCORE'] == 3]
        growth_index_4 = growth_index[growth_index['GROWTH_TIMING_SCORE'] == 4]
        growth_index_5 = growth_index[growth_index['GROWTH_TIMING_SCORE'] == 5]
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(growth_index['TRADE_DATE_DISP'].values, growth_index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(growth_index['TRADE_DATE_DISP'].values, growth_index['CLOSE_INDEX'].values, color=line_color_list[3], label='国证成长指数走势')
        ax.scatter(growth_index_1['TRADE_DATE_DISP'].values, growth_index_1['CLOSE_INDEX'].values, color=line_color_list[1], label='得分1')
        ax.scatter(growth_index_2['TRADE_DATE_DISP'].values, growth_index_2['CLOSE_INDEX'].values, color=line_color_list[9], label='得分2')
        ax.scatter(growth_index_3['TRADE_DATE_DISP'].values, growth_index_3['CLOSE_INDEX'].values, color=line_color_list[3], label='得分3')
        ax.scatter(growth_index_4['TRADE_DATE_DISP'].values, growth_index_4['CLOSE_INDEX'].values, color=line_color_list[4], label='得分4')
        ax.scatter(growth_index_5['TRADE_DATE_DISP'].values, growth_index_5['CLOSE_INDEX'].values, color=line_color_list[0], label='得分5')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=7)
        plt.title('成长择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}growth_timing.png'.format(self.data_path))

        value_data['VALUE_TIMING_UP1'] = value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 0.5 * value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        value_data['VALUE_TIMING_DOWN1'] = value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 0.5 * value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        value_data['VALUE_TIMING_UP15'] = value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 1.0 * value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        value_data['VALUE_TIMING_DOWN15'] = value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 1.0 * value_data['VALUE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        value_data['VALUE_TIMING_SCORE'] = value_data.apply(lambda x: 5 if x['VALUE_TIMING'] >= x['VALUE_TIMING_UP15'] else
                                                                      4 if x['VALUE_TIMING'] >= x['VALUE_TIMING_UP1'] else
                                                                      1 if x['VALUE_TIMING'] <= x['VALUE_TIMING_DOWN15'] else
                                                                      2 if x['VALUE_TIMING'] <= x['VALUE_TIMING_DOWN1'] else 3, axis=1)
        value_res = value_data[value_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        value_index['CLOSE_INDEX'] = value_index['CLOSE_INDEX'] / value_index['CLOSE_INDEX'].iloc[0]
        value_index['RET'] = value_index['CLOSE_INDEX'].pct_change()
        value_index = value_index.merge(value_res[['TRADE_DATE', 'VALUE_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        value_index = value_index.fillna(method='ffill')
        value_index['RET_ADJ'] = value_index.apply(lambda x: x['RET'] if x['VALUE_TIMING_SCORE'] == 4 or x['VALUE_TIMING_SCORE'] == 5 else 0.0, axis=1)
        value_index['RET_ADJ'] = value_index['RET_ADJ'].fillna(0.0)
        value_index['NAV'] = (value_index['RET_ADJ'] + 1).cumprod()
        value_index['TRADE_DATE_DISP'] = value_index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        value_index_1 = value_index[value_index['VALUE_TIMING_SCORE'] == 1]
        value_index_2 = value_index[value_index['VALUE_TIMING_SCORE'] == 2]
        value_index_3 = value_index[value_index['VALUE_TIMING_SCORE'] == 3]
        value_index_4 = value_index[value_index['VALUE_TIMING_SCORE'] == 4]
        value_index_5 = value_index[value_index['VALUE_TIMING_SCORE'] == 5]
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(value_index['TRADE_DATE_DISP'].values, value_index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(value_index['TRADE_DATE_DISP'].values, value_index['CLOSE_INDEX'].values, color=line_color_list[3], label='国证价值指数走势')
        ax.scatter(value_index_1['TRADE_DATE_DISP'].values, value_index_1['CLOSE_INDEX'].values,  color=line_color_list[1], label='得分1')
        ax.scatter(value_index_2['TRADE_DATE_DISP'].values, value_index_2['CLOSE_INDEX'].values, color=line_color_list[9], label='得分2')
        ax.scatter(value_index_3['TRADE_DATE_DISP'].values, value_index_3['CLOSE_INDEX'].values, color=line_color_list[3], label='得分3')
        ax.scatter(value_index_4['TRADE_DATE_DISP'].values, value_index_4['CLOSE_INDEX'].values, color=line_color_list[4], label='得分4')
        ax.scatter(value_index_5['TRADE_DATE_DISP'].values, value_index_5['CLOSE_INDEX'].values, color=line_color_list[0], label='得分5')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=7)
        plt.title('价值择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}value_timing.png'.format(self.data_path))

        style_res = growth_res[['TRADE_DATE', 'GROWTH_TIMING_SCORE']].merge(value_res[['TRADE_DATE', 'VALUE_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        style_res['GROWTH_VALUE'] = style_res['GROWTH_TIMING_SCORE'] - style_res['VALUE_TIMING_SCORE']
        style_res['VALUE_GROWTH'] = style_res['VALUE_TIMING_SCORE'] - style_res['GROWTH_TIMING_SCORE']
        style_res['MARK'] = '均衡'
        style_res.loc[(style_res['GROWTH_TIMING_SCORE'] >= 4) & (style_res['GROWTH_VALUE'] >= 1), 'MARK'] = '成长'
        style_res.loc[(style_res['VALUE_TIMING_SCORE'] >= 4) & (style_res['VALUE_GROWTH'] >= 1), 'MARK'] = '价值'
        style_stats = style_res[['TRADE_DATE', 'MARK']].groupby('MARK').count()
        print(style_stats)

        index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['881001', '399370', '399371'])
        index = index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        index = index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        index['TRADE_DATE'] = index['TRADE_DATE'].astype(str)
        index = index.pivot(index='TRADE_DATE', columns='INDEX_SYMBOL', values='CLOSE_INDEX').sort_index()
        index_ret = index.pct_change()
        index_ret.columns = [col + '_RET' for col in index_ret.columns]
        index = index.merge(index_ret, left_index=True, right_index=True, how='left').merge(style_res.set_index('TRADE_DATE')[['MARK']], left_index=True, right_index=True, how='left')
        index = index.reset_index()
        index['MARK'] = index['MARK'].fillna(method='ffill')
        index = index.dropna(subset=['MARK'])
        index['RET_ADJ'] = index.apply(lambda x: x['399370_RET'] if x['MARK'] == '成长' else x['399371_RET'] if x['MARK'] == '价值' else x['881001_RET'], axis=1)
        index['RET_ADJ'] = index['RET_ADJ'].fillna(0.0)
        index['RET_ADJ'].iloc[0] = 0.0
        index['NAV'] = (index['RET_ADJ'] + 1).cumprod()
        index[['399370', '399371', '881001']] = index[['399370', '399371', '881001']] / index[['399370', '399371', '881001']].iloc[0]
        index['TRADE_DATE_DISP'] = index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        index_growth = index[index['MARK'] == '成长']
        index_balance = index[index['MARK'] == '均衡']
        index_value = index[index['MARK'] == '价值']
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(index['TRADE_DATE_DISP'].values, index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(index['TRADE_DATE_DISP'].values, index['881001'].values, color=line_color_list[3], label='万得全A走势')
        ax.scatter(index_growth['TRADE_DATE_DISP'].values, index_growth['881001'].values,  color=line_color_list[0], label='成长')
        ax.scatter(index_balance['TRADE_DATE_DISP'].values, index_balance['881001'].values, color=line_color_list[3], label='均衡')
        ax.scatter(index_value['TRADE_DATE_DISP'].values, index_value['881001'].values, color=line_color_list[1], label='价值')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=5)
        plt.title('风格择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}style_timing_strategy.png'.format(self.data_path))
        return

class SizeTest:
    def __init__(self, data_path, start_date, end_date):
        self.data_path = data_path
        self.start_date = start_date
        self.end_date = end_date
        self.calendar_df, self.report_df, self.trade_df, self.report_trade_df, self.calendar_trade_df = get_date('19000101', self.end_date)

    def test(self):
        size_data = FEDB().read_timing_data(['TRADE_DATE', 'SIZE_CROWDING', 'SIZE_SPREAD', 'SIZE_MOMENTUM'], 'timing_style', self.start_date, self.end_date)
        size_data.columns = ['TRADE_DATE', 'LARGE_CROWDING', 'LARGE_SPREAD', 'LARGE_MOMENTUM']
        size_data = size_data[(size_data['TRADE_DATE'] > self.start_date) & (size_data['TRADE_DATE'] <= self.end_date)]
        size_data = size_data.dropna()
        size_data_ = pd.read_hdf('{0}style_timing.hdf'.format(self.data_path), key='table')
        size_data_ = size_data_[['TRADE_DATE', 'SIZE_CROWDING', 'SIZE_SPREAD', 'SIZE_MOMENTUM']]
        size_data_.columns = ['TRADE_DATE', 'SMALL_CROWDING', 'SMALL_SPREAD', 'SMALL_MOMENTUM']
        size_data_ = size_data_[(size_data_['TRADE_DATE'] > self.start_date) & (size_data_['TRADE_DATE'] <= self.end_date)]
        size_data_ = size_data_.dropna()
        size_data = size_data.merge(size_data_, on=['TRADE_DATE'], how='left')

        large_index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['000300'])
        large_index = large_index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        large_index = large_index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        large_index['TRADE_DATE'] = large_index['TRADE_DATE'].astype(str)
        large_data = size_data[['TRADE_DATE', 'LARGE_CROWDING', 'LARGE_SPREAD', 'LARGE_MOMENTUM']]
        large_data['LARGE_TIMING'] = (large_data['LARGE_CROWDING'] * (-1.0) + large_data['LARGE_MOMENTUM']) / 2.0
        # large_data['LARGE_TIMING'] = large_data['LARGE_CROWDING'] * (-1.0)
        # large_data['LARGE_TIMING'] = large_data['LARGE_TIMING'].rolling(window=20, min_periods=1, center=False).mean()
        large_data = large_data.merge(large_index, on=['TRADE_DATE'], how='left')
        large_data_disp = large_data[large_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        # large_data_disp = large_data.copy(deep=True)
        large_data_disp['TRADE_DATE_DISP'] = large_data_disp['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

        small_index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['000905'])
        small_index = small_index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        small_index = small_index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        small_index['TRADE_DATE'] = small_index['TRADE_DATE'].astype(str)
        small_data = size_data[['TRADE_DATE', 'SMALL_CROWDING', 'SMALL_SPREAD', 'SMALL_MOMENTUM']]
        small_data['SMALL_TIMING'] = (small_data['SMALL_CROWDING'] * (-1.0) + small_data['SMALL_MOMENTUM']) / 2.0
        # small_data['SMALL_TIMING'] = small_data['SMALL_CROWDING'] * (-1.0)
        # small_data['SMALL_TIMING'] = small_data['SMALL_TIMING'].rolling(window=20, min_periods=1, center=False).mean()
        small_data = small_data.merge(small_index, on=['TRADE_DATE'], how='left')
        small_data_disp = small_data[small_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        # small_data_disp = small_data.copy(deep=True)
        small_data_disp['TRADE_DATE_DISP'] = small_data_disp['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))

        fig, ax1 = plt.subplots(figsize=(12, 6))
        ax2 = ax1.twinx()
        ax1.plot(large_data_disp['TRADE_DATE_DISP'].values, large_data_disp['LARGE_TIMING'].values, color=line_color_list[0], label='大盘择时因子')
        ax2.plot(large_data_disp['TRADE_DATE_DISP'].values, large_data_disp['CLOSE_INDEX'].values, color=line_color_list[1], label='沪深300指数走势（右轴）')
        ax1.plot(small_data_disp['TRADE_DATE_DISP'].values, small_data_disp['SMALL_TIMING'].values, color=line_color_list[2], label='中小盘择时因子')
        ax2.plot(small_data_disp['TRADE_DATE_DISP'].values, small_data_disp['CLOSE_INDEX'].values, color=line_color_list[3], label='中证500指数走势（右轴）')
        h1, l1 = ax1.get_legend_handles_labels()
        h2, l2 = ax2.get_legend_handles_labels()
        plt.legend(handles=h1 + h2, labels=l1 + l2, loc=8, bbox_to_anchor=(0.5, -0.15), ncol=4)
        plt.title('规模择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=False, left=False, bottom=False)
        plt.savefig('{0}size_timing.png'.format(self.data_path))

        large_data['LARGE_TIMING_UP1'] = large_data['LARGE_TIMING'].rolling(window=250, min_periods=1,  center=False).mean() + 0.5 * large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        large_data['LARGE_TIMING_DOWN1'] = large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 0.5 * large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        large_data['LARGE_TIMING_UP15'] = large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 1.0 * large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        large_data['LARGE_TIMING_DOWN15'] = large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 1.0 * large_data['LARGE_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        large_data['LARGE_TIMING_SCORE'] = large_data.apply(lambda x: 5 if x['LARGE_TIMING'] >= x['LARGE_TIMING_UP15'] else
                                                                     4 if x['LARGE_TIMING'] >= x['LARGE_TIMING_UP1'] else
                                                                     1 if x['LARGE_TIMING'] <= x['LARGE_TIMING_DOWN15'] else
                                                                     2 if x['LARGE_TIMING'] <= x['LARGE_TIMING_DOWN1'] else 3, axis=1)
        large_res = large_data[large_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        large_index['CLOSE_INDEX'] = large_index['CLOSE_INDEX'] / large_index['CLOSE_INDEX'].iloc[0]
        large_index['RET'] = large_index['CLOSE_INDEX'].pct_change()
        large_index = large_index.merge(large_res[['TRADE_DATE', 'LARGE_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        large_index = large_index.fillna(method='ffill')
        large_index['RET_ADJ'] = large_index.apply(lambda x: x['RET'] if x['LARGE_TIMING_SCORE'] == 4 or x['LARGE_TIMING_SCORE'] == 5 else 0.0, axis=1)
        large_index['RET_ADJ'] = large_index['RET_ADJ'].fillna(0.0)
        large_index['NAV'] = (large_index['RET_ADJ'] + 1).cumprod()
        large_index['TRADE_DATE_DISP'] = large_index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        large_index_1 = large_index[large_index['LARGE_TIMING_SCORE'] == 1]
        large_index_2 = large_index[large_index['LARGE_TIMING_SCORE'] == 2]
        large_index_3 = large_index[large_index['LARGE_TIMING_SCORE'] == 3]
        large_index_4 = large_index[large_index['LARGE_TIMING_SCORE'] == 4]
        large_index_5 = large_index[large_index['LARGE_TIMING_SCORE'] == 5]
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(large_index['TRADE_DATE_DISP'].values, large_index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(large_index['TRADE_DATE_DISP'].values, large_index['CLOSE_INDEX'].values, color=line_color_list[3], label='沪深300指数走势')
        ax.scatter(large_index_1['TRADE_DATE_DISP'].values, large_index_1['CLOSE_INDEX'].values, color=line_color_list[1], label='得分1')
        ax.scatter(large_index_2['TRADE_DATE_DISP'].values, large_index_2['CLOSE_INDEX'].values, color=line_color_list[9], label='得分2')
        ax.scatter(large_index_3['TRADE_DATE_DISP'].values, large_index_3['CLOSE_INDEX'].values, color=line_color_list[3], label='得分3')
        ax.scatter(large_index_4['TRADE_DATE_DISP'].values, large_index_4['CLOSE_INDEX'].values, color=line_color_list[4], label='得分4')
        ax.scatter(large_index_5['TRADE_DATE_DISP'].values, large_index_5['CLOSE_INDEX'].values, color=line_color_list[0], label='得分5')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=7)
        plt.title('大盘择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}large_timing.png'.format(self.data_path))

        small_data['SMALL_TIMING_UP1'] = small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 0.5 * small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        small_data['SMALL_TIMING_DOWN1'] = small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 0.5 * small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        small_data['SMALL_TIMING_UP15'] = small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).mean() + 1.0 * small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        small_data['SMALL_TIMING_DOWN15'] = small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).mean() - 1.0 * small_data['SMALL_TIMING'].rolling(window=250, min_periods=1, center=False).std(ddof=1)
        small_data['SMALL_TIMING_SCORE'] = small_data.apply(lambda x: 5 if x['SMALL_TIMING'] >= x['SMALL_TIMING_UP15'] else
                                                                      4 if x['SMALL_TIMING'] >= x['SMALL_TIMING_UP1'] else
                                                                      1 if x['SMALL_TIMING'] <= x['SMALL_TIMING_DOWN15'] else
                                                                      2 if x['SMALL_TIMING'] <= x['SMALL_TIMING_DOWN1'] else 3, axis=1)
        small_res = small_data[small_data['TRADE_DATE'].isin(self.trade_df[self.trade_df['IS_MONTH_END'] == '1']['TRADE_DATE'].unique().tolist())]
        small_index['CLOSE_INDEX'] = small_index['CLOSE_INDEX'] / small_index['CLOSE_INDEX'].iloc[0]
        small_index['RET'] = small_index['CLOSE_INDEX'].pct_change()
        small_index = small_index.merge(small_res[['TRADE_DATE', 'SMALL_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        small_index = small_index.fillna(method='ffill')
        small_index['RET_ADJ'] = small_index.apply(lambda x: x['RET'] if x['SMALL_TIMING_SCORE'] == 4 or x['SMALL_TIMING_SCORE'] == 5 else 0.0, axis=1)
        small_index['RET_ADJ'] = small_index['RET_ADJ'].fillna(0.0)
        small_index['NAV'] = (small_index['RET_ADJ'] + 1).cumprod()
        small_index['TRADE_DATE_DISP'] = small_index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        small_index_1 = small_index[small_index['SMALL_TIMING_SCORE'] == 1]
        small_index_2 = small_index[small_index['SMALL_TIMING_SCORE'] == 2]
        small_index_3 = small_index[small_index['SMALL_TIMING_SCORE'] == 3]
        small_index_4 = small_index[small_index['SMALL_TIMING_SCORE'] == 4]
        small_index_5 = small_index[small_index['SMALL_TIMING_SCORE'] == 5]
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(small_index['TRADE_DATE_DISP'].values, small_index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(small_index['TRADE_DATE_DISP'].values, small_index['CLOSE_INDEX'].values, color=line_color_list[3], label='中证500指数走势')
        ax.scatter(small_index_1['TRADE_DATE_DISP'].values, small_index_1['CLOSE_INDEX'].values,  color=line_color_list[1], label='得分1')
        ax.scatter(small_index_2['TRADE_DATE_DISP'].values, small_index_2['CLOSE_INDEX'].values, color=line_color_list[9], label='得分2')
        ax.scatter(small_index_3['TRADE_DATE_DISP'].values, small_index_3['CLOSE_INDEX'].values, color=line_color_list[3], label='得分3')
        ax.scatter(small_index_4['TRADE_DATE_DISP'].values, small_index_4['CLOSE_INDEX'].values, color=line_color_list[4], label='得分4')
        ax.scatter(small_index_5['TRADE_DATE_DISP'].values, small_index_5['CLOSE_INDEX'].values, color=line_color_list[0], label='得分5')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=7)
        plt.title('中小盘择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}small_timing.png'.format(self.data_path))

        size_res = large_res[['TRADE_DATE', 'LARGE_TIMING_SCORE']].merge(small_res[['TRADE_DATE', 'SMALL_TIMING_SCORE']], on=['TRADE_DATE'], how='left')
        size_res['LARGE_SMALL'] = size_res['LARGE_TIMING_SCORE'] - size_res['SMALL_TIMING_SCORE']
        size_res['SMALL_LARGE'] = size_res['SMALL_TIMING_SCORE'] - size_res['LARGE_TIMING_SCORE']
        size_res['MARK'] = '均衡'
        size_res.loc[(size_res['LARGE_TIMING_SCORE'] >= 4) & (size_res['LARGE_SMALL'] >= 1), 'MARK'] = '大盘'
        size_res.loc[(size_res['SMALL_TIMING_SCORE'] >= 4) & (size_res['SMALL_LARGE'] >= 1), 'MARK'] = '中小盘'
        size_stats = size_res[['TRADE_DATE', 'MARK']].groupby('MARK').count()
        print(size_stats)

        index = HBDB().read_index_daily_k_given_date_and_indexs(self.start_date, ['881001', '000300', '000905'])
        index = index.rename(columns={'zqdm': 'INDEX_SYMBOL', 'jyrq': 'TRADE_DATE', 'spjg': 'CLOSE_INDEX'})
        index = index[['TRADE_DATE', 'INDEX_SYMBOL', 'CLOSE_INDEX']]
        index['TRADE_DATE'] = index['TRADE_DATE'].astype(str)
        index = index.pivot(index='TRADE_DATE', columns='INDEX_SYMBOL', values='CLOSE_INDEX').sort_index()
        index_ret = index.pct_change()
        index_ret.columns = [col + '_RET' for col in index_ret.columns]
        index = index.merge(index_ret, left_index=True, right_index=True, how='left').merge(size_res.set_index('TRADE_DATE')[['MARK']], left_index=True, right_index=True, how='left')
        index = index.reset_index()
        index['MARK'] = index['MARK'].fillna(method='ffill')
        index = index.dropna(subset=['MARK'])
        index['RET_ADJ'] = index.apply(lambda x: x['000300_RET'] if x['MARK'] == '大盘' else x['000905_RET'] if x['MARK'] == '中小盘' else x['881001_RET'], axis=1)
        index['RET_ADJ'] = index['RET_ADJ'].fillna(0.0)
        index['RET_ADJ'].iloc[0] = 0.0
        index['NAV'] = (index['RET_ADJ'] + 1).cumprod()
        index[['000300', '000905', '881001']] = index[['000300', '000905', '881001']] / index[['000300', '000905', '881001']].iloc[0]
        index['TRADE_DATE_DISP'] = index['TRADE_DATE'].apply(lambda x: datetime.strptime(x, '%Y%m%d'))
        index_large = index[index['MARK'] == '大盘']
        index_balance = index[index['MARK'] == '均衡']
        index_small = index[index['MARK'] == '中小盘']
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(index['TRADE_DATE_DISP'].values, index['NAV'].values, color=line_color_list[0], label='择时策略走势')
        ax.plot(index['TRADE_DATE_DISP'].values, index['881001'].values, color=line_color_list[3], label='万得全A走势')
        ax.scatter(index_large['TRADE_DATE_DISP'].values, index_large['881001'].values,  color=line_color_list[0], label='大盘')
        ax.scatter(index_balance['TRADE_DATE_DISP'].values, index_balance['881001'].values, color=line_color_list[3], label='均衡')
        ax.scatter(index_small['TRADE_DATE_DISP'].values, index_small['881001'].values, color=line_color_list[1], label='中小盘')
        plt.legend(loc=8, bbox_to_anchor=(0.5, -0.15), ncol=5)
        plt.title('规模择时', fontdict={'font': 'kaiti', 'weight': 'bold', 'size': 16})
        plt.tight_layout()
        sns.despine(top=True, right=True, left=False, bottom=False)
        plt.savefig('{0}size_timing_strategy.png'.format(self.data_path))
        return

if __name__ == '__main__':
    data_path = 'D:/Git/hbshare/hbshare/fe/xwq/data/taa/'
    start_date = '20091231'
    end_date = '20221231'
    StyleTest(data_path, start_date, end_date).test()
    SizeTest(data_path, start_date, end_date).test()

