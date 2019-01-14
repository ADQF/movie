# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 管道： 数据清洗、去重。
# 持久化：写txt，csv。写入数据库。

# scrapy框架将爬取spider模块和处理层pipeline分离开，使得程序更容易扩展。
# spider yield生成的item会交给pipline处理。如果爬取速度跟处理速度不一致的话，scrapy框架会自动调度。
#

class MoviePipeline(object):
    def process_item(self, item, spider):
        with open('my_meiju.txt', 'a', encoding='utf_8') as f:
            f.write(str(item.name) + '\n')
        return item
