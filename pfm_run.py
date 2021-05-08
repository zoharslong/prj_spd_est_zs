#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2021.03.22
Start operation.
@author: zoharslong
"""
from prg_dly.prg_ppc import *
dtt_now = dtz('now').dtt_to_typ(rtn=True)  # 当前日期的标准格式'yyyy-mm-dd'
flt_pgs = [3, 4, 99]  # 分别适用于小区、成交、挂单的爬取页数要求

def pfm_run():
  pass



print('\n\n*****')
print('info: %s, good morning!' % dtt_now)
print('*****\n')

# 小区流程 - 中山贝壳
if dtz('now').dtt_to_typ('weekday', rtn=True) == 6:  # 每周六运行一次
  try:
    est = szs(lcn=lcn_est_shd_bke_zs)   # 中山贝壳小区刷新, 用于配合BeikeEstateNo拼接相关信息至贝壳成交
    est.spd_bch_whl_swh(sop_est_shd_bke_lst, pg_max=flt_pgs[0], lst_bch=lst_bch_bke_zs)  # 通刷
    # est.spd_bch(sop_est_shd_bke_lst, prm='lst', pg_max=11)
    # # # 本地集中导入小区信息开始
    # # from pandas import read_excel
    # # est.dts = read_excel('est.xlsx')
    # # est.ltr_clm_typ(est.lcn['ppc']['clm_typ'])
    # # est.fll_clm_na('')
    # # est.mng_xpt(est.lcn['ppc']['ndx'])
    # # # 本地集中导入小区信息结束
    print('*****')
    print('info: est_shd_bke_zs successed.')
  except:
    print('info: est_shd_bke_zs failed.')
  finally:
    print('*****\n')

# 爬虫流程 - 中山贝壳成交
try:
  bke = szs(lcn=lcn_dlg_shd_bke_zs)   # 中山贝壳二手成交更新
  bke.spd_bch(sop_dlg_shd_bke_lst_zs, prm='lst', pg_max=flt_pgs[1])
  # bke.spd_bch_whl_swh(sop_dlg_shd_bke_lst_zs, pg_max=70, lst_bch=lst_bch_bke_zs)    # 通刷
  print('*****')
  print('info: dlg_shd_bke_zs successed.')
except:
  print('info: dlg_shd_bke_zs failed.')
finally:
  bke = szs(lcn=lcn_dlg_shd_bke_zs)   # 入库流程
  bke.sql_xpt_dlg({'__time_ctt': {'$gte': dtt_now}})  # 当天以后的爬虫入库
  print('info: dlg_shd_bke_zs exported into mysql.')
  print('*****\n')

# 爬虫流程 - 中山贝壳挂盘
try:
  bke = szs(lcn=lcn_shw_shd_bke_zs)   # 中山贝壳二手挂盘
  bke.spd_bch(sop_shw_shd_bke_lst_zs, prm='lst', pg_max=flt_pgs[2])
  print('*****')
  print('info: shw_shd_bke_zs successed.')
except:
  print('info: shw_shd_bke_zs failed.')
finally:
  bke = szs(lcn=lcn_shw_shd_bke_zs)   # 入库流程
  bke.sql_xpt_dlg({'__time_ctt': {'$gte': dtt_now}})  # 当天以后的爬虫入库
  print('info: shw_shd_bke_zs exported into mysql.')
  print('*****\n')

# 爬虫流程 - 中山Q房成交
try:
  qfg = szs(lcn=lcn_dlg_shd_qfg_zs)   # 中山Q房二手成交更新
  qfg.spd_bch(sop_dlg_shd_qfg_lst_zs, prm='lst', pg_max=flt_pgs[1])
  # qfg.spd_bch_whl_swh(sop_dlg_shd_qfg_lst_zs, pg_max=40, lst_bch=lst_bch_qfg_zs)    # 通刷
  print('*****')
  print('info: dlg_shd_qfg_zs successed.')
except:
  print('info: dlg_shd_qfg_zs failed.')
finally:
  qfg = szs(lcn=lcn_dlg_shd_qfg_zs)   # 入库流程
  qfg.sql_xpt_dlg({'__time_ctt': {'$gte': dtt_now}})  # 当天以后的爬虫入库
  print('info: dlg_shd_qfg_zs exported into mysql.')
  print('*****\n')

# 爬虫流程 - 中山Q房挂盘
try:
  qfg = szs(lcn=lcn_shw_shd_qfg_zs)   # 中山Q房二手挂盘
  qfg.spd_bch(sop_shw_shd_qfg_lst_zs, prm='lst', pg_max=flt_pgs[2])
  print('*****')
  print('info: shw_shd_qfg_zs successed.')
except:
  print('info: shw_shd_qfg_zs failed.')
finally:
  qfg = szs(lcn=lcn_shw_shd_qfg_zs)   # 入库流程
  qfg.sql_xpt_dlg({'__time_ctt': {'$gte': dtt_now}})  # 当天以后的爬虫入库
  print('info: sgw_shd_qfg_zs exported into mysql.')
  print('*****\n')
