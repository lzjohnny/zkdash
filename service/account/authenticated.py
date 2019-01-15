#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
摘    要: authenticated.py
创 建 者: liuzijian
创建日期: 2018-01-15
"""
import functools
import urlparse
from urllib import urlencode
from tornado.web import HTTPError


def web_authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            if self.request.method in ("GET", "HEAD"):
                url = self.get_login_url()
                if "?" not in url:
                    if urlparse.urlsplit(url).scheme:
                        # if login url is absolute, make next absolute too
                        next_url = self.request.full_url()
                    else:
                        next_url = self.request.uri
                    url += "?" + urlencode(dict(next=next_url))
                self.redirect(url)
                return
            raise HTTPError(403)
        return method(self, *args, **kwargs)
    return wrapper


def api_authenticated(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        return method(self, *args, **kwargs)
    return wrapper


if __name__ == '__main__':
    pass
