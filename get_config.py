#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/06/22 17:02
# @Author : 王海侠
# @FileName: get_config.py

import sys
sys.path.append("../")
import configparser


class Conf(object):
    def __init__(self,config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()
        self.config.read_file(open(self.config_file))

    def getconf(self,env,*args):
        data = []
        for para in args:
            data.append(self.config.get(env,para))
        return data
