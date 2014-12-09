# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class ip(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def logIp(self):
        ip = web.ctx.env.get('HTTP_X_REAL_IP') if web.ctx.env.get('HTTP_X_REAL_IP') else web.ctx.ip
#         print ip
        if ip in self.blackList:
            return self.error('你访问的过勤，我不想见你了。')
        path = web.ctx.env.get('REQUEST_URI')
        method = web.ctx.env.get('REQUEST_METHOD')
        data = {'ip': ip, 'path': path, 'method': method, 'create_date': time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())}
        ipObj = model.ip()
        ipObj.insert(data)
        
    def getBlackList(self):
        blacklistObj = model.blacklist()
        result = blacklistObj.getList('ip', {'status': 1})
        if result:
            blackList = [l['ip'] for l in result]
        else:
            blackList = []
        self.blackList = blackList
        return self.blackList
    