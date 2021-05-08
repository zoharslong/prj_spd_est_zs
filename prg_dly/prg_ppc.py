#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020-12-24
spider results pre-processing
@author: zoharslong
"""
from numpy import nan as np_nan
from pandas import DataFrame
from bs4 import BeautifulSoup
from re import findall as re_find, sub as re_sub
from pyzohar import dfz, lsz
from pyzohar.sub_slt_spd import spz
from .prg_prm import *


# 中山贝壳小区列表页数据提取
def sop_est_shd_bke_lst(slf):
    """
    Soup estate information from beike in list page of ZhongShan city
    @param slf: a spd with the target html page file
    @return: a DataFrame filled with useful data
    """
    sop = BeautifulSoup(slf.dts, features="html.parser")    # , features="lxml"
    dtf = DataFrame([])
    dtf['BeikeEstateNo'] = [
        re_find('xiaoqu/(\d+)/', i.find('a', class_='maidian-detail')['href'])[0] if
        i.find('a', class_='maidian-detail') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['EstateName'] = [
        i.find('a', class_='maidian-detail')['title'] if
        i.find('a', class_='maidian-detail') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['DistrictName'] = [
        i.find('a', class_='district').text if i.find('a', class_='district') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['AreaName'] = [
        i.find('a', class_='bizcircle').text if i.find('a', class_='bizcircle') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['age'] = [
        re_find('/?(\w+年建成)', i.find('div', class_='positionInfo').text.replace('\n', '').replace('\xa0', ''))[0] if
        i.find('div', class_='positionInfo') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['tag'] = [
        i.find('div', class_='tagList').text.replace('\n', '') if
        i.find('div', class_='tagList') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['aprice'] = [
        i.find('div', class_='totalPrice').text.replace('\n', '') if
        i.find('div', class_='totalPrice') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['onsale'] = [
        i.find('a', class_='totalSellCount').text.replace('\n', '') if
        i.find('a', class_='totalSellCount') is not None else None for
        i in sop.find_all('li', class_='xiaoquListItem')
    ]
    dtf['__time'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d %H:%M:%S', rtn=True)
    return dtf


# 中山贝壳二手成交列表页数据提取
def sop_dlg_shd_bke_lst_zs(slf, dfz_shd_bke=dfz(lcn=lcn_est_shd_bke_zs)):
    """
    Soup dealing logs on second hand dealing from beike in list page of ZhongShan city
    :param slf: a spd with the target html page file
    :param dfz_shd_bke: default est_shd_bke, 用于拼接BeikeEstateNo的贝壳小区详情
    :return: a dataframe filled with useful data
    """
    sop = BeautifulSoup(slf.dts, features="html.parser")    # , features="lxml"
    dtf = DataFrame([])
    dtf['est_rom_sqr'] = [
        i.find_all('a', class_="maidian-detail")[-1].text if i is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['houseInfo'] = [
        i.find('div', class_="houseInfo").text.replace('\n', '').replace(' ', '') if i is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['dealDate'] = [
        i.find('div', class_="dealDate").text.replace('\n', '').replace(' ', '').replace('.', '-') if
        i is not None else '' for i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['totalPrice'] = [
        i.find('div', class_="totalPrice").text.replace('\n', '').replace(' ', '') if i is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['unitPrice'] = [
        i.find('div', class_="unitPrice").text.replace('\n', '').replace(' ', '') if i is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['positionInfo'] = [
        i.find('div', class_="positionInfo").text.replace('\n', '').replace(' ', '') if i is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['dealHouseTxt'] = [
        i.find('span', class_="dealHouseTxt").text if i.find('span', class_="dealHouseTxt") is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['dealCycleTxt'] = [
        i.find('span', class_="dealCycleTxt").text if i.find('span', class_="dealCycleTxt") is not None else '' for
        i in sop.find('ul', class_='listContent').find_all('li', class_='VIEWDATA')
    ]
    dtf['__time_ctt'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d %H:%M:%S', rtn=True)
    dtf['BeikeEstateNo'] = [
        dfz_shd_bke._myCln.find_one({'EstateName': j}, ['BeikeEstateNo'])['BeikeEstateNo'] if
        dfz_shd_bke._myCln.find_one({'EstateName': j}, ['BeikeEstateNo']) is not None else j for
        j in [re_find('^(.*?) ', i)[0] for i in dtf['est_rom_sqr']]
    ]
    return dtf


# 中山贝壳二手挂盘列表页数据提取
def sop_shw_shd_bke_lst_zs(slf):
    sop = BeautifulSoup(slf.dts, features="html.parser")    # , features="lxml"
    dtf = DataFrame([])
    try:
        dtf['BeikeEstateNo'] = [
            re_find('fang/(\d+).html', i.find('div', class_="title").find('a')['href'])[0] for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['title'] = [
            re_sub('[\n\r\t]', '', i.find_all('div', class_="title")[0].text) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['EstateName'] = [
            re_sub('[\n\r\t]', '', i.find('div', class_='flood').text) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['HouseInfo'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='houseInfo').text)) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['followInfo'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='followInfo').text)) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['tag'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='tag').text)) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['tprice'] = [
            re_sub('[\n\t\r ]', '', i.find('div', class_='totalPrice').text) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['aprice'] = [
            re_sub('[\n\t\r ]|单价', '', i.find('div', class_='unitPrice').text) for
            i in sop.find('ul', class_='sellListContent').find_all('li', class_='clear')
        ]
        dtf['__time_ctt'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d %H:%M:%S', rtn=True)
        dtf['__time_day'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d', rtn=True)
    except (KeyError, ValueError):
        print('skip: nothing in this page.')
    return dtf


# 中山q房二手成交列表页数据提取
def sop_dlg_shd_qfg_lst_zs(slf):
    """
    Soup dealing logs on second hand dealing from Qfang in list page of ZhongShan city
    @param slf: a spd with the target html page file
    @return: a dataframe filled with useful data
    """
    sop = BeautifulSoup(slf.dts, features="html.parser")    # , features="lxml"
    dtf = DataFrame([])
    try:
        dtf['est_rom_sqr'] = [
            i.find('a', class_='house-title fl').text for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['info'] = [
            re_sub('[\[\]]', '', re_sub('<.*?>|\t|\r|\n', '', str(i.find_all('p', class_='meta-items')))) for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['transaction'] = [
            re_sub('\.', '-', re_sub('[\t\r\n ]', '', i.find('div', class_='transaction-tips').text)) for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['price'] = [
            re_sub('[\t\r\n ]', '', i.find(class_='list-price').text) for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['aprice'] = dtf.apply(lambda x: re_find('万(.*?)元/平米', x['price'])[0] if x['transaction'] != '近期内成交' else np_nan, axis=1)
        dtf['totalPrice'] = dtf.apply(lambda x: re_find('(^.*?)万', x['price'])[0], axis=1)
        dtf['room'] = dtf.apply(lambda x: re_find(' (\w+) ', x['est_rom_sqr'])[0], axis=1)
        dtf['square'] = dtf.apply(lambda x: re_find(' (\d+[.]{0,1}\d+平米$)', x['est_rom_sqr'])[0], axis=1)
        dtf['tags'] = [
            re_sub('[\t\r\n ]', '', i.find('div', class_='house-tags').text) for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['address'] = [
            re_sub('\n', ' ', re_sub('[\t\r ]', '', i.find('div', class_='text fl').text)) for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['district'] = dtf.apply(
            lambda x: re_find('\[(.*?)\]', x['address'])[0] if re_find('\[(.*?)\]', x['address']) else "", axis=1
        )
        dtf['address'] = dtf.apply(lambda x: re_find('\](.*$)', x['address'])[0], axis=1)
        dtf['QfangEstateNo'] = dtf.apply(lambda x: re_find('^(.*?) ', x['est_rom_sqr'])[0], axis=1)
        dtf['__time_ctt'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d %H:%M:%S', rtn=True)
    except (KeyError, ValueError):
        print('skip: nothing in this page.')
    return dtf


# 中山q房二手上加列表页
def sop_shw_shd_qfg_lst_zs(slf):
    sop = BeautifulSoup(slf.dts, features="html.parser")
    dtf = DataFrame([])
    try:
        dtf['QfangEstateNo'] = [
            re_find('sale/(\d+)\?', i.find('a', class_='house-title fl')['href'])[0] for i in
            sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['EstateName'] = [
            re_sub('[\n\t\r .]', '', i.find('div', class_='house-location').find('a', class_='link').text) for
            i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['title'] = [
            i.find('a', class_='house-title fl').text for i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['house_meta'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='house-metas').text)) for
            i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['district'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='house-location').text)) for
            i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['tags'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', ' ', i.find('div', class_='house-tags').text)) for
            i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['price'] = [
            re_sub('[ ]+', ' ', re_sub('[\n\t\r]', '', i.find('div', class_='list-price').text)) for
            i in sop.find('div', class_='list-result').find_all('li')
        ]
        dtf['tprice'] = dtf.apply(lambda x: re_find('(\d+)万', x['price'])[0] if re_find('(\d+)万', x['price']) else '',
                                  axis=1)
        dtf['aprice'] = dtf.apply(lambda x: re_find('万(\d+)元', x['price'])[0] if re_find('万(\d+)元', x['price']) else '',
                                  axis=1)
        dtf['__time_ctt'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d %H:%M:%S', rtn=True)
        dtf['__time_day'] = dtz('now').dtt_to_typ('str', '%Y-%m-%d', rtn=True)
    except (KeyError, ValueError):
        print('skip: nothing in this page.')
    return dtf


# 用于本项目的定制类 - spider for ZhongShan
class szs(spz):
    """
    web spider for ZhongShan city.
    >>> bke = szs(lcn=lcn_dlg_shd_bke_zs)
    >>> bke.spd_bch(sop_dlg_shd_bke_lst_zs, prm='lst', pg_max=4)                        # 顺着列表爬取到第四页
    >>> bke.spd_bch_whl_swh(sop_dlg_shd_bke_lst_zs, pg_max=4, lst_bch=lst_bch_bke_zs)   # 分行政区通刷各区前四页
    >>> bke.sql_xpt_dlg({'__time_ctt': {'$gte': '2021-03-01'}})                         # 指定日期后的数据入mySql
    >>> bke.lcl_xpt_dlg({'__time_ctt': {'$gte': '2021-03-01'}})                         # 指定日期后的数据入本地xlsx
    """
    def __init__(self, dts=None, lcn=None, *, spr=False):
        """
        Spider for ZhongShan city initiation
        @param dts: self.dts, premier than dfz_mpt
        @param lcn: self.lcn, premier than dfz_mpt
        @param spr: let self = self.dts
        """
        super(szs, self).__init__(dts, lcn, spr=spr)

    def _ng_mpt_mrg_est(self, dct_qry=None, *, est_lcn=None, est_clm=None, est_key=None):
        """
        Get deal and community data from mongodb, basic pre-processing
        @param dct_qry: search query of mongodb
        @param est_lcn: lcn of the dataframe to be merged
        @param est_clm: columns of the datafarme to be merged
        @param est_key: list of merged keys
        @return: Nonep
        """
        est_lcn = lcn_est_shd_bke_zs if est_lcn is None else est_lcn
        est_clm = ['BeikeEstateNo', 'EstateName', 'DistrictName', 'AreaName', 'age'] if est_clm is None else est_clm
        est_key = ['BeikeEstateNo'] if est_key is None else lsz(est_key).typ_to_lst(rtn=True)
        est = spz(lcn=est_lcn)
        est.mng_mpt(lst_clm=est_clm, prm='dtf')
        self.mng_mpt(dct_qry=dct_qry, prm='dtf')
        self.mrg_dtf(est.dts, est_key, prm='left')
        self.fll_clm_na('')

    def _ng_mpt_pur(self, dct_qry=None):
        """
        Purely import and simple pre-processing
        @param dct_qry: search query of mongodb
        @return: None
        """
        self.mng_mpt(dct_qry=dct_qry, prm='dtf')
        self.fll_clm_na('')

    def mng_mpt_dlg(self, dct_qry=None, *, est_lcn=None, est_clm=None, est_key=None):
        """
        Importing and pre-processing data from mongodb
        @param dct_qry: search query of mongodb
        @param est_lcn: lcn of the dataframe to be merged
        @param est_clm: columns of the datafarme to be merged
        @param est_key: list of merged keys
        @return: None
        """
        if self.lcn['cln'] in ['cln_dlg_shd_bke_zs']:       # 对贝壳成交的小区信息拼接后导入内存
            est_clm = ['BeikeEstateNo', 'EstateName', 'DistrictName', 'AreaName', 'age'] if est_clm is None else est_clm
            est_key = ['BeikeEstateNo'] if est_key is None else est_key
            self._ng_mpt_mrg_est(dct_qry=dct_qry, est_lcn=est_lcn, est_clm=est_clm, est_key=est_key)
        elif self.lcn['cln'] in ['cln_shw_shd_bke_zs']:
            est_clm = ['EstateName', 'DistrictName', 'AreaName', 'age'] if est_clm is None else est_clm
            est_key = ['EstateName'] if est_key is None else est_key
            self._ng_mpt_mrg_est(dct_qry=dct_qry, est_lcn=est_lcn, est_clm=est_clm, est_key=est_key)
        elif self.lcn['cln'] in ['cln_dlg_shd_qfg_zs']:     # 对Q房成交的导入内存
            self._ng_mpt_pur(dct_qry=dct_qry)
            self.drp_dcm_ctt('transaction', ['近期内成交'])
        elif self.lcn['cln'] in ['cln_shw_shd_qfg_zs']:
            self._ng_mpt_pur(dct_qry=dct_qry)
        else:
            raise KeyError('stop: needs self.lcn.cln in [cln_dlg_shd_qfg_zs, cln_dlg_shd_bke_zs]')

    def sql_xpt_dlg(self, dct_qry=None, *, est_lcn=None, est_clm=None, est_key=None):
        """
        Export pre-processed data into mysql
        @param dct_qry: search query of mongodb
        @param est_lcn: lcn of the dataframe to be merged
        @param est_clm: columns of the datafarme to be merged
        @param est_key: list of merged keys
        @return:
        """
        self.mng_mpt_dlg(dct_qry, est_lcn=est_lcn, est_clm=est_clm, est_key=est_key)
        self.sql_xpt()

    def lcl_xpt_dlg(self, dct_qry=None):
        """
        pre-processing and local exporting in .xlsx files
        @param dct_qry: query for mongodb importing
        @return: None
        """
        self.mng_mpt_dlg(dct_qry)
        self.lcl_xpt()
