#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/1/22 下午5:25
@license: Apache Licence 2.0
usege:
    ......
    
"""


import yaml


import importlib
import os.path

from rake.custom.load import autoload


def file_extension(path):
    return os.path.splitext(path)[1].replace(".","")


class db_proxy(object):
    """
    各类型数据库的代理类
    """
    def __init__(self, uri=None):
        """

        :param serializer:
        :param uri:
        """

        self.table_name = "workflow"
        self.uri = uri
        engine = uri.split(":")[0]
        self.engine = engine

        a = autoload('rake.custom.db.custom_%s' % (self.engine))
        m = a.get_mod()
        self.db_object = getattr(m, 'custom_%s' % self.engine)(self.uri)

    def put(self, data=None, priority=1):
        """

        :param data:
        :param priority:
        :return:
        """

        tmp_data = {'priority': priority, 'flag': 0}
        tmp_data.update(data)

        return self.db_object.insert(self.table_name,**tmp_data)



    def get(self):

        """

        :return:
        """

        where = {'flag': 0}

        data = self.db_object.find_one_and_update(self.table_name, where)

        return data

    def empty(self):
        """

        :return:
        """

        where = {'flag': 0}
        count = self.db_object.count(self.table_name, **where)
        return count


class item_proxy(object):

    """
    数据存贮类型代理转换类
    """
    def __init__(self, format='pickle'):
        """

        :param format: pickle|json
        """
        self.format = format

    def dumps(self, data=None):
        """
        python对象转化为序列化数据
        :param data:
        :return:
        """
        tools = importlib.import_module(self.format)

        return tools.dumps(data)

    def loads(self, data=None):
        """
        序列化数据转化为python对象
        :param data:
        :return:
        """

        tools = importlib.import_module(self.format)

        return tools.loads(data)


class conf_proxy(object):
    """
    配置数据[yaml|json]转化为python的代理类
    """

    def __init__(self, filename= None):
        """

        :param format: json|yaml
        """
        self.filename = filename
        self.format = file_extension(self.filename)

        a = autoload('rake.custom.config.custom_%s' % (self.format))
        m = a.get_mod()
        self.conf_object = getattr(m, 'custom_%s' % self.format)(self.filename)

    def dump(self, data=None):
        """
        python对象转化为序列化数据
        :param data:
        :return:
        """

        return self.conf_object.dump(data)


    def load(self):
        """
        序列化数据转化为python对象
        :param data:
        :return:
        """

        return self.conf_object.load()

