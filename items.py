# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pn = scrapy.Field() #工程名称
    pa = scrapy.Field() #施工许可证号
    county = scrapy.Field() #所在区县
    b_com = scrapy.Field() #建设单位
    area = scrapy.Field() #工程规模（平方米）
    date = scrapy.Field() #发证日期
    addr = scrapy.Field() #建设地址
    m_com = scrapy.Field() #施工单位




