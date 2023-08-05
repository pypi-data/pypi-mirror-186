#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os.path

import pandas
import akshare as ak

from quant1x.data import *


class DataHandler:
    """数据"""
    __root = ''
    __path = ''
    __path_cn = ''
    __path_hk = ''

    __stock_list = {}

    """初始化"""
    def __init__(self):
        self.__root = os.path.expanduser(quant1x_home)
        self.__path_cn = os.path.expanduser(quant1x_data_cn)
        self.__path_hk = os.path.expanduser(quant1x_data_hk)
        if not os.path.exists(self.__root):
            os.makedirs(self.__root)
        if not os.path.exists(self.__path_cn):
            os.makedirs(self.__path_cn)
        if not os.path.exists(self.__path_hk):
            os.makedirs(self.__path_hk)
        self.__path = os.path.expanduser(quant1x_data)

    def update(self):
        # 自选股csv文件路径
        # 从自选股中获取证券代码列表
        zxg_csv = self.__path + '/zxg.csv'
        stock_list = pandas.read_csv(zxg_csv)
        # stock_list.columns = [
        #     "market",
        #     "code",
        #     "name",
        # ]
        print(stock_list)

        # for row in stock_list:
        #    print(row)

        # for key, value in stock_list.items():
        #     print ('key: ',key,'value: ',value)

        for key, value in enumerate(stock_list.values):
            print ('key:', key, ', value: ',value)
            code = value[1][2:]
            print("code:%s" % code)
            df = ak.stock_zh_a_hist(symbol=code, period="daily", adjust="qfq")
            df.to_csv(self.__path_cn + '/' + code +'.csv')



