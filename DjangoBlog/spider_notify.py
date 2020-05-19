#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: superstrongz
@license: MIT Licence 
@contact: 857508399@qq.com
@site: http://www.superstrongz.com/
@software: PyCharm
@file: spider_notify.py
@time: ??
"""

from django.contrib.sitemaps import ping_google
import requests
from django.conf import settings
import logging
import re

logger = logging.getLogger(__name__)


class SpiderNotify():
    @staticmethod
    def baidu_notify(urls):
        try:
            data = '\n'.join(urls)
            result = requests.post(settings.BAIDU_NOTIFY_URL, data=data)
            logger.info(result.text)
        except Exception as e:
            logger.error(e)

    @staticmethod
    def __google_notify():
        try:
            ping_google('/sitemap.xml')
        except Exception as e:
            logger.error(e)

    @staticmethod
    def notify(url):

        SpiderNotify.baidu_notify(url)
        SpiderNotify.__google_notify()

    @staticmethod
    def push_urls( urls):
        headers = {
            'User-Agent': 'curl/7.12.1',
            'Host': 'data.zz.baidu.com',
            'Content - Type': 'text / plain',
            'Content - Length': '83'
        }
        try:
            html = requests.post(settings.BAIDU_NOTIFY_URL, headers=headers, data=urls, timeout=5).text
            return html
        except:
            return "{'error':404,'message':'请求超时，接口地址错误！'}"

    @staticmethod
    def get_urls(url):
        '''提取网站sitemap中所有链接，参数必须是sitemap的链接'''
        try:
            html = requests.get(url,timeout=5).text
        except:
            return 'miss'
        else:
            urls = re.findall('<loc>(.*?)</loc>', html)
            return '\n'.join(urls)
