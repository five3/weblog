# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
from utils.function import *
class user(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def up(self):
        rt = {'errorCode': 0, 'message': ''}
        inputParams = self.getPars()
#         print inputParams  
        if not inputParams.has_key('id') :
            rt['errorCode'] = -1000
            rt['message'] = '参数错误'
            return rt
        id=inputParams['id']
        result=model.cms().execute('update cms set up=up+1 where id=%s;' % id)
        if result:
            rt['message'] = '点赞成功！'
        else:
            rt['errorCode'] = -1001
            rt['message'] = '点赞失败'
        rt['id'] = id
        return rt

