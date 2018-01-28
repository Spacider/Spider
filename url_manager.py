#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

# 爬虫url管理器

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self, url):
        if url is None:
            return
        # 如果这个url既不在新的url列表钟又不在旧的url列表中，说明这是一个新的url地址
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0 :
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        # 如果新的url长度不等于0，就说明有的地址
        return len('self.new_urls') != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

