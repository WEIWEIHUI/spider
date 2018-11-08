# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.spiders.build import BuildSpider
from xlwt import *

class TutorialPipeline(object):
 

    def  open_spider(self,spider):
     
        self.workname=spider.filename
        self.items = []
        


    def process_item(self, item, spider):
      
        self.items.append(item)
        return item

    def close_spider(self,spider):
        if(len(self.items) > 0):
            self.write_info_to_excle()
        else:
            self.write_nothing_to_excle()

    def write_info_to_excle(self):
       
        workbook = Workbook(encoding = 'utf-8')   #指定file以utf-8的格式打开  
        worksheet = workbook.add_sheet('Sheet1')  #指定打开的文件名  
        #表头
        worksheet.write(0, 0, u'工程名称')
        worksheet.write(0, 1, u'施工许可证号')
        worksheet.write(0, 2, u'所在区县')
        worksheet.write(0, 3, u'建设单位')
        worksheet.write(0, 4, u'工程规模(平方米)')
        worksheet.write(0, 5, u'发证日期')
        worksheet.write(0, 6, u'建设地址')
        worksheet.write(0, 7, u'施工单位')
        i = 1
        for info in self.items:                       
            worksheet.write(i, 0, info['pn'])
            worksheet.write(i, 1, info['pa'])
            worksheet.write(i, 2, info['county'] )
            worksheet.write(i, 3, info['b_com'])
            worksheet.write(i, 4, info['area'])
            worksheet.write(i, 5, info['date'])
            worksheet.write(i, 6, info['addr'])
            worksheet.write(i, 7, info['m_com'])
            i = i + 1
           
        workbook.save(self.workname)
        return

    def write_nothing_to_excle(self):
        workbook = Workbook(encoding = 'utf-8')   #指定file以utf-8的格式打开  
        worksheet = workbook.add_sheet('Sheet1')  #指定打开的文件名  
        worksheet.write(0, 0, u'您查找的信息不存在')
        workbook.save(self.workname)
        return
