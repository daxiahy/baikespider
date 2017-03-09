#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

#url控制器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    #添加url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    #添加多条url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    #新url列表是否有url
    def has_new_url(self):
        return len(self.new_urls) != 0

    #从新url列队中取出url 并添加至旧url中
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url



