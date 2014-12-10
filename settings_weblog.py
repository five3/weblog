#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='/'
WEB_NAME='上帝De助手 的博客'
WEB_SUBNAME='我只生产内容，我不是互联网的搬运工！'
WEB_TITLE='seo基础入门教程_seo入门学习_seo优化教程'
WEB_KEYWORDS='seo基础入门教程，seo入门学习，seo优化教程'
WEB_DESCRIPTION='本站长期发布有关seo相关的基础学习教程，包括seo建站流程、seo常见问题，seo日常维护等；另外也会开发和发布一些建站工具！是各建站新手和seo新手的学习之地。'
TEMPLATE_THEME='default'
PER_PAGE_COUNT = 10

#账号相关
ADMIN_USERNAME = 'five3@163.com'
ADMIN_PASSWORD='chenxiaowu'

#项目配置
DEFAULT_PATH='/index/index'
DEBUG_SWITCH=True
STATUS_LIST = {1:'发布',0:'草稿'}

#路径信息
ROOT_PATH=os.getcwd()+'/'
DATA_DIR_PATH=ROOT_PATH+'data/'
TMP_DIR_PATH=ROOT_PATH+'data/cache/'

#目录结构
UPLOAD_DIR='static/upload/'
TPL_DIR = 'templates'
ADMIN_TPL_DIR='admin'

#数据库信息
# DB_TYPE='sqlite'
# DB_STRING=DATA_DIR_PATH+'cms.db'
# DB_TABEL_PREFIX='cms_'
DB_TYPE='mysql'
DB_STRING='localhost/3306/root/changeit!/weblog'
DB_TABEL_PREFIX='cms_'
