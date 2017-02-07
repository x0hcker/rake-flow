#!/usr/bin/env python
# encoding: utf-8

"""
mail:wqc2008@gmail.com
@createtime: 17/1/13 下午2:13
@license: Apache Licence 2.0
usege:
    ......
    
"""

import  sys
from rake.workflow import  producer



if __name__ == '__main__':


    try:
        p = producer(uri ="mongodb://localhost:27017/logs")

        for i in range(1,2):

            p.put("./test.yaml", priority = i )

    except KeyboardInterrupt:
        print "Ctrl-c pressed ..."
        sys.exit(1)








