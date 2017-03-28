#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/1/13 下午2:09
@license: Apache Licence 2.0
usege:
    ......
    
"""

import  sys

from rake.workflow import consumer


class C(consumer):

    def __init__(self,serializer='json', uri=None):

        super(C,self).__init__(serializer=serializer, uri=uri)

    def workflow_callback(self):

        print "workflow_callback"

if __name__ == '__main__':


    try:

        temp = C(serializer='json', uri="mongodb://localhost:27017/logs")

        temp.start()


    except KeyboardInterrupt:
        print "Ctrl-c pressed ..."
        sys.exit(1)




