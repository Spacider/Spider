#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
__author__ = 'Gary'

from bs4 import BeautifulSoup
import re
import urllib.parse

# 爬虫解析器

class HtmlParaser(object):

    def _get_new_urls(self, page_url, soap):
        new_urls = set()
        # 获取所有的链接（使用正则表达式）
        links = soap.find_all('a', href= re.compile(r"/item/"))
        for link in links:
            new_url = link['href']
            #  由于是不完整的url地址，所以需要拼接成完整的
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soap):
        res_data = {}

        # 返回当前url
        res_data['url'] = page_url

        # 拷贝我们需要爬取的东西，方便书写解析器
        # < dd >class ="lemmaWgt-lemmaTitle-title" >
        # < h1 > Python < / h1 >

        # 得到标题的标签
        title_node = soap.find('dd', class_= 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        #< div class ="lemma-summary" label-module="lemmaSummary" >
        # 得到简介的标签
        summary_node = soap.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        # 将cont 加载进soap
        soap = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        # 进行2个解析
        new_urls = self._get_new_urls(page_url, soap)
        new_data = self._get_new_data(page_url, soap)
        return  new_urls, new_data

