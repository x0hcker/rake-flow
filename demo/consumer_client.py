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

if __name__ == '__main__':


    try:

        temp = consumer(serializer='json', uri="mongodb://localhost:27017/logs")

        temp.start()


    except KeyboardInterrupt:
        print "Ctrl-c pressed ..."
        sys.exit(1)




