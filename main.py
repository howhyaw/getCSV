#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/1 10:43
# @Author : 王海侠
# @FileName: main.py


import sys
import getData, get_config,write_csv


if __name__ == '__main__':


    # 获取数据库相关配置
    Conf = get_config.Conf('mysql_config.ini')
    host, port, user, passwd, db, charset = Conf.getconf("tidb_db_dm", "host", "port", "user", "passwd", "db","charset")
    database = getData.mysql_data(host, int(port), user, passwd, db,charset)
    header = ['出入库时间','OMS系统创建时间','原始订单创建时间','店铺名','经营模式','订单行经营模式','出入库类型','退换货单号','销售退换编码',
              '平台订单号','原始平台订单号','条形码','宝尊商品编码','货号','商品名称','商品购买数量','单价','吊牌价','成交价','支付总金额','订单类型',
              '运费','包装费','省份','城市','区域','收货地址','外围编码','SKU颜色','SKU尺码','平台账号','淘宝ID','积分','淘宝付款时间','参加活动',
              '大客户编码','大客户名字','快单号','快递公司','发货仓','成本中心代码','付款方式','支付宝流水号','发票类型','是否礼品','手机号',
              '收件人','Member ID','买家备注','卖家备注','内部产品品牌英文名称','内部产品品牌名称']
    # print(len(header))
    file = open('sql.txt','r', encoding='utf-8-sig')
    content = file.read()
    #print(content)
    data_list = database.exec_sql_return(content)
    write_csv.write_csv(header = header,write_data = data_list, filename= sys.argv[1])