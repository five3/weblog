# -*- coding: utf-8 -*-
#!/usr/bin/env python
#coding=utf-8
import web,time
from action.base import base as baseAction
import model
class index(baseAction):
    def __init__(self, pars):
        baseAction.__init__(self, pars)
        settings = self.getSettings()
        self.assignTplDir(settings.TEMPLATE_THEME)
        
    def index(self):
        settings = self.getSettings()
        count = settings.PER_PAGE_COUNT
        inputParams = self.getPars()
        page = int(inputParams['page']) if inputParams.has_key('page') else 1
        offset= (page-1)*count if page > 0 else 0
        cmsObj = model.cms()
        condition = {'status':1}
        if 'category' in inputParams:
            condition['category'] = inputParams['category']            
        listData = cmsObj.getOne('COUNT(*) AS `total`',condition)
        totalCount = listData['total']
        cmsList = cmsObj.getList('*',condition,'orders desc,createTime desc',str(offset)+','+str(count))
        self.assign('cmsList',cmsList)
        path = web.ctx.env['PATH_INFO'] if web.ctx.env['PATH_INFO'].strip('/') else '/index/index'
        pageString = self.getPageStr(path, page,count,totalCount)
        self.assign('pageString',pageString)
#         commentObj=model.comment()
#         commentList = commentObj.getList('*',{'status':1},'id desc',str(offset)+','+str(count))
#         self.assign('commentList', commentList)  ##评论内容列表 
        unioObj = model.unio() 
        topHotList = unioObj.fetchAll('select id,name,preview_image_src from cms order by views desc limit 0,10')
        self.assign('topHotList', topHotList)  ##最热文章列表 
        categoryArtList = unioObj.fetchAll('select category.id, category.name, count(cms.id) as num from cms,category where category.id=cms.category GROUP BY cms.category order by num desc limit 0,10')
        self.assign('categoryArtList', categoryArtList)  ##分类归档列表  
        tagArtList = []
        self.assign('tagArtList', tagArtList)  ##标签归档列表  
        lastCommentList = unioObj.fetchAll('select cms.id, `comment`.content as name, cms.preview_image_src from cms, `comment` where cms.id=`comment`.cmsId order by `comment`.createTime desc limit 0,10') 
        self.assign('lastCommentList', lastCommentList)  ##最新评论列表  
        return self.display('index')
    def seo(self):
        return self.index()
    def songli(self):
        inputParams = self.getPars()
        if 'category' in inputParams:
            cate_id = int(inputParams['category'])
            cate_name = self.tplData['categoryList'].get(cate_id)
            self.assign('webTitle', cate_name) 
        return self.index()
    def tag(self):
        settings = self.getSettings()
        count = settings.PER_PAGE_COUNT
        inputParams = self.getPars()
        if 'name' not in inputParams:
            raise web.notfound(u"您的访问已超出本府管辖范围！")
        name = inputParams['name']
        page = int(inputParams['page']) if inputParams.has_key('page') else 1
        offset= (page-1)*count if page > 0 else 0
        cmsObj = model.cms()
        condition = u''' status=1 and tags like '%''' +name+'''%' '''
        sql = u'select COUNT(*) AS `total` from cms where '  + condition
#         print sql
        listData = cmsObj.fetchOne(sql)
        totalCount = listData['total']
        sql = u'select * from cms where ' + condition + ' ORDER BY  orders desc,createTime desc limit ' + str(offset)+','+str(count)
#         print sql 
        cmsList = cmsObj.fetchAll(sql)
        self.assign('cmsList',cmsList)
        pageString = self.getPageStr(self.makeUrl('index','index'),page,count,totalCount)
        self.assign('pageString',pageString)
        return self.display('index')
    
    def show(self):
        inputParams = self.getPars()
        if not inputParams.has_key('id') :
            settings = self.getSettings()
            web.seeother(settings.WEB_URL)
        id=inputParams['id']
        cmsObj = model.cms()
        condition = {'status':1,'id':str(id)}
        atl = cmsObj.getOne('*',condition)
#         print atl
        if not atl:
            raise web.notfound('not found')
        atl['views']+=1
        updateData = {'views':(atl['views'])}
        #view count 
        cmsObj.update(updateData,condition)
        commentList=model.comment().getList('*',{'status':1,'cmsId':int(id)})
        atl['categoryList'] = self.getCate()
        atl['tags'] = atl['tags'].split(u'，')
        self.assign('atl',atl)
        self.assign('commentList',commentList)
        self.assignSEO(atl['name'], atl['keywords'], atl['description'])
        if atl['category']:
            cate_id = atl['category']
            cate_name = self.tplData['categoryList'].get(cate_id)
            self.assign('webTitle', '%s_%s' % (self.tplData['webTitle'], cate_name)) 
        unioObj = model.unio() 
        topNewList = unioObj.fetchAll('select cms.id, cms.name, cms.preview_image_src from cms order by createTime desc limit 0,10')
        self.assign('topNewList', topNewList)  ##最新文章列表 
        categoryArtList = unioObj.fetchAll('select category.id, category.name, count(cms.id) as num from cms,category where category.id=cms.category GROUP BY cms.category order by num desc limit 0,10')
        self.assign('categoryArtList', categoryArtList)  ##分类归档列表 
        tagArtList = []
        self.assign('tagArtList', tagArtList)  ##标签归档列表 
        dateArtList = []
        self.assign('dateArtList', dateArtList)  ##日期归档列表 
        return self.display('show')  
    
    def comment(self):
        userInput= self.getInput()
        cmsObj = model.cms()
        cmsId = userInput['cmsId']
        condition = {'status':1,'id':cmsId}
        atl = cmsObj.getOne('*',condition)
        if atl == None:
            return self.error('文章不存在')
        from web import form
        validList=(
            form.Textbox("name",form.regexp(r".{3,100}$", '姓名需为3~100个字符')),
            form.Textbox("content",form.regexp(r".{1,100}$", '评论内容需为3~100个字符')),
            form.Textbox("email", form.regexp(r".*@.*", '邮箱格式错误')),
            form.Textbox("email",form.regexp(r".{5,100}$", '邮箱需为5~100个字符')),
            )
        if not self.validates(validList):
            return self.error(self.errorMessage)
        date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        HTTP_X_REAL_IP =  web.ctx.env.get('HTTP_X_REAL_IP')
        ip=HTTP_X_REAL_IP if HTTP_X_REAL_IP else web.ctx.ip
        data={
            'cmsId':cmsId,
            'content':userInput['content'],
            'name':userInput['name'],
            'email':userInput['email'],
            'createTime':date,
            'ip':ip,
            'status':1
        }
        model.comment().insert(data)
        data = {'commentCount':atl['commentCount']+1}
        model.cms().update(data,condition)
        return self.success('评论成功',self.referer)
