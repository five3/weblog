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
        id = inputParams['id'] if 'id' in inputParams else 'myfav'    
        tplData = self.getData(id)
#         print tplData    
        try:            
            content = web.template.frender('templates/%s/%s.htm' % (settings.TEMPLATE_THEME, id))(tplData) 
        except:
            content = 'No TEMPLATE FILE FOR  %s'  % id
        self.assign('content', content)
        prefix = '/person/index/id_'
        leftsideList = {prefix + 'myfav' : '我的收藏', prefix + 'ebook': '电子书' }
        self.assign('leftsideList', leftsideList)
        return self.display('custom')

    def getData(self, id, pars={}):
        if hasattr(self, id):
            return getattr(self, id)(pars)
        else:
            return None
        
    def myfav(self, pars={}):
        urlObj = model.favurl()
        rt = urlObj.getList('name, url, category', {'status': 1}, 'category asc')
        td = {}
        if rt:
            tl = []
            precate = rt[0]['category']
            td[precate] = []
            for d in rt:
                if d['category'] != precate:
                    precate = d['category']
                    td[precate] = []
                td[precate].append(d)
        return td
                    
        
        