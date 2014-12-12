#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='/'
WEB_NAME='上帝De助手 的博客'
WEB_SUBNAME='我只生产内容，我不是互联网的搬运工！'
WEB_TITLE='seo基础入门教程_网络营销入门学习_移动互联网创业项目故事'
WEB_KEYWORDS='seo基础入门教程，互联网络营销入门学习，移动互联网创业项目，互联网创业故事'
WEB_DESCRIPTION='发布有关seo相关的基础学习教程，开发seo相关的工具；学习互联网思维，并运用互联网思维进行网络营销策划；同时关注各行业互联网、移动互联网创业项目的发展。'
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
