#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
摘    要: action.py
创 建 者: liuzijian
创建日期: 2018-1-14
"""
from handler.bases import CommonBaseHandler
from lib import route


@route(r'/auth/action/register')
class ActionRegisterHandler(CommonBaseHandler):

    '''注册入口
    '''

    def response(self):
        self.finish()


@route(r'/auth/action/login')
class ActionLoginHandler(CommonBaseHandler):

    '''登录入口
    '''

    def response(self):
        self.finish()
