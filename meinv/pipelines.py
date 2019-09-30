# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MeinvPipeline(object):
    def get_media_requests(self, item, info):
        yield Request(url=item['imgurl'])
