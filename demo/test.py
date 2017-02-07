#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/1/23 下午3:28
@license: Apache Licence 2.0
usege:
    ......
    
"""

from rake.workflow.proxy import conf_proxy

dict = {

    'workflow': [
        {'task': 'setp1',
         "priority": 1,
         "hosts": ["192.168.56.101", "192.168.56.101"],
         "nodes": [
             {"nodename": 'phpfpm', "priority": 1, "cmd": "sh /data/shell/phpfpm.sh start"},
             {"nodename": 'nginx',  "priority": 2, "cmd": "sh /data/shell/nginx.sh start"},
         ]},
        {'task': 'setp2',
         "priority": 2,
         "hosts": ["192.168.56.101", "192.168.56.101"],
         "nodes": [
             {"nodename": 'phpfpm', "priority": 1, "cmd": "sh /data/shell/phpfpm.sh start"},
             {"nodename": 'nginx', "priority": 2, "cmd": "sh /data/shell/nginx.sh start"},
         ]},
        {'task': 'setp3',
         "priority": 3,
         "hosts": ["192.168.56.101", "192.168.56.101"],
         "nodes": [
             {"nodename": 'phpfpm', "priority": 1, "cmd": "sh /data/shell/phpfpm.sh start"},
             {"nodename": 'nginx', "priority": 2, "cmd": "sh /data/shell/nginx.sh start"},
         ]},
    ]
}

c = conf_proxy()
r = c.dumps(dict)
print(r)


d = c.loads(r)
print(d)