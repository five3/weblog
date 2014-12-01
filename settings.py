#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='http://www.chenxiaowu.com/'
WEB_TITLE='上帝De助手 的博客'
WEB_NAME='SEO优化_SEM营销'
WEB_DESCRIPTION='我不生产内容，我只是互联网的搬运工！'
WEB_KEYWORDS=['seo优化', 'sem营销', '网络推广']
TEMPLATE_THEME='default'
PER_PAGE_COUNT = 10

#账号相关
ADMIN_USERNAME = 'five3@163.com'
ADMIN_PASSWORD='chenxiaowu'

#项目配置
DEFAULT_PATH='/index/index'
DEBUG_SWITCH=True
CATEGORY_LIST = {'default':'默认分类', 'seo':'SEO', 'life':'生活'}
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
DB_STRING='localhost/3306/root/root/weblog'
DB_TABEL_PREFIX='cms_'
