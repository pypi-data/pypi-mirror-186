#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path

import akshare as ak
import pandas
from tqdm import tqdm
from mootdx.quotes import Quotes

from quant1x.data import *


class DataHandler:
    """数据"""

    """初始化"""

    def __init__(self):
        self.__root = os.path.expanduser(quant1x_home)
        self.__data_cn = os.path.expanduser(quant1x_data_cn)
        self.__data_hk = os.path.expanduser(quant1x_data_hk)
        self.__info_cn = os.path.expanduser(quant1x_info_cn)
        self.__info_hk = os.path.expanduser(quant1x_info_hk)

        if not os.path.exists(self.__root):
            os.makedirs(self.__root)

        self.__path = os.path.expanduser(quant1x_data)
        if not os.path.exists(self.__data_cn):
            os.makedirs(self.__data_cn)
        if not os.path.exists(self.__data_hk):
            os.makedirs(self.__data_hk)

        self.__info = os.path.expanduser(quant1x_info)
        if not os.path.exists(self.__info_cn):
            os.makedirs(self.__info_cn)
        if not os.path.exists(self.__info_hk):
            os.makedirs(self.__info_hk)

        self.__stock_list = {}
        # 自选股csv文件路径
        # 从自选股中获取证券代码列表
        # stock_list.columns = [
        #     "market",
        #     "code",
        #     "name",
        # ]
        zxg_csv = self.__path + '/zxg.csv'
        self.__stock_list = pandas.read_csv(zxg_csv)
        #print(self.__stock_list)

        # 标准市场
        self.__client = Quotes.factory(market='std', multithread=True, heartbeat=True)

    def update_history(self):
        """
        更新全量历史数据
        :return:
        """
        for key, value in enumerate(self.__stock_list.values):
            print('key:', key, ', value: ', value)
            code = value[1][2:]
            print("code:%s" % code)
            df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
            print(df)
            # df.to_csv(path_or_buf=self.__data_cn + '/' + code +'.csv', index=False)
            df.to_csv(self.__data_cn + '/' + code + '.csv', index=False)

    def dataset(self, code):
        """
        读取历史数据
        :param code:
        :return:
        """
        filename = self.__data_cn + '/' + code + '.csv'
        if not os.path.exists(filename):
            return
        df = pandas.read_csv(filename)
        df = df[["日期","开盘","收盘","最高","最低","成交量","成交额"]]
        df.columns=['time', 'open', 'close', 'high', 'low', 'volume', 'amount']  # 更正排序
        return df

    def __finance(self, code):
        """
        获取个股基本信息
        :param code:
        :return:
        """
        data = self.__client.finance(symbol=code[-6:])
        return data

    def update_info(self):
        """
        更新全量个股信息
        :return:
        """
        import time

        #tqdm.pandas(desc='个股基本面信息, 进行中')

        total = len(self.__stock_list)
        print("自选股基本面信息, 共计[%d]:" % total)
        values = enumerate(self.__stock_list.values)
        pbar = tqdm(values, total=total)
        for key, value in pbar:
            #print('key:', key, ', value: ', value)
            code = value[1][2:]
            #print("code:%s" % code)
            pbar.set_description_str("同步[%s]进行中" % code)
            data = self.__finance(code=code)
            data.to_csv(self.__info_cn + '/' + code + '.csv', index=False)
            #time.sleep(0.05)
            pbar.set_description_str("同步[%s]完成" % code)

        pbar.close()
        print("自选股基本面信息, 处理完成.")

    def finance(self, code):
        """
        读取本地基本面
        :param code:
        :return:
        """
        filename = self.__info_cn + '/' + code + '.csv'
        if not os.path.exists(filename):
            return
        df = pandas.read_csv(filename)
        return df