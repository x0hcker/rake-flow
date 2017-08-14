# /usr/bin/python
#coding=utf-8

import redis
import json

class custom_redis():

    def __init__(self, uri=None):

        """
        @param cursor_hander: 数据库句柄
        """
        self.conn = None

        if uri == None:
            print 'please write uri'
            exit(0)
        else:
            self.uri = uri

        #建立和数据库系统的连接,创建Connection时，指定host及port参数
        self.conn = redis.from_url(url=self.uri)


    def keys(self):
        """
        获取所有的key
        :return:
        """
        return self.conn.keys()

    def close(self):
        """
        关闭连接
        :return:
        """
        if self.conn != None:
            del self.conn

    def get(self, key):
        """
        获取一条数据
        :param : key值
        :return: 结果
        """
        return self.conn.get(key)

    def set(self, key, value):
        """
        插入一条数据
        :param : 要插入的数据
        """
        self.conn.set(key, value)

    def sset(self,key,value):

        """
        插入一条数据
        :param key:
        :param value:
        :return:
        """

        self.conn.sset(key,value)


    def delete(self, key):
        """
        删除一条数据
        :param :
        """
        self.conn.delete(key)


    def insert(self,table_name,**data):

        """
        插入数据
        :param table_name:
        :param data:
        :return:
        """

        self.conn.lpush(table_name,json.dumps(data))


    def find_one_and_update(self, table_name, where = {}):

        """
        插入数据
        :param table_name:
        :param where:
        :return:
        """

        content = self.conn.rpoplpush(table_name,"%s_history" % table_name)

        return json.loads(content)



    def count(self,table_name,**parameters):

        '''
        返回单个结果
        :param table_name:
        :param parameters:
        :return:
        '''

        return self.conn.llen(table_name)



