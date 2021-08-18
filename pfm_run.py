#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021.03.22
Start operation.
@author: zoharslong
"""
from src.prg_ppc import *


def pfm_run(lcn, sop, pg_max, *, gte_dtt=None):
  """
  爬虫、更新到mysql
  @param lcn: 爬虫dfz对应的参数字典
  @param sop: 爬虫页面的beautifulsoup解析方法
  @param pg_max: 爬取的页面数
  @param gte_dtt: 为了更新mysql而所需获取的爬虫运行时间
  @return: None
  """
  gte_dtt = dtz('now').dtt_to_typ(rtn=True) if gte_dtt is None else gte_dtt
  pfm = szs(lcn=lcn)  # 中山贝壳二手成交更新
  try:
    if type(pg_max) in [int, float]:
      pfm.spd_bch(sop, prm='lst', pg_max=pg_max)
    else:
      pfm.ltr_spd_for_dcm(1, 'gte', 'drop', False)
      pfm.spd_bch(sop, prm='ctt', srt={'cnt': 1})
    print('*****')
    print('info: %s successed.' % pfm.lcn['cln'])
  except:
    print('\n*****')
    print('*****')
    print('info: ERROR - %s failed.' % pfm.lcn['cln'])
    print('*****')
    print('*****\n')
  # finally:
    # pfm.sql_xpt_dlg({'__time_ctt': {'$gte': gte_dtt}})  # 当天以后的爬虫入库
    # print('info: %s exported into mysql on %s.' % (pfm.lcn['cln'], gte_dtt))
    print('*****\n')


print('\n\n*****')
print('info: %s, good morning!' % dtz('now').dtt_to_typ(rtn=True))
print('*****\n')
flt_pgs = [4, 9, 101]  # 分别适用于小区、成交、挂单的爬取页数要求
flt_pgs_qfg = 30

# 爬虫流程 - 深圳贝壳挂盘
pfm_run(lcn_shw_shd_bke_sz, sop_shw_shd_bke_lst_sz, flt_pgs[2])
# 爬虫流程 - 深圳贝壳挂盘详情
pfm_run(lcn_shw_shd_bke_sz, sop_shw_shd_qfg_ctt_sz, 'ctt')
