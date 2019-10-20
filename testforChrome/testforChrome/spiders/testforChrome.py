# -*- coding: utf-8 -*-
import scrapy


class TestforchromeSpider(scrapy.Spider):
    name = 'testforChrome'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
