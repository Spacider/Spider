#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from Baike_Spaider import html_downloader
from Baike_Spaider import html_outputer
from Baike_Spaider import html_paraser
from Baike_Spaider import url_manager

__author__ = 'Gary'


# 爬虫主函数

class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # 下载器
        self.downloader = html_downloader.HtmlDownloader()
        # 解析器
        self.paraser = html_paraser.HtmlParaser()
        # 输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加入口url
        self.urls.add_new_url(root_url)
        # 如果有新的url地址
        while self.urls.has_new_url():
            try:
                # 从网页url管理器取出
                new_url = self.urls.get_new_url()
                # 输入解析的是第几个url
                print('craw %d : %s' % (count, new_url))
                # 下载对应的页面
                html_cont = self.downloader.download(new_url)
                # 运行界面的解析，得到新的url数据
                new_urls, new_data = self.paraser.parse(new_url, html_cont)
                # 将新的url补充进url数据
                self.urls.add_new_urls(new_urls)
                # 收集新的数据
                self.outputer.collect_data(new_data)

                if count >= 200:
                    break
                count +=1

            except:
               print('craw failed')

        # 输出数据
        self.outputer.output_html()


if __name__ == '__main__':
    # 输入待抓取url
    root_url = 'https://baike.baidu.com/item/Python'
    # 创造一个Spider
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)

    

