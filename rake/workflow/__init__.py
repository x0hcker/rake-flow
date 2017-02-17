#!/usr/bin/env python
# encoding: utf-8

"""
mail:wqc2008@gmail.com
@createtime: 17/1/17 下午7:19
@license: Apache Licence 2.0
usege:
    ......

"""

import time
from multiprocessing import Process
from threading import Thread

from proxy import  db_proxy, conf_proxy


class producer(Process):
    """
    生产者

    # baozi_make1 = producer(serializer ='json', uri ="mongodb://localhost:27017/logs")
    # baozi_make1.put({"key":"value9"},exchange ="exchange", priority = 9 )

    """

    def __init__(self, serializer='json', uri=None):
        """

        :param serializer:
        :param uri:
        """
        self.uri = uri
        self.serializer = serializer
        super(producer, self).__init__()  # 重写了父类的方法

    def put(self, payload_file = None,priority=1):
        """

        :param payload:
        :param priority:
        :return:
        """


        c = conf_proxy(payload_file)
        self.payload = c.load()
        self.priority= priority


        self.run()

    def run(self):

        """

        :return:
        """
        db = db_proxy(uri=self.uri)
        result = db.put(self.payload, self.priority)

        #print('%s生产:%s' % (self.exchange, self.payload))



class workflow(Thread):
    """
    workflow之间并行
    task之间串行
    task node之间串行
    """
    def __init__(self,data):
        """

        :param data:
        """
        Thread.__init__(self)
        self.data = data


    def run(self):


        workflow = self.data['workflow']
        from operator import itemgetter

        workflow.sort(key=itemgetter('priority'),reverse = True)

        #task之间串行
        for w in workflow:

            nodes = w['nodes']
            hosts = w['hosts']
            nodes.sort(key=itemgetter('priority'), reverse=True)



            cmds = []
            for host in hosts:

                # task node之间串行
                cmd = []
                for n in nodes:
                    cmd.append(n['cmd'])

                cmd_dict = {"cmd": "&".join(cmd),"ip":host,"username":w['username'],'port':w['port']}
                cmds.append(cmd_dict)


            from rake.workflow.task import task

            d = task(cmds)
            d.run()
            result =  d.get_result()
            print(result)



class consumer(Process):
    """
    消费者

    """

    def __init__(self, serializer='json', uri=None):
        """

        :param serializer:
        :param uri:
        """

        self.uri = uri
        self.serializer = serializer
        super(consumer, self).__init__()


    def run(self):

        db = db_proxy(uri=self.uri)

        while True:

            if db.empty():

                data = db.get()

                #workflow并行关系,所以开启线程
                w = workflow(data)
                w.start()

            else:
                time.sleep(1)