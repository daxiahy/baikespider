#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urlparse
from bs4 import BeautifulSoup

#网页解析器
class HtmlParser(object):

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        #将页面转为soup对象
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        #从页面中获取urls
        new_urls = self._get_new_urls(page_url, soup)
        #从页面中获取价值数据
        new_data = self._get_new_data(page_url, soup)
        #返回出新url列表和数据列表
        return new_urls, new_data

    #获取新url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #获取是词条的url链接
        links = soup.find_all('a', href=re.compile(r"/item/.+?"))
        for link in links:
            new_url = link['href']
            #拼接url
            new_full_url = urlparse.urljoin('http://baike.baidu.com', new_url)
            new_urls.add(new_full_url)
        #返回出有效urls
        return new_urls

    #提取价值数据
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url

        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_= "lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        print res_data

        return res_data
