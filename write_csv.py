#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/1 10:42
# @Author : 王海侠
# @FileName: write_csv.py


import csv
import os


def write_csv(header, write_data, filename):
    # header-标题 write_data-写入数据 filename-文件名
    with open(filename, 'a', newline='',encoding='utf-8-sig') as csvFile:
        writer = csv.writer(csvFile)
        if os.path.getsize(filename) == False:
            # 先写columns_name
            writer.writerow(header)
            # 写入多行用writerows
            writer.writerows(write_data)
