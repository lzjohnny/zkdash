#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
摘    要: action.py
创 建 者: liuzijian
创建日期: 2018-01-14
"""
from handler.bases import CommonBaseHandler
from lib import route
from conf.settings import (
    WEB_SITE,
)


@route(r'/auth/action/register')
class ActionRegisterHandler(CommonBaseHandler):

    '''注册入口
    '''

    def response(self):
        self.redirect(WEB_SITE['register_url'])


@route(r'/auth/action/login')
class ActionLoginHandler(CommonBaseHandler):

    '''登录入口
    '''

    def response(self):
        self.redirect(WEB_SITE['login_url'])
