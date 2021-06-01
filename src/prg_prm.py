#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2020-02-25
basic import and export program.
@author: zoharslong
"""
from .__init__ import chk_sys
from pyzohar import dtz
from prg_tkn import dct_jgh, dct_sql, str_mng  # 自用的极光ip, mysql库卡密, mongodb库卡密


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

lcn_est_shd_bke_zs = {
    'url_lst': 'https://zs.ke.com/xiaoqu/start/pg(\d+)/',
    'url_ctt': 'https://zs.ke.com/xiaoqu/(\d+)/',
    'url_htp': 'get',
    'prx': 'auto',    # proxy从极光调用
    'prx_tkn': dct_jgh,
    'hdr': {
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Connection': 'Keep-Alive',
        'Host': 'zs.ke.com',
        'Referer': 'https://zs.ke.com/ershoufang/',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_est_shd_bke_zs',
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
lcn_dlg_shd_bke_zs = {
    'sql': dct_sql,  # Tencent cloud
    'sdb': 'db_spd_zsd', 'tbl': 'tbl_spd_dlg_shd_bke_zs_210317',
    'fld': './dst/doc_xpt', 'fls': 'dlg_shd_bke_zs_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
    'url_lst': 'https://zs.ke.com/chengjiao/start/pg(\d+)/',
    'url_ctt': 'https://zs.ke.com/chengjiao/c(\d+)/pg1/',
    'url_htp': 'get',       # 默认缺省
    'prx': 'auto',          # proxy从极光调用
    'prx_tkn': dct_jgh,     # 申请代理的token
    'hdr': {
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Host': 'zs.ke.com',
        'Referer': 'https://zs.ke.com/chengjiao/',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_bke_zs',
    'ppc': {
        'ndx_rgx': {'BeikeEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
        'ndx': ['BeikeEstateNo', 'est_rom_sqr', 'dealDate', 'totalPrice'],
        'clm_typ': {
            'BeikeEstateNo': 'str',     # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
            'est_rom_sqr': 'str',       # 楼盘 户型 面积
            'dealDate': 'str',          # 成交日期 in format '%Y-%m-%d'
            'totalPrice': 'str',        # 总价
            'unitPrice': 'str',         # 单价
            'houseInfo': 'str',         # 房屋信息
            'positionInfo': 'str',      # 位置信息
            'dealHouseTxt': 'str',      # 本房成交信息
            'dealCycleTxt': 'str',      # 本房成交周期
            # 'EstateName': 'str',      # 小区页, 拼接而来, 小区名
            # 'DistrictName': 'str',    # 小区页, 拼接而来, 行政区
            # 'AreaName': 'str',        # 小区页, 拼接而来, 片区
            # 'age': 'str',             # 小区页, 拼接而来, 小区年代
            # '__time': 'str',          # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_ctt': 'str',        # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # 贝壳二手成交每日更新
lcn_shw_shd_bke_zs = {
    'sql': dct_sql,  # Tencent cloud
    'sdb': 'db_spd_zsd', 'tbl': 'tbl_spd_shw_shd_bke_zs_210430',
    'fld': './dst/doc_xpt', 'fls': 'shw_shd_bke_zs_' + dtz('now').dtt_to_typ(rtn=True) + '.xlsx',
    'url_lst': 'https://zs.ke.com/ershoufang/start/pg(\d+)co32/',
    'url_ctt': 'https://zs.ke.com/ershoufang/(\d+).html/',
    'url_htp': 'get',  # 默认缺省
    'prx': 'auto',  # proxy从极光调用
    'prx_tkn': dct_jgh,  # 申请代理的token
    'hdr': {
        'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'Keep-Alive',
        'Host': 'zs.ke.com',
        'Referer': 'https://zs.ke.com/ershoufang/',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_shw_shd_bke_zs',
    'ppc': {
        'ndx_rgx': {'BeikeEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
        'ndx': ['BeikeEstateNo', '__time_day'],
        'clm_typ': {
            'BeikeEstateNo': 'str',  # 列表页, 中原找房所使用的小区id系统, in format 'xq-\w+'
            'est_rom_sqr': 'str',  # 楼盘 户型 面积
            'dealDate': 'str',  # 成交日期 in format '%Y-%m-%d'
            'totalPrice': 'str',  # 总价
            'unitPrice': 'str',  # 单价
            'houseInfo': 'str',  # 房屋信息
            'positionInfo': 'str',  # 位置信息
            'dealHouseTxt': 'str',  # 本房成交信息
            'dealCycleTxt': 'str',  # 本房成交周期
            # 'EstateName': 'str',      # 小区页, 拼接而来, 小区名
            # 'DistrictName': 'str',    # 小区页, 拼接而来, 行政区
            # 'AreaName': 'str',        # 小区页, 拼接而来, 片区
            # 'age': 'str',             # 小区页, 拼接而来, 小区年代
            # '__time': 'str',          # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_ctt': 'str',  # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
            '__time_day': 'str',  # 列表页, 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # 贝壳二手放盘

lcn_dlg_shd_qfg_zs = {
    'sql': dct_sql,  # Tencent cloud
    'sdb': 'db_spd_zsd', 'tbl': 'tbl_spd_dlg_shd_qfg_zs_210320',
    'fld': './dst/doc_xpt', 'fls': 'dlg_shd_qfg_zs_'+dtz('now').dtt_to_typ(rtn=True)+'.xlsx',
    'url_lst': 'https://zhongshan.qfang.com/transaction/start/f(\d+)/',
    'url_ctt': 'https://zhongshan.qfang.com/transaction/(\d+)?insource=sale_list',
    'url_htp': 'get',
    'prx': 'auto',    # proxy从极光调用
    'prx_tkn': dct_jgh,
    'hdr': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'Keep-Alive',
        'Host': 'zhongshan.qfang.com',
        'Referer': 'https://zhongshan.qfang.com/transaction',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_dlg_shd_qfg_zs',
    'ppc': {
        'ndx_rgx': {'QfangEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
        'ndx': ['QfangEstateNo', 'est_rom_sqr', 'transaction', 'totalPrice'],
        'clm_typ': {
            'QfangEstateNo': 'str',     # Q房的小区id系统，因为并没有，所以用小区名代替
            'est_rom_sqr': 'str',       # 楼盘名 户型 面积
            'transaction': 'str',       # 成交时间 in format %Y-%m-%d
            'totalPrice': 'str',        # 总价
            'aprice': 'str',            # 单价
            'district': 'str',          # 行政区 片区
            'price': 'str',             # 总价单价
            'room': 'str',              # 户型
            'square': 'str',            # 面积
            'info': 'str',              # 其他信息
            'tags': 'str',              # 标签（学校地铁等）
            'address': 'str',           # 地址
            '__time_ctt': 'str',        # 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # q房二手成交每日更新
lcn_shw_shd_qfg_zs = {
    'sql': dct_sql,  # Tencent cloud
    'sdb': 'db_spd_zsd', 'tbl': 'tbl_spd_shw_shd_qfg_zs_210430',
    'fld': './dst/doc_xpt', 'fls': 'shw_shd_qfg_zs_' + dtz('now').dtt_to_typ(rtn=True) + '.xlsx',
    'url_lst': 'https://zhongshan.qfang.com/sale/start/f(\d+)/',
    'url_ctt': 'https://zhongshan.qfang.com/sale/(\d+)?insource=sale_list',
    'url_htp': 'get',
    'prx': 'auto',    # proxy从极光调用
    'prx_tkn': dct_jgh,
    'hdr': {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'Keep-Alive',
        'Host': 'zhongshan.qfang.com',
        'Referer': 'https://zhongshan.qfang.com/sale',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
    },
    'mng': str_mng if chk_sys in ['Linux'] else None,
    'mdb': 'dbs_spd', 'cln': 'cln_shw_shd_qfg_zs',
    'ppc': {
        'ndx_rgx': {'QfangEstateNo': '(\d+)'},  # 用于调整内容页url的关键信息
        'ndx': ['QfangEstateNo', '__time_day'],
        'clm_typ': {
            '__time_day': 'str',  # 按日记录时间戳 in format '%Y-%m-%d'
            'QfangEstateNo': 'str',  # Q房的小区id系统，因为并没有，所以用小区名代替
            'est_rom_sqr': 'str',  # 楼盘名 户型 面积
            'transaction': 'str',  # 成交时间 in format %Y-%m-%d
            'totalPrice': 'str',  # 总价
            'aprice': 'str',  # 单价
            'district': 'str',  # 行政区 片区
            'price': 'str',  # 总价单价
            'room': 'str',  # 户型
            'square': 'str',  # 面积
            'info': 'str',  # 其他信息
            'tags': 'str',  # 标签（学校地铁等）
            'address': 'str',  # 地址
            '__time_ctt': 'str',  # 信息爬取的时间 in format '%Y-%m-%d %H:%M:%S'
        }
    },
}       # q房二手放盘
