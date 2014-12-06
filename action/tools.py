# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class tools(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def index(self):
        settings = self.getSettings()
        inputParams = self.getPars()
        if 'id' in inputParams:
            id = inputParams['id']
        else:
            id = 'zhanzhangseoPlug'
        try:
            content = web.template.frender('templates/%s/%s.htm' % (settings.TEMPLATE_THEME, id))() 
        except:
            content = 'No TEMPLATE FILE FOR  %s'  % id
        self.assign('content', content)
        prefix = '/tools/index/id_'
        leftsideList = {prefix + 'zhanzhangseoPlug' : '站长SEO助手', prefix + 'friendLinkTool': '友链定期检测' }
        self.assign('leftsideList', leftsideList)
        return self.display('custom')

    def seoinfo(self):
        settings = self.getSettings()
        inputParams = self.getPars()
        if 'host' in inputParams:
            host = inputParams['host']
        else:
            host = ''
        self.assign('host', host)
        return self.display('seoinfo')

