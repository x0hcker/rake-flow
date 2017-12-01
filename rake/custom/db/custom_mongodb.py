# /usr/bin/python
# coding=utf-8

"""
auth:wuqichao
mail:wuqichao@playcrab.com
createtime:2014-6-26下午12:13:07
usege:

"""

import sys

try:
    # Python 3.x
    from urllib.parse import quote_plus
except ImportError:
    # Python 2.x
    from urllib import quote_plus

try:
    import pymongo
    from pymongo import MongoClient

except ImportError:
    print >> sys.stderr, """\

There was a problem importing Python modules(pymongo) required.
The error leading to this problem was:
%s Please install a package which provides this module, or
verify that the module is installed correctly.
you can use this cmd :pip install pymongo

It's possible that the above module doesn't match the current version of Python,
which is:
%s
""" % (sys.exc_info(), sys.version)


class custom_mongodb():
    def __init__(self, uri=None,selectdb=None):

        """
        @param cursor_hander:数据库句柄
        """
        self.cursor = None
        self.connections = None
        self.conn = None
        self.uri = None

        if uri == None:
            print 'please write uri'
            exit(0)
        else:
            self.uri = uri

        # 建立和数据库系统的连接,创建Connection时，指定host及port参数
        self.conn = MongoClient(self.uri)
        #self.database = self.conn.get_default_database()

        if selectdb == None:
            self.database = self.conn.get_default_database()
        else:
            self.database = self.conn.get_database(selectdb)

    def __del__(self):

        self.close()

    def close(self):
        """
        关闭当前数据库句柄
        """
        if self.conn != None:
            return self.conn.close()

    def query(self, table_name, parameters, skip=None, limit=None):
        """
        @return: 返回一个list，多个结果。
        @param table_name:表名
        @param parameters:SQL语句参数
        """
        result = self.database[table_name].find(parameters)

        if skip != None:
            result.skip(skip)
        if limit != None:
            result.limit(limit)

        return result

    def get(self, table_name, **parameters):
        """
        @return: 返回单个结果
        @param table_name:表名
        @param parameters:SQL语句参数
        """
        return self.database[table_name].find_one(parameters)

    def count(self, table_name, **parameters):
        """
        @return: 返回单个结果
        @param table_name:表名
        @param parameters:SQL语句参数
        """
        return self.database[table_name].find(parameters).count()

    def insert(self, table, **datas):
        '''
        @param table:表名
        @param datas:｛字段：值｝
        '''
        return self.database[table].insert_one(datas).inserted_id

    def update(self, table, where, **datas):
        '''
        @param table:表名
        @param datas:｛字段：值｝
        '''
        return self.database[table].update(where, datas)

    def delete(self, table, where):
        '''
        @param table:表名
        @param datas:｛字段：值｝
        '''
        return self.database[table].remove(where)

    def find_one_and_update(self, table, where):
        '''
        @param table:表名
        @param datas:｛字段：值｝
        '''

        updata = {'$set': {'flag': 1}}
        sort = [('priority', pymongo.DESCENDING)]

        return self.database[table].find_one_and_update(where, updata, sort=sort)
