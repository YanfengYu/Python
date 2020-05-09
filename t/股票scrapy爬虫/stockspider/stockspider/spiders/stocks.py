# -*- coding: utf-8 -*-
import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stock_list.html#sh']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r"[s][hz]\d{6}", href)[0]
                url = "http://so.cfi.cn/so.aspx?txquery=" + str(stock) + ".html"
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infoDict = {}
        try:
            list1 = response.css('#tdquote')
            if list1 != []:
                lsst = list1.xpath('.//text()').extract()
                if lsst != []:
                    name = lsst[0]
                    price = lsst[4]
                    infoDict[name] = price
        except Exception as e:
            print(e)

        yield infoDict


