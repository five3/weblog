#!/usr/bin/env python
#coding=utf-8
import os
#网站信息
WEB_URL='/'
WEB_NAME=' 91小象网，有礼有祝福！'
WEB_SUBNAME='让送礼从此轻松又愉快，让祝福从此时时永相伴！'
WEB_TITLE='创意礼品店_送礼又许愿'
WEB_KEYWORDS='创意礼品店，许愿树，许愿墙，创意生日礼物'
WEB_DESCRIPTION='专注于学生、白领等青年人群的送礼导购网站，提供增值的在线许愿服务。'
TEMPLATE_THEME='xiaoxiang'
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
DB_STRING='localhost/3306/root/changeit!/xiaoxiang'
DB_TABEL_PREFIX='cms_'
