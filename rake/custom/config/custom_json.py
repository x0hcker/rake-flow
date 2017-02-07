#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/1/23 下午4:26
@license: Apache Licence 2.0
usege:
    ......
    
"""

import  os
import  json



class custom_json(object):

    """
    数据存贮类型代理转换类
    """
    def __init__(self, filename):

        if os.path.exists(filename) and os.path.isfile(filename):

            self.filename = filename
        else:

            exit("not exit %s" % filename)


    def dump(self, data=None):
        """
        python对象序列化成json并存入文件
        :param data:
        :return:
        """

        with open(self.filename, 'w') as outfile:
            return  json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))


    def load(self):
        """
        读json文件反序列化成python对象
        :param data:
        :return:
        """

        with open(self.filename) as json_file:
            return json.load(json_file)

