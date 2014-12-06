# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class person(baseAction):
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
            id = 'myfav'
        self.assign('content', id)
        prefix = '/person/index/id_'
        leftsideList = {prefix + 'myfav' : '我的收藏', prefix + 'ebook': '电子书' }
        self.assign('leftsideList', leftsideList)
        return self.display('custom')
