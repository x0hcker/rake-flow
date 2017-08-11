#!/usr/bin/env python
# encoding: utf-8

"""
mail:wqc2008@gmail.com
@createtime: 17/1/13 下午2:13
@license: Apache Licence 2.0
usege:
    ......
    
"""

import sys
sys.path.append("..")
from rake.workflow import producer



if __name__ == '__main__':

    try:
        p = producer(uri ="redis://@localhost:6379/0")

        for i in range(1,2):

            p.put("./test.yaml", priority = i )

    except KeyboardInterrupt:
        print "Ctrl-c pressed ..."
        sys.exit(1)








