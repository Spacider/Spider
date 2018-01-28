#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

# 爬虫下载器

import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()

# # 使用request库
# import requests
#
#
# class HtmlDownloader(object):
#     def download(self, url):
#         if url is None:
#             return None
#
#         r = requests.get(url)
#
#         if r.status_code !=200:
#             return None
#
#         return r.text

