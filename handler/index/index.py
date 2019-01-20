#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014,掌阅科技
All rights reserved.

摘    要: index.py
创 建 者: zhuangshixiong
创建日期: 2015-10-09
"""
from handler.bases import CommonBaseHandler
from lib import route
from service.account.authenticated import web_authenticated


@route(r'/')
class IndexHandler(CommonBaseHandler):

    '''配置管理系统页面入口
    '''

    @web_authenticated
    def response(self):
        return self.render('index.html')


@route(r'/auth/index/main', '首页')
class IndexMainHandler(CommonBaseHandler):

    '''首页
    '''

    @web_authenticated
    def response(self):
        self.finish()
