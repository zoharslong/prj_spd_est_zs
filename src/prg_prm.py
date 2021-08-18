#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020-02-25
basic import and export program.
@author: zoharslong
"""
from .__init__ import chk_sys
from .prg_tkn import dct_jgh, dct_sql, str_mng  # 自用的极光ip代理卡密, mysql库卡密, mongodb库卡密
from pyzohar import dtz


lst_bch_bke_zs = [
    'xiaolanzhen', 'banfuzhen', 'henglanzhen', 'minzhongzhen', 'shenwanzhen', 'fushazhen', 'huangpuzhen',
    'sanxiangzhen', 'sanjiaozhen', 'dongfengzhen', 'dongqu', 'dongshengzhen1', 'nantouzhen', 'nanlangzhen',
    'guzhenzhen', 'tanzhouzhen', 'dayongzhen', 'xiqu', 'nanqu', 'shiqiqu', 'huoju', 'gangkouzhen', 'shaxizhen',
    'wuguishan',
]           # 贝壳行政片区区划, 系统自动在收尾拼接'start', 'end'
lst_bch_qfg_zs = [
    'tanzhoua', 'dongqua', 'huojukaifaqua', 'banfua', 'dayonga', 'dongfenga', 'dongshenga', 'fushaa',
    'gangkoua', 'guzhena', 'henglana', 'huangpua', 'minzhonga', 'nanlanga', 'nanqua', 'nantoua', 'sanjiaoa',
    'shiqia', 'sanxianga', 'shaxia', 'shenwana', 'xiqua', 'wuguishana', 'xiaolana', 'cuihengxinqua',
]           # Q房行政片区区划, 系统自动在收尾拼接'start', 'end'

lcn_est_shd_bke_sz = {
    'url_lst': 'https://sz.ke.com/xiaoqu/start/pg(\d+)/',
    'url_ctt': 'https://sz.ke.com/xiaoqu/(\d+)/',
    'url_htp': 'get',
    'prx': 'auto',    # proxy从极光调用
    'prx_tkn': dct_jgh,
    'hdr': {
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Connection': 'Keep-Alive',
        'Host': 'sz.ke.com',
        'Referer': 'https://sz.ke.com/ershoufang/',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_est_shd_bke_sz',
    'ppc': {
        'ndx_rgx': {'BeikeEstateNo': '(\d+)'},
        'ndx': ['BeikeEstateNo'],
        'clm_typ': {
            'BeikeEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
            'EstateName': 'str',        # 列表页
            'DistrictName': 'str',      # 列表页
            'AreaName': 'str',          # 列表页
            'age': 'str',               # 列表页
            '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_ctt': 'str',        # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # 贝壳二手小区
lcn_shw_shd_bke_sz = {
    'sql': dct_sql,  # Tencent cloud
    'sdb': 'db_spd_szd', 'tbl': 'tbl_spd_shw_shd_bke_sz_210621',
    'fld': './dst/doc_xpt', 'fls': 'shw_shd_bke_sz_' + dtz('now').dtt_to_typ(rtn=True) + '.xlsx',
    'url_lst': 'https://sz.ke.com/ershoufang/start/pg(\d+)co32sf2sf5/',
    'url_ctt': 'https://sz.ke.com/ershoufang/(\d+).html/',
    'url_htp': 'get',  # 默认缺省
    'prx': 'auto',  # proxy从极光调用
    'prx_tkn': dct_jgh,  # 申请代理的token
    'hdr': {
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Host': 'sz.ke.com',
        'Referer': 'https://sz.ke.com/ershoufang/',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_shw_shd_bke_sz_210621',
    'ppc': {
        'ndx_rgx': {'BeikeEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
        'ndx': ['BeikeEstateNo', '__time_day'],
        'clm_typ': {
            'BeikeEstateNo': 'str',     # 列表页, 二手产品id系统, in format '\d+'
            'CommunityNo': 'str',       # 小区id
            'title': 'str',             # 外推标题
            'EstateName': 'str',        # 小区名称
            'HouseInfo': 'str',         # 房屋信息
            'followInfo': 'str',        # 跟单信息
            'tag': 'str',               # 标签
            'aprice': 'str',            # 列表页本房成交信息
            'tprice': 'str',            # 列表页本房成交周期
            '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_day': 'str',        # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_ctt': 'str',        # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # 贝壳二手放盘

#
# # # 当前在用爬虫
# est_shd_ctn = dfz(lcn={
#     'url_lst': 'https://sz.centanet.com/xiaoqu/g(\d+)/',
#     'url_ctt': 'https://sz.centanet.com/xiaoqu/(xq-\w+)',
#     'prx': 'auto',    # proxy从极光调用
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_est_shd_ctn',
#     'ppc': {
#         'ndx_rgx': {'CentaEstateNo': '(xq-\w+)'},
#         'ndx': ['CentaEstateNo'],
#         'clm_typ': {
#             'CentaEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             'EstateName': 'str',        # 列表页
#             'DistrictName': 'str',      # 列表页
#             'AreaName': 'str',          # 列表页
#             'aprice': 'str',            # 列表页, in format '\d+元/平'
#             'age': 'str',               # 列表页, in format '[0-9]{4}年'
#             'onsale': 'str',            # 列表页, 在售量
#             'onrent': 'str',            # 列表页, 在租量
#             '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '__time_ctt': 'str'         # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#         }
#     },
# })          # 中原二手小区
# dlg_shd_ctn = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'dlg_shd_ctn_' + dtz('now').dtt_to_typ(rtn=True) + '.xlsx',
#     'url_lst': 'https://sz.centanet.com/xiaoqu/g(\d+)/',
#     'url_ctt': 'https://sz.centanet.com/xiaoqu/(xq-\w+)/cj/g1/',
#     'prx': 'auto',    # proxy从极光调用
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_ctn',
#     'ppc': {
#         'ndx_rgx': {'CentaEstateNo': '(xq-\w+)'},
#         'ndx': ['CentaEstateNo', '成交时间', '成交价', '面积', '经纪人'],
#         'clm_typ': {
#             'CentaEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '__time_ctt': 'str',        # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '户型': 'str',
#             '朝向': 'str',
#             '楼层': 'str',
#             '面积': 'str',
#             '成交时间': 'str',
#             '成交价': 'str',
#             '单价': 'str',
#             '经纪人': 'str'
#         }
#     },
# })          # 中原二手成交
#
# dlg_shd_ctn_dly = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'dlg_shd_ctn_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
#     'url_lst': 'https://sz.centanet.com/chengjiao/g(\d+)/',  # 'https://sz.ke.com/xiaoqu/luohuqu/pg(\d+)/'
#     'url_ctt': 'https://sz.centanet.com/chengjiao/xq-(\w+)/g1',
#     'prx': 'auto',    # proxy从极光调用
#     'hdr': {},
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_ctn',
#     'ppc': dlg_shd_ctn.lcn['ppc'],
# })      # 贝壳二手成交每日更新
# dlg_shd_bke = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'dlg_shd_bke_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
#     'url_lst': 'https://sz.ke.com/xiaoqu/pg(\d+)/',  # 'https://sz.ke.com/xiaoqu/luohuqu/pg(\d+)/'
#     'url_ctt': 'https://sz.ke.com/chengjiao/c(\d+)/pg1/',
#     'prx': 'auto',    # proxy从极光调用
#     'hdr': {
#         'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
#         'Cache-Control': 'no-cache',
#         'Connection': 'Keep-Alive',
#         'Host': 'sz.ke.com',
#         'Referer': 'https://sz.ke.com/ershoufang/',
#         'Upgrade-Insecure-Requests': '1',
#     },
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_bke',
#     'ppc': {
#         'ndx_rgx': {'BeikeEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
#         'ndx': ['BeikeEstateNo', 'est_rom_sqr', 'dealDate', 'totalPrice'],
#         'clm_typ': {
#             'BeikeEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '__time_ctt': 'str',        # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#         }
#     },
# })          # 贝壳二手成交全部
# dlg_shd_bke_dly = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'dlg_shd_bke_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
#     'url_lst': 'https://sz.ke.com/chengjiao/pg(\d+)/',  # 'https://sz.ke.com/xiaoqu/luohuqu/pg(\d+)/'
#     'url_ctt': 'https://sz.ke.com/chengjiao/c(\d+)/pg1/',
#     'prx': 'auto',    # proxy从极光调用
#     'hdr': {
#         'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
#         'Cache-Control': 'no-cache',
#         'Connection': 'Keep-Alive',
#         'Host': 'sz.ke.com',
#         'Referer': 'https://sz.ke.com/ershoufang/',
#         'Upgrade-Insecure-Requests': '1',
#     },
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_bke',
#     'ppc': {
#         'ndx_rgx': {'BeikeEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
#         'ndx': ['BeikeEstateNo', 'est_rom_sqr', 'dealDate', 'totalPrice'],
#         'clm_typ': {
#             'BeikeEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             '__time': 'str',            # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '__time_ctt': 'str',        # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#         }
#     },
# })      # 贝壳二手成交每日更新
#
# lst_shd_ctn = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'lst_shd_ctn_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
#     # 'url_lst': 'https://sz.centanet.com/ershoufang/start/g(\d+)/',
#     'url_lst': 'https://sz.centanet.com/ershoufang/g(\d+)/',
#     'url_ctt': 'https://sz.centanet.com/ershoufang/(\w*\d+).html/',
#     'prx': 'auto',    # proxy从极光调用
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_lst_shd_ctn',
#     'ppc': {
#         'ndx_rgx': {'shd_id': '(\w*\d+)'},
#         'ndx': ['shd_id'],
#         'clm_typ': {
#             'shd_id': 'str',
#             'est_id': 'str',
#             'district': 'str',      # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             'area': 'str',
#             'estname': 'str',       # 列表页
#             '户型': 'str',
#             '面积': 'str',
#             'houseinfo': 'str',     # 列表页
#             'tprice': 'str',        # 列表页
#             'aprice': 'str',        # 列表页
#             'new': 'str',
#             '__time': 'str',        # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             '__time_ctt': 'str',    # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#         }
#     },
# })          # 中原二手挂牌
#
# lst_shd_bke = dfz(lcn={
#     'fld': './dst/doc_xpt', 'fls': 'lst_shd_bke_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
#     'url_lst': 'https://sz.ke.com/ershoufang/pg(\d+)co32sf2sf5/',     # 按照发布事件顺序开始爬取
#     # 'url_lst': 'https://sz.ke.com/ershoufang/start/pg(\d+)/',   # 使用特定方法全局爬取
#     'url_ctt': 'https://sz.ke.com/ershoufang/(\d+).html/',
#     'prx': 'auto',    # proxy从极光调用
#     'hdr': {
#         'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'Keep-Alive',
#         'Host': 'sz.ke.com',
#         'Refer': 'https://sz.ke.com/ershoufang/co32/',
#         'Upgrade-Insecure-Requests': '1',
#     },
#     'mng': 'mongodb://shenlong:sl19890421@172.16.0.7:27017/admin' if chk_sys in ['Linux'] else None,
#     'mdb': 'dbs_spd', 'cln': 'cln_lst_shd_bke',
#     'ppc': {
#         'ndx_rgx': {'shd_id': '(\d+)'},
#         'ndx': ['shd_id'],
#         'clm_typ': {
#             'shd_id': 'str',        # 列表页
#             'est_id': 'str',        # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
#             'estname': 'str',       # 列表页
#             'houseinfo': 'str',     # 列表页
#             'tag': 'str',           # 列表页
#             'push': 'str',          # 列表页
#             'tprice': 'str',        # 列表页
#             'aprice': 'str',        # 列表页
#             'tprice_p': 'str',      # 列表页
#             'aprice_p': 'str',      # 列表页
#             '__time': 'str',        # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#             'newOn': 'str',         # 详情页
#             '__time_ctt': 'str',    # 详情页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
#         }
#     },
# })          # 贝壳二手挂牌
