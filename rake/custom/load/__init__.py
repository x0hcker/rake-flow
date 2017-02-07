#!/usr/bin/env python
# encoding: utf-8


"""
mail:wqc2008@gmail.com
@createtime: 17/1/19 下午5:43
@license: Apache Licence 2.0
usege:
    ......
    
"""


#!/usr/bin/env python
# encoding: utf-8

"""
mail:wqc2008@gmail.com
@createtime: 17/1/17 下午7:19
@license: Apache Licence 2.0
usege:
    ......

"""


__all__ = ['auto_load']


class autoload(object):
    '''
    自动引入模块类
    '''

    def __init__(self, class_path):

        self.class_path = class_path

    def import_and_get_mod(self, str, parent_mod=None):

        mods = str.split('.')
        child_mod_str = '.'.join(mods[1:])
        if parent_mod is None:
            if len(mods) > 1:
                # First time this function is called; import the module
                # __import__() will only return the top level module
                return self.import_and_get_mod(child_mod_str, __import__(str))
            else:
                return __import__(str)
        else:
            mod = getattr(parent_mod, mods[0])
            if len(mods) > 1:
                # We're not yet at the intended module; drill down
                return self.import_and_get_mod(child_mod_str, mod)
            else:
                return mod

    def get_mod(self):
        '''
        动态实例化工厂类
        '''
        if self.class_path:
            # 组装引入字符串
            name = self.class_path
            # 引入modle
            return self.import_and_get_mod(name)