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
    pfm.spd_bch(sop, prm='lst', pg_max=pg_max)
    print('*****')
    print('info: %s successed.' % pfm.lcn['cln'])
  except:
    print('\n*****')
    print('*****')
    print('info: ERROR - %s failed.' % pfm.lcn['cln'])
    print('*****')
    print('*****\n')
  finally:
    pfm.sql_xpt_dlg({'__time_ctt': {'$gte': gte_dtt}})  # 当天以后的爬虫入库
    print('info: %s exported into mysql on %s.' % (pfm.lcn['cln'], gte_dtt))
    print('*****\n')


def pfm_bch_zssgxkz(pgs=1, slf=None):
  """
  中山施工建设许可证，每日更新，可能会随着审批状态的变化由新行覆盖库内数据
  http://jsj.zs.gov.cn/dwfwxt/fdcxmspcx/index.html
  @param pgs: pages
  @param slf: rsl = dfz(lcn=lcn_zssgxkz_zs)
  @return: None
  """
  slf.lcn['prm']['page'] = pgs
  slf.lcn['prm']['start'] = (slf.lcn['prm']['page']-1)*20
  slf.api_run()
  slf.dts = slf.dts['rows']
  slf.typ_to_dtf()
  slf.rnm_clm(slf.lcn['ppc']['clm_rnm'])
  slf.ltr_clm_typ(slf.lcn['ppc']['clm_typ'])
  slf.ltr_clm_rpc('工程地址', '"', "'", prm='part')
  slf.srt_clm(list(slf.lcn['ppc']['clm_typ'].keys()))
  slf.sql_xpt()
  # slf.mng_xpt(lst_ndx=slf.lcn['ppc']['ndx'])


print('\n\n*****')
print('info: %s, good morning!' % dtz('now').dtt_to_typ(rtn=True))
print('*****\n')
flt_pgs = [4, 9, 99]  # 分别适用于小区、成交、挂单的爬取页数要求
flt_pgs_qfg = 30

# 爬虫流程 - 中山贝壳成交
pfm_run(lcn_dlg_shd_bke_zs, sop_dlg_shd_bke_lst_zs, flt_pgs[1])
# 爬虫流程 - 中山Q房成交
pfm_run(lcn_dlg_shd_qfg_zs, sop_dlg_shd_qfg_lst_zs, flt_pgs_qfg)

# 爬虫流程 - 中山贝壳挂盘
pfm_run(lcn_shw_shd_bke_zs, sop_shw_shd_bke_lst_zs, flt_pgs[2])
# 爬虫流程 - 中山Q房挂盘
pfm_run(lcn_shw_shd_qfg_zs, sop_shw_shd_qfg_lst_zs, flt_pgs[2])

# 爬虫流程 - 施工许可证
rsl = dfz(lcn=lcn_zssgxkz_zs)
pfm_bch_zssgxkz(3, rsl)
pfm_bch_zssgxkz(2, rsl)
pfm_bch_zssgxkz(1, rsl)

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
    print('*****\n')
  except:
    print('\n*****')
    print('*****')
    print('info: ERROR - est_shd_bke_zs failed.')
    print('*****')
    print('*****\n')



