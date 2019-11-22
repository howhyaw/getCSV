#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/1 10:41
# @Author : 王海侠
# @FileName: getData.py

import pymysql
import re

class mysql_data(object):
    def __init__(self,host,port,user,passwd,db,charset):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
    def get_conn(self):
        # 连接mysql数据库
        try:
            self.conn = pymysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        except pymysql.Error as e:
            print(e)
            print('连接数据库失败')

    def close_conn(self):
        # 关闭数据库
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print(e)
            print('关闭数据库失败')



    def exec_sql_return(self, sql):
        # 执行sql，并返回需要的数据，传入要执行的sql，rows_list_list可修改为所需要数据形式
        try:
            self.get_conn()
            cursor = self.conn.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            #rows_list_dict = [dict(zip([x[0] for x in cursor.description], row)) for row in rows]
            rows_list_list = [list(row) for row in rows]
            #print(rows_list_list)
            cursor.close()
            self.close_conn()
            return rows_list_list
        except AttributeError as e:
            print(e)
            return None






if __name__ == "__main__":
    database = mysql_data()
    header_line = database.get_head_line('tm_cs_01_002_0003.csv')
    print(header_line)
    target_table, target_column, target_desc, terminal_source = database.get_mysql_data('tm_cs_01_002_0003.csv', ['店铺id','时间粒度','地区','品牌'])
    print(target_table, target_column, target_desc,terminal_source)
    shop_id, shop_name = database.get_shop_info('71730686')
    print(shop_id, shop_name)





